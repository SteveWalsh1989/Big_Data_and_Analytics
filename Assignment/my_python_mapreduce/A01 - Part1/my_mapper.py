#!/usr/bin/python

# --------------------------------------------------------
#           PYTHON PROGRAM
# Here is where we are going to define our set of...
# - Imports
# - Global Variables
# - Functions
# ...to achieve the functionality required.
# When executing > python 'this_file'.py in a terminal,
# the Pythozoon interpreter will load our program,
# but it will execute nothing yet.
# --------------------------------------------------------

import sys
import codecs

# ------------------------------------------
# FUNCTION process_line
# ------------------------------------------
def process_line(line):
    # 1. We create the output variable
    res = ()

    # 2. We remove the end of line character
    line = line.replace("\n", "")

    # 3. We split the line by tabulator characters
    params = line.split(";")

    # 4. We assign res
    if len(params) == 7:
        res = tuple(params)

    # 5. We return res
    return res


# ------------------------------------------
# FUNCTION my_map
#
# ------------------------------------------
def my_map(my_input_stream, my_output_stream, my_mapper_input_parameters):
    # create output variable dict
    res = {}
    # Loop over input file
    for line in my_input_stream:
        location = line.split(";")                   # split rows into column |  0-status, 1-name, 2-lat, 3-long, 4-date, 5-bikes avail, 6-docks avail
        # print(f"Testing: status: {location[0]} -- bikes: {location[5]} ")
        if int(location[0]) == 0 and int(location[5]) == 0:    # check if station ran out of bikes
            # print(f"Testing:{location[1]} - bikes: {location[5]}")
            if location[1] in res:                   # check if location already added
                res[location[1]] += 1                # increment number of times there are no bikes at the station
            else:
                res[location[1]] = 1                 # initialise station in result list and set value to one

    # write results to result file
    for key in res:                                  # res - format each key in dict
        format = key + " - " + str(res[key]) + "\n"
        my_output_stream.write(format)               # write output to output file line by line



# ------------------------------------------
# FUNCTION my_main
# ------------------------------------------
def my_main(local_False_Cloudera_True,
            my_mapper_input_parameters,
            input_file_example,
            output_file_example
           ):

    # 1. We select the input and output streams based on our working mode
    my_input_stream = None
    my_output_stream = None

    # 1.1: Local Mode --> We use the debug files
    if local_False_Cloudera_True == False:
        my_input_stream = codecs.open(input_file_example, "r", encoding='utf-8')
        my_output_stream = codecs.open(output_file_example, "w", encoding='utf-8')

    # 1.2: Cloudera --> We use the stdin and stdout streams
    else:
        my_input_stream = sys.stdin
        my_output_stream = sys.stdout

    # 2. We trigger my_map
    my_map(my_input_stream, my_output_stream, my_mapper_input_parameters)


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
    input_file_example = "../../my_dataset/bikeMon_20170201.csv"
    output_file_example = "../../my_result/A01 - Part1/my_mapper_results.txt"

    # 3. my_mappper.py input parameters
    # We list the parameters here

    # We create a list with them all
    my_mapper_input_parameters = []

    # 4. We call to my_main
    my_main(local_False_Cloudera_True,
            my_mapper_input_parameters,
            input_file_example,
            output_file_example
           )
