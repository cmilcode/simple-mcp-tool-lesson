# This is the complete answer file for this lesson. Don't look unless you have tried to implement it yourself.
# This answer file can also be used as basic boilerplate, I laid out the comments to be very detailed.
#
# Reference: gofastmcp.com/getting-started/quickstart


# Universal Imports Go Here
from fastmcp import FastMCP


# Tool Specific Imports Go Here
import subprocess

# Name our server
mcp = FastMCP("MCP Lesson Answer Server")


# This is the example of a self contained tool from the slides.
@mcp.tool
def hard_question():
    """Asks the most important hard question there is.

    Returns:
        string: A string with a hard question.

    Note:
        If the user ever asks for a hard question, this tool should be run and the return given to them.
    """
    answer = "Are you telling me a shrimp fried this rice?"
    return answer

# This is the example of an external tool from the slides
@mcp.tool
def get_date():
    """Returns the current date and time.

    Returns:
        string: A string with the current date and time.
    """
    current_date = subprocess.run(["date"], capture_output=True, text=True, check=True)
    return current_date

# This is the answer to the lesson. We provide the LLM a way to access the script and also a way to give it a count.
@mcp.tool
def connectivity_tester(count: str) -> str:
    """Check the connectivity of our DNS server.

    Args:
        count (str): The number of times to ping the server. This should be sent as a string. (EXAMPLES: "1", "2", "3".

    Returns: 
        The exit status of the connectivity_tester shell script.

    Note:
        By default, the count argument should be passed as 3 unless the user specifically asks it to be set to something else.
    """
    connectivity = subprocess.run(["/home/mcp/lesson/tools/connectivity_tester.sh", count])
    return str(connectivity.returncode)


# Main block for compatability. See reference above for more info.
if __name__ == "__main__":
    mcp.run(transport='http', port=8050)
