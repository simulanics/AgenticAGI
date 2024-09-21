# AgenticAGI Python Integration Guide

Welcome to the AgenticAGI Python library integration guide. This document explains how to use the AgenticAGI wrapper library in your Python projects to interact with AGI systems seamlessly.

## Installation

You can install the library in two ways:

### From Source
Clone the repository and install from the root directory of the Python library source code:
```bash
pip install .
```

### From PyPI (Stable Release)
To install the latest stable release, use the following command:
```bash
pip install AgenticAGI
```

## Usage Example

### Setting Up the AGI System

Before starting, ensure you have the AGI system's executable and LLM API key (unless using a local model such as Ollama or Llama). Specify the executable path, and set up the API endpoint for communication.

```python
from agenticagi.agi_wrapper import AGIWrapper

# The AGI system executable location must be specified.
# Example path to the executable:
AGIPath = r"C:\Users\mcomb\Desktop\executables\windows\agi.exe"
# Supported Platforms: Windows, MacOS, Linux - x86 32/64 bit and ARM 32/64 bit - including Raspberry Pi

# Define your callback functions to process the AGI's outputs.
def thought_callback(data):
    print(f"Callback Thought: {data}")

def action_callback(data):
    # Actions can be handled here. You can replace the print statement with actual code logic.
    print(f"Callback Action: {data}")

def observation_callback(data):
    print(f"Callback Observation: {data}")

def final_answer_callback(data):
    print(f"Callback Final Answer: {data}")

def ctsi_callback(scores):
    print(f"Callback CTSI Scores: Confidence={scores.get('confidence')}, "
          f"Truthfulness={scores.get('truthfulness')}, "
          f"Satisfaction={scores.get('satisfaction')}, "
          f"Invalid={scores.get('invalid')}")
```

### Initializing the AGI Wrapper

Next, initialize the `AGIWrapper` by specifying parameters like the API key, model, and the task to be solved by the AGI. **Ensure that both `interactive=False` and `colormode=False`** are set to use the callback functionality correctly.

```python
# Initialize the AGI wrapper
agi = AGIWrapper(
    api_key="YOUR_API_KEY",  # Replace with your actual API key
    apiendpoint="https://api.groq.com/openai/v1/chat/completions",  # API Endpoint
    model="llama-3.1-70b-versatile",  # Model to use
    interactive=False,  # Must be False for callbacks to work
    confidence=True,  # Enable confidence scoring
    hitm=False,  # Human-in-the-middle mode
    cooldown=3,  # Cooldown period between LLM requests (seconds)
    task="Solve x = x^2 + 1",  # The task to solve
    exe_path=AGIPath,  # Path to the AGI executable
    colormode=False  # Must be False for callbacks to work
)
```

### Setting Callbacks

You must define various callback functions to handle thought processes, actions, observations, final answers, and confidence scores (CTSI). These callbacks are then registered using the `set_callbacks` method.

```python
# Set the callback functions
agi.set_callbacks(
    on_thought=thought_callback, 
    on_action=action_callback, 
    on_observation=observation_callback, 
    on_final_answer=final_answer_callback,
    on_ctsi_score=ctsi_callback  # CTSI score callback
)
```

### Executing the AGI Task

Finally, execute the AGI task by calling the `execute` method, which will trigger the AGI system to solve the given task. The process output will be handled by the previously defined callbacks.

```python
# Execute the AGI process
agi.execute()
```

### Full Example

Here's the complete example of how to set up and run AgenticAGI with the Python wrapper:

