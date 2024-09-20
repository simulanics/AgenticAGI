# AgenticAGI - by [Simulanics Technologies](https://www.simulanics.com)

AgenticAGI is Strawberry Logic for ALL LLMs - The AGI system allows all LLMs to operate like OpenAI's o1-preview/o1-mini models - only more useful...

**Welcome to AgenticAGI – The Future of Autonomous AI Reasoning** 🤖🚀

AgenticAGI is a cutting-edge AI system that turns any large language model (LLM) into a powerful, self-correcting, deeply reasoning agent. By implementing a transparent and iterative thought process, AgenticAGI delivers more accurate, flexible, and efficient interactions, providing continuous improvement with every task. Whether you're solving complex problems, running code, or generating data visualizations, AgenticAGI is your comprehensive problem-solving partner.

## Features

- ✅ **Deep Chain-of-Thought Reasoning**  
  Unlike traditional AI systems that generate quick responses based on surface-level understanding, AgenticAGI dives deeper to ensure that every answer is logical and highly accurate.

- ✅ **Self-Correction & Confidence Scoring**  
  AgenticAGI doesn’t just provide answers—it self-corrects and attaches confidence scores, ensuring reliable outcomes for any task.

- ✅ **Transparency & Full Auditability**  
  Gain full control and insight into AgenticAGI’s reasoning process. Every decision can be reviewed, audited, and trusted.

- ✅ **Multi-Model Compatibility**  
  AgenticAGI works with various LLM providers, including OpenAI, Ollama, Groq, and more, offering flexibility without being tied to a single ecosystem.

- ✅ **Reinforcement Learning**  
  Continuous learning ensures that the system becomes more efficient and accurate over time, adapting to user needs.

- ✅ **Real-Time Actions**  
  AgenticAGI is capable of web searches 🌐, executing Python scripts 🐍, interacting with hardware 🛠️, and more, offering solutions beyond simple responses.

## Installation

### 1. Download 💾

Choose your preferred OS from the releases page:

