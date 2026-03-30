## README
This repo contains the slides and code for a quick lesson on implementing an MCP tool server that I made for some colleagues.

While the slides are intended to be explained by an instructor, pairing them with this readme should make it easy enough for someone to do this lesson on their own.

The below instructions are current as of March 2026, and were tested on a Lubuntu 24.04 VM.

## Environment Setup
1. Install ollama in one of two ways:
	1. For the install script that does *a lot* of extra random stuff like create a service, jetpack stuff, CUDA stuff, and more that I didn't care about for this lesson, run the install script with `curl -fsSL https://ollama.com/install.sh | sh`
	2. For a simple manual install, run `curl -fsSL https://ollama.com/download/ollama-linux-amd64.tar.zst \ | sudo tar x -C /usr` then just use `ollama serve` when you want to run ollama. This will eat the terminal, so run it in it's own tab.
	3. Test that ollama is successfully running with `ollama -v` in a new tab.
2. Pull down a model you would like to use, that can run tools. For this walkthrough, we will use mistral-3. Why? I like croissants.
	1. `ollama pull mistral-3`
3. Set up your python environment.
	1. Install python venv if you don't already have it with `sudo apt install python3.12-venv`
	2. Create a virtual environment with `python3 -m venv mcp_env`
	3. Activate your venv with `source ./mcp_env/bin/activate`
	4. Install required packages with `pip install fastmcp ollama` to get the most up to date libraries, or use requirements.txt for the frozen versions that this lesson was tested with.
4. Clone the repo from cmilcode.
	1. `git clone [this/repo]`
5. Update the LOGFILE variable in ./tools/connectivity_tester.sh to point somewhere easy for you to access so you can review how the model executed the script.

## Edit the MCP server to add our tool
1. Edit ./student_scripts/mcp_server_STUDENT.py with your favorite text editor
	1. `vim ./student_scripts/mcp_server_STUDENT.py`
2. Your tool implementation should go in the designated space, as seen below:
```python
##########
########## STUDENT CODE STARTS HERE
##########

# Your code goes here.

##########
########## STUDENT CODE ENDS HERE
##########
```
3. If you get stuck, one way to implement the connectivity tester as a tool can be found in ./answers/mcp_server_ANSWER.py.

## Executing the MCP server and connecting via the MCP client
1. First ensure ollama is running.
	1. Run `ollama serve` if you haven't already. Remember this will eat the terminal, so run it in it's own tab.
	2. Make sure ollama is up and responsive by running `ollama -v` in a new tab.
2. Open a new terminal and start the MCP server in our mcp environment.
	1. `./mcp_env/bin/python ./student_scripts/mcp_server_STUDENT.py`
3. Open a new terminal and start the MCP client in our mcp environment.
	1. `./mcp_env/bin/python ./mcp_client_chatbot.py`
4. Ask the LLM to perform one of the tasks that requires your tool to verify your implementation.
