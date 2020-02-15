import numpy as np
import multiprocessing


# ------------------------------------------
# FUNCTION solve
# ------------------------------------------
def solve(my_data, num_cores):
    """Searches Matrix for mines around each point in data[map] and changes value to number mines found"""
    y = -1  # initialise column
    # iterate through each row

    if num_cores == 1:    # Run sequentially
        for index, row in enumerate(my_data["Matrix"]):
            # print(f"Number cores: {num_cores}")
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
    else:  # Run in parallel using number of cores requested
        num_rows = 0
        # Get number of rows
        for index, _ in enumerate(my_data["Matrix"]):
            num_rows += 1

        print(f"Number cores: {num_cores}")
        print(f"Number rows: {num_rows}")
        if num_rows % num_cores != 0:
            print(f"Invalid Core Count provided:")
            exit()

        # Stage 1: Divide - break up number rows by num cores in
        rows_slice = my_divide_stage(my_data, num_cores, num_rows)

        # Stage 2: Map - We setup the object for enabling parallel computation among the different cores
        res = my_map_stage(rows_slice)

        # Stage 3: reduce - combine results into final solution set
        solution = my_reduce_stage(res)

    return solution


# --------------------------------------------------
# my_divide_stage
# --------------------------------------------------
def my_divide_stage(data, num_cores, num_rows):
    """ Divides the data using number of rows  in data divided by
    number of cores provided to return a nested list of datapoints

    returns: slice with array of row indexes per chunk and full dataset
    """
    index_list = range(num_rows)  # create list containing indexes for each row
    index_list_chunks = np.array_split(index_list, num_cores)  # Get row index chunks for each core
    # print(f"index_list_chunks: {index_list_chunks}")
    # print(f"res : {res}")

    res = [slice(chunk, data) for chunk in index_list_chunks]
    return res


# --------------------------------------------------
# my_map_stage
# --------------------------------------------------
def my_map_stage(data_slice):
    # 1. We create the output variable
    res = []

    # 2. We setup the object for enabling parallel computation among the different cores
    pool = multiprocessing.Pool()

    # 3. We use pool to trigger the parallel execution of each people subset (slice) in a different process
    res = pool.map(core_workload, data_slice)
    # print(f"res: {res}")

    # 4. We return res
    return res


# --------------------------------------------------
# my_reduce_stage
# --------------------------------------------------
def my_reduce_stage(results_slice):
    # 1. We create the output variable
    res = {}
    # 2. loop over each chunk in results slice
    for chunk in results_slice:
        # print(f"chunk-- {chunk}")

        res["NumRows"] = chunk["NumColumns"]  # messed up naming before this
        # 3. loop over array index list
        for index in chunk["index_list"]:
            # 4. Add data found in Matrix at array index to results
            res[index] = chunk["Matrix"][index]
    # print(f"testing numrows-- {res['NumRows']}")
    return res


def count_mines(x, y, search_points, data):
    """ Uses the search points to check for mines around a specific (x,y) point"""

    # 1. Points_pos :  Top Left  Top Center   Top Right   ->    [0]  [1]  [2]
    #                      Left                 Right     ->    [3]       [4]
    #                  Btm Left  Btm Center   Btm Right   ->    [5]  [6]  [7]
    points_pos = [[x - 1, y - 1], [x, y - 1], [x + 1, y - 1], [x - 1, y], [x + 1, y], [x - 1, y + 1], [x, y + 1],
                  [x + 1, y + 1]]
    count = 0

    # 2. search each point passed in
    for point in search_points:
        # 3. check for mine
        if data["Matrix"][points_pos[point][1]][points_pos[point][0]] == 'x':
            # 4. increase bomb counter for search point if found
            count += 1
    # 5. return results
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


def core_workload(my_data_slice):
    # print(f"\n\nmy_data_slice:  {my_data_slice}")
    index_list = my_data_slice.start
    my_data = my_data_slice.stop
    my_data["index_list"] = index_list
    # Testing by printing core name
    core =""
    if 0 in index_list:
        core = "Core 1: "
    else:
        core = "Core 2: "
    # print(f"{core}index_list: {index_list}")
    # print(f"{core}my_data: {my_data}")

    for index, row in enumerate(index_list):
        y = row
        x = 0  # reset x value for each row

        # iterate through each column in row
        for val in my_data['Matrix'][row]:
            if val == 'o':  # check point is not a mine
                # print(f"{core} (x, y): {x}, {y}")

                search_points = get_search_points(x, y, my_data['NumRows'] - 1, my_data['NumColumns'] - 1)
                num_mines = count_mines(x, y, search_points, my_data)
                val = str(num_mines)
                my_data["Matrix"][y][x] = val
            x += 1  # increment

    # print(f"\n{core}Result data: {my_data}")
    return my_data
