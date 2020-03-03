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

import os
import codecs


# ------------------------------------------
# FUNCTION reduce_cols
# ------------------------------------------
def reduce_cols(line):
    # 1. We create the output variable
    res = []

    # 2. We populate the list using columns passed in
    for val in cols:                   # iterate through passed in cols
        res.append(line[val])   # add to temp list

    # 3. We return res
    return res


# ------------------------------------------
# FUNCTION find_empty_station
# ------------------------------------------
def find_empty_station(line):
    # 1. We create the output variable
    res = []
    # 2. We populate the list with stations that have no bikes available
    if line[1] == 0:                    # check if there are bikes available
        res.append([line[0], line[1]])  # add to result

    # 3. We return res
    return res


# ------------------------------------------
# FUNCTION check_station
# ------------------------------------------
def check_station_name(line):
    # 1. We create the output variable
    res = False

    # 2. We check if name is in stations list
    for name in station_names:
        if line[0] == name:
            res = True

    # 3. We return res
    return res


# ------------------------------------------
# FUNCTION add_bike
# ------------------------------------------
def add_bike(line):
    # 1. We create the output variable
    res = []

    # 2. We make each entry to be (Station_name, 1)
    res.append(line[0])
    res.append(1)

    # 3. We return res
    return res


# ------------------------------------------
#
# HIGHER ORDER FUNCTIONS
#
# ------------------------------------------

# ------------------------------------------
# FUNCTION my_map
# ------------------------------------------
def my_map(funct, my_list):
    # 1. We create the output variable
    res = []

    # 2. We populate the list with the higher application
    for item in my_list:
        sol = funct(item)
        res.append(sol)

    # 3. We return res
    return res


# ------------------------------------------
# FUNCTION my_filter
# ------------------------------------------
def my_filter(funct, my_list):
    # 1. We create the output variable
    res = []

    # 2. We populate the list with the higher application
    for item in my_list:
        # 2.1. If an item satisfies the function, then it passes the filter
        if funct(item):
            res.append(item)

    # 3. We return res
    return res


# ------------------------------------------
# FUNCTION my_fold
# ------------------------------------------
def my_fold(funct, accum, my_list):
    # 1. We create the output variable
    res = accum

    # 2. We populate the list with the higher application
    for item in my_list:
        res = res + funct(accum, item)

    # 3. We return res
    return res

# ------------------------------------------
#
# LINE PROCESSING
#
# ------------------------------------------


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
        res = ( int(params[0]), params[1], float(params[2]), float(params[3]), params[4], int(params[5]), int(params[6]) )

    # 5. We return res
    return res

# ------------------------------------------
#
# TO DO
#
# ------------------------------------------


# ------------------------------------------
# FUNCTION my_main
# ------------------------------------------
def my_main(my_list, station_names):

    # --------------- STEP 1 ------------------------#

    # 1. Apply the Higher-Order function my_map provided above,
    #    so as to apply "process_line" to all functions

    my_list = my_map(process_line, my_list)  #

    print("\n\n\n\n\n------ STEP 1 ------\n")
    for item in range(50):
        print(my_list[item])

    # --------------- STEP 2 ------------------------#
    # 2. Apply the Higher-Order function my_map again,
    #    now to restrict the tuple previously computed to just the name of the station and the amount of bikes available
    global cols
    cols = [1, 5]
    my_list = my_map(reduce_cols, my_list)  #

    print("\n\n\n\n\n------ STEP 2 ------\n")
    for item in range(50):
        print(my_list[item])

    # --------------- STEP 3 ------------------------#

    # 3. Apply the Higher-Order function my_filter provided above,
    #    now to restrict only the entries which are ran out of bikes

    my_list = my_filter(find_empty_station, my_list)

    print("\n\n\n\n\n------ STEP 3 ------\n")
    for item in range(50):
        print(my_list[item])

    # --------------- STEP 4 ------------------------#

    # 4. Apply the Higher-Order function my_filter again,
    #    now to restrict the entries to the ones of the desired stations

    my_list = my_filter(check_station_name, my_list)

    print("\n\n\n\n\n------ STEP 4 ------\n")
    for item in range(50):
        print(my_list[item])

    # --------------- STEP 5 ------------------------#

    # 5. Apply the the Higher-Order function my_map again,
    #    now to make each entry to be (Station_name, 1)

    my_list = my_map(add_bike, my_list)

    print("\n\n\n\n\n------ STEP 5 ------\n")
    for item in range(50):
        print(my_list[item])

    # --------------- STEP 6 ------------------------#

    # 6. Apply the the Higher-Order function my_fold provided above,
    #    so as to compute the total amount of ran outs

    res = my_fold(lambda x, y: 1, 0, my_list)

    print("\n\n\n\n\n------ STEP 6 ------\n")
    print(res)

# ---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
# ---------------------------------------------------------------
if __name__ == '__main__':
    global station_names
    # 1. Local or HDFS folders
    input_file_name = "../../my_dataset/bikeMon_20170317.csv"
    output_file_name = "../../my_result/A01 - Part4/result.txt"

    # 2. List of stations we are interested into
    station_names = ["Fitzgerald's Park", "South Main St.", "Lapp's Quay"]

    # 3. We read-in the content from the input file

    # 3.1. We open the file for reading
    my_input_stream = codecs.open(input_file_name, "r", encoding='utf-8')

    # 3.2. We read-in its content
    file_content = []
    for line in my_input_stream:
        file_content.append(line)

    # 3.3. We close the file
    my_input_stream.close()

    # 4. We call to my_main
    my_main(file_content, station_names)
