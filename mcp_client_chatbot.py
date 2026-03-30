# This file can be used as basic boilerplate, I laid out the comments to be very detailed.
# There are a lot of imporvements that can be made. I mention some of them in the comments.
#
# Reference: gofastmcp.com/getting-started/quickstart


# Universal Imports Go Here
import os
import sys
import json
import traceback
import asyncio
import ollama
from fastmcp import Client

# Define our client using the default of localhost:8050, using HTTP for transport.
client = Client("http://localhost:8050/mcp")

# This implementation heavily leans on kirillsaidov's ollama mcp example with the ollama function translation.
async def main(model: str) -> str:
    # Give the user some information on startup.
    print(f'Executing MCP Client using {model}. Use /quit to exit, /tools to list available tools.')

    # Start working with the client code.
    async with client:
        # Set up the history and basic system prompt.
        history = [{
            'role': 'system',
            'content': 'You are a simple llm assistant testing if a student has implemented their tools correctly.'
        }]

        # Get a list of all the tools available to the client.
        # These are the tools that we set up in the mcp_server.py script.
        mcp_tools = await client.list_tools()
        ollama_tools = []

        # Tell the user what tools are available.
        print('Available tools:')
        list_tools(mcp_tools)

        # Convert MCP tools to the Ollama format.
        # That means this script only works with Ollama.
        # You need to write your own connector if you are using something else.
        # But remember, this is for the CLIENT. The SERVER is universal for all clients that adhere to the MCP protocol.
        for tool in mcp_tools:
            ollama_tools.append({
                'type': 'function',
                'function': {
                    'name': tool.name,
                    'description': tool.description,
                    'parameters': tool.inputSchema
                }
            })

        # This is where we handle the interactive chat.
        while True:
            try:
                # Get user input, strip whitespace.
                user_input = input('>>> ').strip()

                # Check to see if the user is trying to run a command.
                # A better implementation of this would allow for more internal commands that skip prompting without a long if chain.
                if user_input.startswith('/quit'):
                    break
                elif user_input.startswith('/tools'):
                    list_tools(mcp_tools)
                    continue
                elif not user_input:
                    continue

                # Add the user's input to the history.
                history.append({'role': 'user', 'content': user_input})

                # Generate a response.
                response = ollama.chat(model, messages=history, tools=ollama_tools)

                # Check if we need to call the MCP server.
                if response.message.tool_calls:
                    for tool in response.message.tool_calls:
                        print(f'Calling {tool.function.name}')
                        print(f'\tWith parameters: {tool.function.arguments}')

                        # Call the requested tool with the given arguments.
                        result = await client.call_tool(tool.function.name, tool.function.arguments)

                        # Append the results to the history and tag it as a tool.
                        history.append({
                            'role': 'tool',
                            'content': json.dumps(result, indent=2) if isinstance(result, dict) else str(result),
                            'name': tool.function.name,
                        })

                        # Generate an additional response, with the results of the tool included in the history.
                        response = ollama.chat(model, messages=history, tools=ollama_tools)

                # Append the model's response to the history.
                history.append({
                    'role': 'assistant',
                    'content': response.message.content,
                })

                # Print the response to the screen for the user.
                print(response.message.content)
            except:
                traceback.print_exc()

def list_tools(tool_list: list) -> list:
    for tool in tool_list:
        print(f'\t- {tool.name}')
        print(f'\t  {tool.description.split("\n")[0]}')

if __name__ == "__main__":
    asyncio.run(main(model='ministral-3:latest'))