```python
from agenticagi.agi_wrapper import AGIWrapper

# Specify the AGI executable location.
AGIPath = r"C:\Users\mcomb\Desktop\executables\windows\agi.exe"

# Define callback functions to process AGI outputs.
def thought_callback(data):
    print(f"Callback Thought: {data}")

def action_callback(data):
    print(f"Callback Action: {data}")

def observation_callback(data):
    print(f"Callback Observation: {data}")

def final_answer_callback(data):
    print(f"Callback Final Answer: {data}")

def ctsi_callback(scores):
    print(f"Callback CTSI Scores: Confidence={scores.get('confidence')}, "
          f"Truthfulness={scores.get('truthfulness')}, "
          f"Satisfaction={scores.get('satisfaction')}, "
          f"Invalid={scores.get('invalid')}")

# Initialize the AGI wrapper
agi = AGIWrapper(
    api_key="YOUR_API_KEY",  # Replace with your actual API key
    apiendpoint="https://api.groq.com/openai/v1/chat/completions",  # API Endpoint
    model="llama-3.1-70b-versatile",  # Model to use
    interactive=False,  # Must be False for callbacks to work
    confidence=True,  # Enable confidence scoring
    hitm=False,  # Human-in-the-middle mode
    cooldown=3,  # Cooldown period between LLM requests (seconds)
    task="Solve x = x^2 + 1",  # The task to solve
    exe_path=AGIPath,  # Path to the AGI executable
    colormode=False  # Must be False for callbacks to work
)

# Set the callback functions
agi.set_callbacks(
    on_thought=thought_callback, 
    on_action=action_callback, 
    on_observation=observation_callback, 
    on_final_answer=final_answer_callback,
    on_ctsi_score=ctsi_callback  # CTSI score callback
)

# Execute the AGI process
agi.execute()
```

### API Overview

The `AGIWrapper` provides a flexible interface to configure and execute AGI tasks. Below is a list of the available flags and their purposes:

- **`api_key`** (required): The API key used to authenticate your requests.
- **`task`** (required): The task for the AGI to execute.
- **`exe_path`** (required): Path to the AGI executable file.
- **`apiendpoint`**: The API endpoint for the AGI service (default is `https://api.groq.com/openai/v1/chat/completions`).
- **`confidence`**: Whether to enable confidence scoring for the AGI output.
- **`contextlimit`**: The maximum number of memories used to make decisions (default is `50`).
- **`cooldown`**: Duration in seconds between LLM requests (default is `10`).
- **`fao`**: Enable Final-Answer-Only mode (default is `False`).
- **`hitm`**: Enable Human-In-The-Middle mode, which allows AGI to ask the user for information during task completion (default is `True`).
- **`inputprice`**: Optional price for input tokens per million (for calculating costs).
- **`interactive`**: **Must be disabled** (set to `False`) for callback functionality to work.
- **`maxcorrections`**: Maximum number of self-corrections allowed during task execution (default is `3`).
- **`model`**: The LLM model to use for the task (e.g., `llama-3.1-70b-versatile`).
- **`outputprice`**: Optional price for output tokens per million (for calculating costs).
- **`pytimeout`**: Timeout in seconds for Python code execution during task processing (default is `60` seconds).
- **`schema`**: A custom tag or JSON structure to define the final answer response format (optional).
- **`selfcorrect`**: Enable self-correction mode where the AGI can correct its own mistakes (default is `False`).
- **`showprice`**: Show token usage and input/output pricing after task completion (default is `False`).
- **`steplimit`**: The maximum number of steps the AGI can perform before answering or giving up (default is `25`).
- **`colormode`**: **Must be disabled** (set to `False`) when using callbacks to prevent conflicts with text formatting.

### Example Output

```
Callback Thought: I need to solve the equation x = x^2 + 1. To do this, I can rearrange it to form a quadratic equation and then use the quadratic formula to solve for x.
Callback Action: python [python: Solve the quadratic equation using Python.]
Callback Observation: The solutions are (0.5+0.8660254037844386j) and (0.5-0.8660254037844386j).
Callback Final Answer: The equation x = x^2 + 1 has no real solutions, but it has two complex solutions: x = 0.5 + i√3/2 and x = 0.5 - i√3/2.
Callback CTSI Scores: Confidence=100, Truthfulness=100, Satisfaction=100, Invalid=0
```

---

**Important Notes**:
- **`interactive=False`** and

 **`colormode=False`** are required for callbacks to work.
- Custom callbacks can be defined for handling AGI thoughts, actions, observations, final answers, and confidence scores.
