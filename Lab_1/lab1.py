import codecs

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

# ------------------------------------------
# FUNCTION parse_in
# ------------------------------------------


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

    search_area = []

    # create 8 points around position to be used for searching for mines
    # Points_pos Ord: Tp left,   Tp C,    Tp right,   left,     right,   btm left,   btm C,    tb right
    x, y = 0, 0
    points_pos = [ [x-1, y+1], [x, x+1], [x+1, y+1], [x-1, y], [x+1, y], [x-1, y-1], [x, y-1], [x+1, y-1]]

    print(f"Points positions:  {points_pos}")
    print(f"Top Left:  {points_pos[0]}")

    result = {}
    result["Filled"] = []
    x = -1
    # iterate through each data point in the map
    for index, row in enumerate(my_data["Matrix"]):
        print(f"index : {index}")
        print(f"row : {row}")
        x += 1
        y = 0  # reset y value for each row
        for val in row:
            if val == 'o':  # check point is not a mine

                print(f"Value : {val}")
                print(f" (x, y )  : ({x}, {y})")

                y += 1  # increment y


    # result["Filled"].append(filledRow)

    #print(f"Solved Result: {result}")

    return result


# ------------------------------------------
# FUNCTION parse_out
# ------------------------------------------
def parse_out(output_name, my_solution):
    pass


# ------------------------------------------
# FUNCTION my_main
# ------------------------------------------
def my_main(input_name, output_name):
    # 1. We do the parseIn from the input file
    my_data = parse_in(input_name)
    print(f"Data: {my_data}")

    # 2. We do the strategy to solve the problem
    my_solution = solve(my_data)

    # 3. We do the parse out to the output file
   #parse_out(output_name, my_solution)


# ---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
# ---------------------------------------------------------------
if __name__ == '__main__':
    # 1. Name of input and output files
    input_name = "input_1.txt"
    output_name = "output.txt"

    # 2. Main function
    my_main(input_name, output_name)
