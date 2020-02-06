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
    x, y = 0, 0


    # print(f"Points positions:  {points_pos}")
    # print(f"Top Left:  {points_pos[0]}")
    y = -1
    # iterate through each data point in the map
    for index, row in enumerate(my_data["Matrix"]):
        # print(f"index : {index}")
        # print(f"row : {row}")
        y += 1
        x = 0  # reset y value for each row
        for val in row:
           # print(f"row : {row}")
           #  print(f"val : {val}")

            if val == 'o':  # check point is not a mine

                # print(f"Value : {val}")
                #print(f" (x, y )  : ({x}, {y})")
                search_points = get_search_points(x, y, my_data['NumRows']-1, my_data['NumColumns']-1)

                num_mines = count_mines(x, y, search_points, my_data )
                val = str(num_mines)

                # my_data["Matrix"][x][y] = val
            x += 1  # increment y
    # print(f"Solved Result: {my_data}")

    return my_data


def count_mines(x, y, search_points, data):

    # Points_pos Ord:Tp left - 0  Tp C - 1,    Tp right- 2,   left- 3,     right- 4,  btm left 5,    btm C- 6,  btm right- 7
    points_pos = [[x - 1, y - 1], [x, y - 1], [x + 1, y - 1], [x - 1, y], [x + 1, y], [x - 1, y + 1], [x, y + 1],
                  [x + 1, y + 1]]
    count = 0
    vx = x
    vy = y
    # print(f"Search x : {vx}")
    # print(f"Search y : {vy}")
    for point in search_points:
        print(f" Point Pos {point} : {points_pos[point]}    ")

    #     print(f"Search Point : {points_pos[point]}")
    #
        print(f"Search Point X : {points_pos[point][0]}")
        print(f"Search Point y : {points_pos[point][1]}")
        print(f"Value Found: {data['Matrix'][points_pos[point][1]][points_pos[point][0]]}")
        if data["Matrix"][points_pos[point][1]][points_pos[point][0]] == 'x':
            count += 1
            # print(f"count: {count}")
    print(f"Num Mines : {count}")

    return count


def get_search_points(x, y, last_row, last_cols):
    print(f"--------------------------------")
    # print(f" last_row : {last_row}")
    # print(f" last_cols : {last_cols}")

    print(f" Search Points:  (x, y )  : ({x}, {y})")

    # Scenarios: 9: Corners, Sides, else

    # Rules: If Corner
    if x == 0 and y == 0:                  # 1 top left
        print("top Left")
        points = [4, 6, 7]
    elif x == 0 and y == last_cols:         # 2 btm left
        print("btm Left")

        points = [1, 2, 4]
    elif x == last_row and y == 0:         # 3 top right
        print("top right")

        points = [3, 5, 6]
    elif x == last_row and y == last_cols:  # 4 btm right
        points = [0, 1, 3]
        print("btm right")

    # Rule: Sides
    elif x == 0 and y != 0 and y != last_cols:          # 5 left
        points = [1, 2, 4, 6, 7]
        print("left")

    elif y != 0 and y != last_cols and x == last_row:  # 6 right
        points = [0, 1, 3, 5, 6]
        print("right")

    elif x != 0 and y == 0 and x != last_row:         # 7 top
        points = [3, 4, 5, 6, 7]
        print("top")

    elif x != 0 and x != last_row and y == last_cols:    # 8 bottom
        points = [0, 1, 2, 3, 4]
        print("bottom")

    # Rule: 9 Else - search all position
    else:
        print("mid")

        points = [0, 1, 2, 3, 4, 5, 6, 7]  # all positions

    return points


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
    print(f"My solution: {my_solution}")

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
