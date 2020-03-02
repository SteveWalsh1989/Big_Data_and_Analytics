#!/usr/bin/python

# --------------------------------------------------------
#           PYTHON PROGRAM
# Here is where we are going to define our set of...
# - Imports
# - Global Variables
# - Functions
# ...to achieve the functionality required.
# When executing > python 'this_file'.py in a terminal,
# the Python interpreter will load our program,
# but it will execute nothing yet.
# --------------------------------------------------------

import sys
import codecs


#---------------------------------------
#  FUNCTION get_key_value
#---------------------------------------
def get_key_value(line):
    # 1. We create the output variable
    res = ()

    # 2. We remove the end of line char
    line = line.replace('\n', '')

    # 3. We get the key and value
    words = line.split('\t')
    station = words[0]
    value = words[1]

    # 4. We process the value
    value = value.rstrip(')')
    value = value.strip('(')
    num_ran_outs = int(value)

    # 4. We assign res
    res = (station, num_ran_outs)

    # 5. We return res
    return res


# ------------------------------------------
# FUNCTION my_reduce
#
# TODO; we will also be changing stuff here
#
# 1. read line by line
# word either can be the same as the last word or a new word
#   if the same -->  same station --> add amount to current station
#   if different -->  new station --> print amount for current station + set up count for new station with its amount
#
# for the last line in the file then -> as there is no previous that you can check, you just print the last one so need to account for this
#k
# ------------------------------------------
def my_reduce(my_input_stream, my_output_stream, my_reducer_input_parameters):
    station = ""
    times_empty = 0

    for line in my_input_stream:                    # iterate through input
        location = line.split("\t")                 # split station name and bike avail value
        if station == "":                           # check for initial station
            station = location[0]                   # set station name
        # print(f"my_reduce: line - {line}")
        if len(location) > 1:                       # ignore blank lines
            location[1] = location[1].rstrip()      # remove newline char
            if location[0] == station:              # if station hasn't changed
                times_empty = times_empty + int(location[1])     # increment number of times without bike by station value
            else:                                   # if new station
                format = station + " - " + str(times_empty) + "\n"    # format results
                my_output_stream.write(format)      # write result to output file
                station = location[0]               # reset values for new station
                times_empty = int(location[1].rstrip())
        # print(f"my_map: mapping complete")

# ------------------------------------------
# FUNCTION my_main
# ------------------------------------------
def my_main(local_False_Cloudera_True,
            my_reducer_input_parameters,
            input_file_example,
            output_file_example
           ):

    # 1. We select the input and output streams based on our working mode
    my_input_stream = None
    my_output_stream = None

    # 1.1: Local Mode --> We use the debug files
    if (local_False_Cloudera_True == False):
        my_input_stream = codecs.open(input_file_example, "r", encoding='utf-8')
        my_output_stream = codecs.open(output_file_example, "w", encoding='utf-8')

    # 1.2: Cloudera --> We use the stdin and stdout streams
    else:
        my_input_stream = sys.stdin
        my_output_stream = sys.stdout

    # 2. We trigger my_reducer
    my_reduce(my_input_stream, my_output_stream, my_reducer_input_parameters)

# ---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
# ---------------------------------------------------------------
if __name__ == '__main__':
    # 1. Local Mode or Cloudera
    local_False_Cloudera_True = False

    # 2. Debug Names
    input_file_example = "../../my_result/A01 - Part1/my_sort_results.txt"
    output_file_example = "../my_result/A01 - Part1/my_reducer_results.txt"

    # 3. my_reducer.py input parameters
    # We list the parameters here

    # We create a list with them all
    my_reducer_input_parameters = []

    # 4. We call to my_main
    my_main(local_False_Cloudera_True,
            my_reducer_input_parameters,
            input_file_example,
            output_file_example
           )
