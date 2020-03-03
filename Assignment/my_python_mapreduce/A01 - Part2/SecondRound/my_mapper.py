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
from datetime import datetime

import calendar
import datetime

# ------------------------------------------
# FUNCTION get_day_of_week
# ------------------------------------------
# Examples: get_day_of_week("06-02-2017") --> "Monday"
#           get_day_of_week("07-02-2017") --> "Tuesday"


weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']  # store weekdays

def get_day_of_week(date):
    # 1. We create the output variable
    res = calendar.day_name[(datetime.datetime.strptime(date, "%d-%m-%Y")).weekday()]

    # 2. We return res
    return res

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
    if (len(params) == 7):
        res = tuple(params)

    # 5. We return res
    return res


# ------------------------------------------
# FUNCTION my_map
# ------------------------------------------
def my_map(my_input_stream, my_output_stream, my_mapper_input_parameters):
    count = 0  # number times ran out of bikes
    hour = 0   # current hour that we're checking
    for line in my_input_stream:  # Loop over input file
        location = line.split(";")  # split location row into columns as elements in list
        if location[1] == my_mapper_input_parameters[0] and int(location[0]) == 0 and int(location[5]) == 0:  # checks station name, status and that there are no bikes left
            date = datetime.datetime.strptime(location[4], '%d-%m-%Y %H:%M:%S')  # convert string to date time object

            if hour == 0:          # if this is the first record being read
                hour = date.hour   # initialise hour

            if hour == date.hour:  # If current line is the same hour as previously read
                count += 1         # increment count
            else:                  # If current line is for a new hour
                # print current day and hour counts to output
                format = weekdays[date.weekday()] + "_"+ str(hour) + "\t(" + str(count) + ")\n"  # format output
                my_output_stream.write(format)  # write output
                hour = date.hour   # set hour to the new hour value


# ------------------------------------------
# FUNCTION my_main
# ------------------------------------------
def my_main(local_False_Cloudera_True, my_mapper_input_parameters, input_file_example, output_file_example):

    # 1. We select the input and output streams based on our working mode
    my_input_stream = None
    my_output_stream = None

    # 1.1: Local Mode --> We use the debug files
    if not local_False_Cloudera_True:
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
    input_file_example = "../../../my_dataset/bikeMon_20170204.csv"
    output_file_example = "../../../my_result/A01 - Part2/SecondRound/my_mapper_results.txt"

    # 3. my_mappper.py input parameters
    # We list the parameters here
    station_name = "Fitzgerald's Park"

    # We create a list with them all
    my_mapper_input_parameters = [station_name]

    # 4. We call to my_main
    my_main(local_False_Cloudera_True,
            my_mapper_input_parameters,
            input_file_example,
            output_file_example
           )
