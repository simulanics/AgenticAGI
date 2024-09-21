import os
import platform
import subprocess
import threading
import json
import asyncio  # Import asyncio for async calls
import inspect
import urllib.parse  # Import for URL decoding

class AGIWrapper:
    def __init__(self, api_key, task, exe_path, apiendpoint="https://api.groq.com/openai/v1/chat/completions",
                 confidence=None, contextlimit=50, cooldown=10, fao=False, hitm=True, inputprice=None,
                 interactive=False, maxcorrections=3, model=None, outputprice=None, pytimeout=60, schema=None,
                 selfcorrect=False, showprice=False, steplimit=25, colormode=False):
        """
        Initialize the AGIWrapper class.

        :param api_key: API key for authentication.
        :param task: Task for the AGI to execute.
        :param exe_path: Path to the executable file.
        :param apiendpoint: API endpoint URL.
        :param confidence: Optional confidence parameter.
        :param contextlimit: Limit for the context size.
        :param cooldown: Cooldown time between executions.
        :param fao: Flag to enable or disable First-Action-Only mode.
        :param hitm: Flag to enable or disable Hit-The-Mark mode.
        :param inputprice: Optional price for input.
        :param interactive: Flag to enable or disable interactive mode.
        :param maxcorrections: Maximum number of corrections allowed.
        :param model: Model identifier.
        :param outputprice: Optional price for output.
        :param pytimeout: Timeout for the Python process.
        :param schema: Optional schema parameter.
        :param selfcorrect: Flag to enable or disable self-correction mode.
        :param showprice: Flag to show or hide the price.
        :param steplimit: Step limit for execution.
        """
        self.api_key = api_key
        self.task = task
        self.apiendpoint = apiendpoint
        self.confidence = confidence
        self.contextlimit = contextlimit
        self.cooldown = cooldown
        self.fao = fao
        self.hitm = hitm
        self.inputprice = inputprice
        self.interactive = interactive
        self.maxcorrections = maxcorrections
        self.model = model
        self.outputprice = outputprice
        self.pytimeout = pytimeout
        self.schema = schema
        self.selfcorrect = selfcorrect
        self.showprice = showprice
        self.steplimit = steplimit
        self.colormode = colormode

        # Ensure the executable path is provided
        if not exe_path:
            raise ValueError("AGI executable path must be specified.")
        self.exe_path = exe_path

        # Define callbacks
        self.on_thought = None
        self.on_action = None
        self.on_observation = None
        self.on_final_answer = None
        self.on_ctsi_score = None  # Callback for CTSI score

    def set_callbacks(self, on_thought=None, on_action=None, on_observation=None, on_final_answer=None, on_ctsi_score=None):
        """Set callbacks for various events."""
        self.on_thought = on_thought
        self.on_action = on_action
        self.on_observation = on_observation
        self.on_final_answer = on_final_answer
        self.on_ctsi_score = on_ctsi_score  # Set the CTSI score callback

    async def _handle_output(self, line):
        """
        This method processes the output from the AGI and calls the appropriate callbacks.
        """
        if "Thought:" in line and self.on_thought:
            thought_data = line.split("Thought:", 1)[1].strip()
            if inspect.iscoroutinefunction(self.on_thought):
                await self.on_thought(thought_data)
            else:
                self.on_thought(thought_data)  # Non-async callback

        elif "Action:" in line and self.on_action:
            action_data = line.split("Action:", 1)[1].strip()
            if inspect.iscoroutinefunction(self.on_action):
                await self.on_action(action_data)
            else:
                self.on_action(action_data)  # Non-async callback

        elif "Observation:" in line and self.on_observation:
            observation_data = line.split("Observation:", 1)[1].strip()
            if inspect.iscoroutinefunction(self.on_observation):
                await self.on_observation(observation_data)
            else:
                self.on_observation(observation_data)  # Non-async callback

        elif "FINAL ANSWER:" in line and self.on_final_answer:
            answer_data = line.split("FINAL ANSWER:", 1)[1].strip()
            
            if "CTSI Score:" in answer_data:
                final_answer_data = answer_data.split("CTSI Score:", 1)[0].strip()
                CTSILine = line.split("CTSI Score:", 1)[1].strip()
                
                if inspect.iscoroutinefunction(self.on_final_answer):
                    await self.on_final_answer(final_answer_data)
                else:
                    self.on_final_answer(final_answer_data)  # Non-async callback
                
                
                try:
                    ctsi_scores = json.loads(CTSILine)
                    if inspect.iscoroutinefunction(self.on_ctsi_score):
                        await self.on_ctsi_score(ctsi_scores)
                    else:
                        self.on_ctsi_score(ctsi_scores)  # Non-async callback
                except json.JSONDecodeError:
                    pass  # Ignore lines that are not valid JSON
            else:            
            
                if inspect.iscoroutinefunction(self.on_final_answer):
                    await self.on_final_answer(answer_data)
                else:
                    self.on_final_answer(answer_data)  # Non-async callback
            

        elif line.startswith('{') and self.on_ctsi_score:
            try:
                ctsi_scores = json.loads(line)
                if inspect.iscoroutinefunction(self.on_ctsi_score):
                    await self.on_ctsi_score(ctsi_scores)
                else:
                    self.on_ctsi_score(ctsi_scores)  # Non-async callback
            except json.JSONDecodeError:
                pass  # Ignore lines that are not valid JSON

    def _read_process_output(self, process):
        """Reads the output from the process and handles it via callbacks."""
        async def read_output():
            output_buffer = ""
            for line in iter(process.stdout.readline, ''):
                # Decode the URL-encoded line
                decoded_line = urllib.parse.unquote(line)
                output_buffer += decoded_line  # Accumulate decoded lines
                
                # Check if there's a complete thought/action/observation in the buffer
                if "Thought:" in output_buffer:
                    await self._handle_output(output_buffer)
                    output_buffer = ""  # Clear the buffer after handling
                elif "Action:" in output_buffer:
                    await self._handle_output(output_buffer)
                    output_buffer = ""
                elif "Observation:" in output_buffer:
                    await self._handle_output(output_buffer)
                    output_buffer = ""
                elif "Final Answer:" in output_buffer:
                    await self._handle_output(output_buffer)
                    output_buffer = ""

            # Process any remaining content in the buffer after the loop
            if output_buffer:
                await self._handle_output(output_buffer)

        asyncio.run(read_output())

    def execute(self):
        """Run the executable with the provided arguments."""
        cmd = [
            self.exe_path, "--apikey", self.api_key, "--task", self.task, "--apiendpoint", self.apiendpoint,
            "--contextlimit", str(self.contextlimit), "--cooldown", str(self.cooldown), "--fao", str(self.fao),
            "--hitm", str(self.hitm), "--interactive", str(self.interactive), "--maxcorrections", str(self.maxcorrections),
            "--pytimeout", str(self.pytimeout), "--selfcorrect", str(self.selfcorrect), "--showprice", str(self.showprice),
            "--steplimit", str(self.steplimit), "--urlencode", "True", "--colormode", str(self.colormode)
        ]

        # Optional arguments
        if self.confidence is not None:
            cmd.extend(["--confidence", str(self.confidence)])
        if self.inputprice is not None:
            cmd.extend(["--inputprice", str(self.inputprice)])
        if self.outputprice is not None:
            cmd.extend(["--outputprice", str(self.outputprice)])
        if self.model is not None:
            cmd.extend(["--model", self.model])
        if self.schema is not None:
            cmd.extend(["--schema", self.schema])

        # Print the command for debugging purposes
        print("Command being executed:", " ".join(cmd))

        # Suppress output by redirecting stdout and stderr to subprocess.PIPE
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1, text=True)

        # Run the process output reader in a separate thread
        output_thread = threading.Thread(target=self._read_process_output, args=(process,))
        output_thread.start()

        process.wait()  # Wait for the process to finish
        output_thread.join()

        return process.returncode
