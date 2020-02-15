from builtins import str, len

import codecs

# --------------------------------------------------------
#           Mine Sweeper program
# --------------------------------------------------------
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
# FUNCTION solve
# ------------------------------------------
def solve(my_data):
    """Searches Matrix for mines around each point in data[map] and changes value to number mines found"""
    y = -1  # initialise column
    # iterate through each row
    for index, row in enumerate(my_data["Matrix"]):

        y += 1
        x = 0  # reset x value for each row
        # iterate through each column in row
        for val in row:
            if val == 'o':  # check point is not a mine
                search_points = get_search_points(x, y, my_data['NumRows']-1, my_data['NumColumns']-1)
                num_mines = count_mines(x, y, search_points, my_data)
                val = str(num_mines)
                my_data["Matrix"][y][x] = val
            x += 1  # increment y

    return my_data


def count_mines(x, y, search_points, data):
    """ Uses the search points to check for mines around a specific (x,y) point"""

    # Points_pos :  Top Left  Top Center   Top Right   ->    [0]  [1]  [2]
    #                   Left                 Right     ->    [3]       [4]
    #               Btm Left  Btm Center   Btm Right   ->    [5]  [6]  [7]
    points_pos = [[x - 1, y - 1], [x, y - 1], [x + 1, y - 1], [x - 1, y], [x + 1, y], [x - 1, y + 1], [x, y + 1],
                  [x + 1, y + 1]]
    count = 0
    for point in search_points:
        if data["Matrix"][points_pos[point][1]][points_pos[point][0]] == 'x':  # check for mine
            count += 1

    return count


def get_search_points(x, y, last_row, last_cols):
    """ Uses the search points and size of map to determine location of point determine what
        points would need to be checked around it when searching for mines in count_mines()
        Position comes from:  Top Left  Top Center   Top Right   ->    [0]  [1]  [2]
                                  Left                   Right   ->    [3]       [4]
                              Btm Left  Btm Center   Btm Right   ->    [5]  [6]  [7]"""
    # Rules: If Corner
    if x == 0 and y == 0:                              # 1 top left
        points = [4, 6, 7]
    elif x == 0 and y == last_cols:                    # 2 btm left
        points = [1, 2, 4]
    elif x == last_row and y == 0:                     # 3 top right
        points = [3, 5, 6]
    elif x == last_row and y == last_cols:             # 4 btm right
        points = [0, 1, 3]
    # Rule: Sides
    elif x == 0 and y != 0 and y != last_cols:         # 5 left side
        points = [1, 2, 4, 6, 7]
    elif y != 0 and y != last_cols and x == last_row:  # 6 right side
        points = [0, 1, 3, 5, 6]
    elif x != 0 and y == 0 and x != last_row:          # 7 top row
        points = [3, 4, 5, 6, 7]
    elif x != 0 and x != last_row and y == last_cols:  # 8 bottom row
        points = [0, 1, 2, 3, 4]
    # Rule: 9 Else - search all position
    else:
        points = [0, 1, 2, 3, 4, 5, 6, 7]  # Middle

    return points


# ------------------------------------------
# FUNCTION parse_out
# ------------------------------------------
def parse_out(output_name, my_solution):
    my_output_stream = codecs.open(output_name, "w", encoding="utf-8")
    for cell_row in my_solution["Matrix"]:
        line = ""

        for cell in cell_row:
            line = line + str(cell) + " "

        size = len(line)
        if size > 0:
            line = line[0:(size - 1)]

        line = line + "\n"

        my_output_stream.write(line)
    my_output_stream.close()


# ------------------------------------------
# FUNCTION my_main
# ------------------------------------------
def my_main(input_name, output_name):
    # 1. We do the parseIn from the input file
    my_data = parse_in(input_name)
    print(f"Data: {my_data}")

    # 2. We do the strategy to solve the problem
    my_solution = solve(my_data)
    print(f"Sol:  {my_solution}")

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

    file_num = 3  # number of file to test

    input_name = "input_files/input_" + str(file_num) + ".txt"
    output_name = "results/output_" + str(file_num) + ".txt"

    # 2. Main function
    my_main(input_name, output_name)