- [macOS 64 bit](#)
- [macOS ARM 64 bit](#)
- [Windows 32 bit](#)
- [Windows 64 bit](#)
- [Linux 32 bit](#)
- [Linux 64 bit](#)
- [Raspberry Pi ARM 32/64 bit](#)

### 2. Extract 📂

Once downloaded, extract the contents to a directory of your choice. **AgenticAGI** can even run directly from a USB for ultimate portability! 🖥️💡

### 3. Run ▶️

Navigate to the directory and simply execute the appropriate file for your platform (including required command-line flags):

- For Windows: `agi.exe`
- For Linux/macOS: `./agi`

You’re ready to unlock the full potential of AGI reasoning! 🔓🤖

**MacOS users will need to run the included `codesign.sh` file in order to sign and run the AGI locally.**

## Usage

AgenticAGI is a command-line tool that can be customized to fit your needs. Here’s a basic example of how to get started:

### Interactive Mode 💬

Launch AgenticAGI in interactive mode where it awaits your commands:

```bash
agi --interactive true --cooldown 3 --apikey YOUR_API_KEY --model llama-3.1-70b-versatile
```

### Fully Autonomous Mode 🤖⚙️

Run a task autonomously, such as retrieving a WiFi password, with no human-in-the-middle:

```bash
agi --cooldown 3 --apikey YOUR_API_KEY --model llama-3.1-70b-versatile --task "Retrieve WiFi password for 'TheNet'"
```

### Available Flags 🏁

- `--apiendpoint` : Completions URL endpoint (DEFAULT = `https://api.groq.com/openai/v1/chat/completions`).
- `--apikey` : LLM API key.
- `--confidence` : (Confidence/Truthfulness/Satisfaction/Validity) score (0-100%) of the final answer, provided in JSON format (DEFAULT = True).
- `--contextlimit` : Maximum number of memories used to make decisions (DEFAULT = 50).
- `--cooldown` : Duration in seconds between LLM requests (DEFAULT = 10).
- `--fao` : Final Answer Only. If set to true, see `--schema` flag for structured data output.
- `--hitm` : Human-in-the-middle allows the AGI to ask the user for information during task completion (DEFAULT = True).
- `--inputprice` : Set the INPUT price of tokens per million. See `--showprice` flag.
- `--interactive` : Start Agentic AGI in interactive mode. Each task run is a new session (DEFAULT = False).
- `--maxcorrections` : Sets the self-correction limit (DEFAULT = 3).
- `--model` : LLM model to use.
- `--newlines` : Outputs newlines as \n (DEFAULT = False).
- `--outputprice` : Set the OUTPUT price of tokens per million. See `--showprice` flag.
- `--pytimeout` : Python script timeout period (in seconds) before Python is terminated and control is returned to the AGI (DEFAULT = 60 sec).
- `--schema` : A defined custom tag (`<search>{query}</search>`) or JSON structure (`{ "ans": {{final_response}} }`) for the 'final answer'/response. See `--fao` flag.
- `--selfcorrect` : Allow the model to self-correct when confidence/truthfulness < 92%, satisfaction < 85%, or inaccurate/invalid perception > 3% (DEFAULT = False). When enabled, confidence will auto-enable. See `--maxcorrections` flag.
- `--showprice` : Show token usage and input/output pricing per task completion. See `--inputprice` and `--outputprice` flags (DEFAULT = False).
- `--steplimit` : The maximum number of steps the AGI can perform before answering or giving up (DEFAULT = 25).
- `--task` : The task to be solved or completed.
- `--urlencode` : Encodes output using URL encoding (DEFAULT = False).

**Note**: By default, Groq is the default LLM service if an `--apiendpoint` is not specified.

For a full list of commands, run:

```bash
agi --help
```

## Examples 📖

### Example 1: Solving Advanced Problems 🐍

```bash
agi --task "What is the integral of x^2?" --model llama-3.1-70b-versatile --apikey YOUR_API_KEY
```

AgenticAGI will not only give you the answer but also walk through the steps to reach that conclusion using Python! ✨📐

### Example 2: Automating a Web Search and Content Creation 🌐

```bash
agi --task "Search the web for the latest AI trends in 2024 and write a report" --model llama-3.1-70b-versatile --apikey YOUR_API_KEY
```

AgenticAGI can browse the web, synthesize information, and deliver actionable insights. 📊

### Example 3: Hardware Interaction 🛠️

```bash
agi --task "Install a new Python package and run a script" --model llama-3.1-70b-versatile --apikey YOUR_API_KEY
```

AgenticAGI can autonomously install tools, manage system resources, and run code. ⚙️💻

## Why AgenticAGI?

AgenticAGI stands out because it doesn’t just provide answers – it **reasons** through problems. Its adaptive learning algorithms allow it to get better with every use, making it the perfect tool for developers, data analysts, and businesses looking to leverage the next level of AI technology. 🌟

### Key Benefits 🔑

- **Increased Accuracy**: By thinking through problems, AgenticAGI reduces errors and provides more reliable outcomes.
- **Reduced Token Usage**: Efficiency in solving multi-step problems reduces the number of tokens used, cutting down costs 💰.
- **Flexible Deployment**: Use AgenticAGI with any LLM provider, whether proprietary or open-source.
- **Future-Proof**: Decentralized learning ensures that AgenticAGI stays on the cutting edge of AI technology without losing past abilities.

## Future Updates 🚀

We are continually improving AgenticAGI, with upcoming features such as:

- **Cloud-Learning Sync**: Share learned abilities with other AGI systems to enhance collective intelligence.
- **Deep Memory**: Enable AGI to retain and apply knowledge across long-term tasks, improving efficiency and learning rates.

## Testimonials 🗣️

> “AgenticAGI has been a game-changer for our data analysis team. It not only provides accurate results but shows us the reasoning behind each step.”  
> *– Samantha T., Data Scientist*  

> “Its ability to reason like a human sets AgenticAGI apart. I’ve used it to write and debug code, and it performs with precision and accuracy.”  
> *– Carlos M., Senior Developer*  

> “The transparency and self-correcting features have saved us countless hours. AgenticAGI doesn’t just give answers—it verifies them, ensuring we get the best results.”  
> *– Michael D., Data Analyst*

## Contributing 🤝

We welcome contributions! Feel free to submit issues or pull requests as we continue to grow this project. Check out our [contribution guidelines](CONTRIBUTING.md) to get started.

## License 📜

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.

## Get in Touch 📬

For any questions, feedback, or business inquiries, contact

 us via [Simulanics Technologies](https://www.simulanics.com/contact).

---

**Unlock the potential of AgenticAGI** – Your evolving, reasoning AI system that adapts to your needs. Start today and experience the future of AI! 🌍🤖
