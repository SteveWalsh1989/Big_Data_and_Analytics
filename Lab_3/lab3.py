from builtins import str, len

import codecs
import algorithm
import numpy as np
# --------------------------------------------------------
#           Mine Sweeper program - Big data style
# --------------------------------------------------------
#
# Basically just converting lab 1 to be able to run either sequentially
# or using multiple cores.
#
# Input The first line contains two integers N and M, 1 ≤ N, M ≤ 1000,
# corresponding to the the height and width of the map respectively.
# The next N lines contain M space-separated characters.
# Each character is either an x if this cell contains a mine,
# or o to represent an empty cell.
#
# Output The output consists of N lines of M space-separated characters. Each
# character either encodes for the number of adjacent cells containing mines,
# or the character ’x’ if the cell itself contains a mine.
#
# EX:
# Sample Input 1     Sample Output 1
# 3 5                   1 x 3 x 3
# o x o x o             1 1 3 x x
# o o o x x             0 0 1 2 2
# o o o o o
#
# --------------------------------------------------------


def generate_file(name, num_rows, num_cols):
    print(f"Generating Data ...")
    print(f"Rows Requested: {num_rows}")
    print(f"Cols Requested: {num_cols}")

    output_name = "input_files/input_" + str(name) + ".txt"
    my_output_stream = codecs.open(output_name, "w", encoding="utf-8")
    header = str(num_rows) + " " + str(num_cols) + "\n"
    my_output_stream.write(header)
    for i in range(0, num_rows):
        map_row = generate_random_row(num_cols)
        my_output_stream.write(map_row)
    my_output_stream.close()
    print(f"Generating Data Complete")

    return name


def generate_random_row(num_cols):
    res = ""
    for i in range(0, num_cols):
        test = np.random.choice(np.arange(0, 2), p=[0.23, 0.77])
        if test == 0:
            letter = "x "
        else:
            letter = "o "
        res += letter
    res += "\n"  # add new line
    return res


def parse_in(file_name):
    """Open and read data from file-name and store data in map."""

    result = {}
    input_stream = open(file_name).readline()
    result["NumColumns"], result["NumRows"] = map(int, input_stream.strip().split())
    input_stream = open(file_name).readlines()
    result["Matrix"] = []

    for line in input_stream:
        line = line.replace('\n', "")   # remove new line
        line = line.strip()             # strip chars
        cells = line.split(" ")         # split each element in lists

        result["Matrix"].append(cells)

    result["Matrix"].pop(0)  # remove num col and rows from data matrix
    return result


# ------------------------------------------
# FUNCTION parse_out
# ------------------------------------------
def parse_out(output_name, my_solution):
    my_output_stream = codecs.open(output_name, "w", encoding="utf-8")
    row = 0
    while row < my_solution['NumRows']:
        line = ""
        for cell in my_solution[row]:
            line = line + str(cell) + " "

        size = len(line)
        if size > 0:
            line = line[0:(size - 1)]

        line = line + "\n"
        my_output_stream.write(line)
        row += 1
    my_output_stream.close()


# ------------------------------------------
# FUNCTION my_main
# ------------------------------------------
def my_main(input_name, output_name, num_cores):
    # 1. We do the parseIn from the input file
    my_data = parse_in(input_name)
    # print(f"Data: {my_data}")

    # 2. We do the strategy to solve the problem
    my_solution = algorithm.solve(my_data, num_cores)
    # print(f"Sol:  {my_solution}")

    # 3. We do the parse out to the output file
    parse_out(output_name, my_solution)


# ---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
# ---------------------------------------------------------------
if __name__ == '__main__':
    # 1. Name of input and output files
    cores = [1, 2, 4, 8]

    file_num = 3  # number of file to test

    # generates a file with inputname, numRows, numColumn
    file_num = generate_file(4, 1000, 1000)

    input_name = "input_files/input_" + str(file_num) + ".txt"
    output_name = "results/output_" + str(file_num) + ".txt"

    for num_cores in cores:
        # 2. Main function
        my_main(input_name, output_name, num_cores)
