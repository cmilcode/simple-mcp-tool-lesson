#!/bin/bash
#
# This is a simple script that pings Google's DNS n number of times.
#
# This script exists to be implemented in the "Simple MCP Tool Lesson"
# https://github.com/cmilcode/simple-mcp-tool-lesson
#
# This script is complete as is, and only LOGFILE should be changed. It logs execution to LOGFILE to see how
# the agent executed the tool.

TIMESTAMP_FORMAT="%Y%m%d-%H:%M:%S"
LOGFILE="/home/mcp/lesson/tools/mcp_tool_execution.log"

echo $(date +$TIMESTAMP_FORMAT) -- Connectivity Tool Executed >> $LOGFILE

if [[ $1 == "" ]]; then
	ping 8.8.8.8 -c 1
	echo $(date +$TIMESTAMP_FORMAT) --- Tool Execution Incorrect, No Argument Provided >> $LOGFILE
	exit 1
else
	GIVEN_ARGUMENT=$(($1))
fi

if (( $GIVEN_ARGUMENT == 3 )); then
	ping 8.8.8.8 -c 3
	echo $(date +$TIMESTAMP_FORMAT) --- Tool Execution Implemented Correctly, ping 8.8.8.8 -c 3 >> $LOGFILE
	exit
elif (( $GIVEN_ARGUMENT > 3)); then
	ping 8.8.8.8 -c 5
	echo $(date +$TIMESTAMP_FORMAT) --- Tool Execution Incorrect, High Count, Attempted To Ping $1 Times >> $LOGFILE
	exit 1
elif (( $GIVEN_ARGUMENT < 3)); then
	ping 8.8.8.8 -c 1
	echo $(date +$TIMESTAMP_FORMAT) --- Tool Execution Incorrect, Low Count,  Attempted To Ping $1 Times >> $LOGFILE
	exit 1
else
	echo $(date +$TIMESTAMP_FORMAT) --- Unknown Execution Error >> $LOGFILE
	exit 1
fi


