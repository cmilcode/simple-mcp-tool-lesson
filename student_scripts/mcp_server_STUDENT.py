# This is the student answer file for this lesson. Only add code between the two designated comments.
# The student code portion starts on line 47.
# This file can also be used as basic boilerplate, I laid out the comments to be very detailed.
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


##########
########## STUDENT CODE STARTS HERE
##########

# Your code goes here.
# You should implement an MCP tool that executes the connectivity_tester.sh script in the tools directory.
# It takes one argument, which is a number in string format that represents how many ICMP pings to do.
# Unless told otherwise by the user, the LLM should execute the script with 3 ICMP pings.
#   Example: connectivity_tester.sh 3

##########
########## STUDENT CODE ENDS HERE
##########


# Main block for compatability. See reference above for more info.
if __name__ == "__main__":
    mcp.run(transport='http', port=8050)
