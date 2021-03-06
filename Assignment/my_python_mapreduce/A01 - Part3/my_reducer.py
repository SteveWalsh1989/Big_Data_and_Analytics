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
import datetime
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
    day = words[0]
    hour = words[1]

    # 4. We process the value
    hour = hour.rstrip(')')
    hour = hour.strip('(')

    # 4. We assign res
    res = (day, hour)

    # 5. We return res
    return res


# ------------------------------------------
# FUNCTION my_reduce
# ------------------------------------------
def my_reduce(my_input_stream, my_output_stream, my_reducer_input_parameters):
    date = ""    # stores current date
    times = []   # stores list of adjacent time slots where no bikes avail
    for line in my_input_stream:                                                 # Loop over input file
        time_delta = datetime.timedelta(minutes=my_reducer_input_parameters[0])  # set time delta based on input params
        date_time = line.split("\t")                                             # split date into list
        date_time[1] = date_time[1].rstrip().replace("(", "").replace(")", "")   # remove newline and brackets
        date_time_str = date_time[0] + " " + date_time[1]                        # create date time string from input
        current_date = datetime.datetime.strptime(date_time_str, '%d-%m-%Y %H:%M:%S')  # convert date time string to datetime
        if date == "":                  # check if its the first date being inputted
            date = current_date         # initialise date
        if len(times) == 0:
            times.append(current_date)  # add time to list
        else:
            # check its the same day and within 5 minute increment
            dt = times[len(times) - 1] + time_delta
            if date.date() == current_date.date() and current_date.time() == dt.time():
                times.append(dt) # add current time to times[]
            else:
                # format current count and time from start of station being empty to string
                date_str = current_date.date().strftime("%d-%m-%Y")  # extract date as string
                time_str = times[0].strftime("%H:%M:%S")             # extract time as string
                format = date_str + "\t(" + time_str + ", " + str(len(times)) + ")\n"
                my_output_stream.write(format)  # write output
                times = []                      # reset value


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
    input_file_example = "../../my_result/A01 - Part3/2. my_sort_simulation/sort_1.txt"
    output_file_example = "../my_result/A01 - Part3/3. my_reduce_simulation/reduce_sort_1.txt"

    # 3. my_reducer.py input parameters
    # We list the parameters here
    measurement_time = 5

    # We create a list with them all
    my_reducer_input_parameters = [measurement_time]

    # 4. We call to my_main
    my_main(local_False_Cloudera_True,
            my_reducer_input_parameters,
            input_file_example,
            output_file_example
           )
