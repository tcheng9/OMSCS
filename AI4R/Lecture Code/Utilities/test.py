######################################################################
# This file copyright the Georgia Institute of Technology
#
# Permission is given to students to use or modify this file (only)
# to work on their assignments.
#
# You may NOT publish this file or make it available to others not in
# the course.
#
######################################################################

import copy

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def adjacent_cells(grid,row,col):
    yMax = len(grid)-1
    xMax = len(grid[0])-1
    
    ret = []
    
    if row-1 >= 0 and grid[row-1][col] != 1:
        ret.append((row-1,col))
    if row+1 <= yMax and grid[row+1][col] != 1:
        ret.append((row+1,col))
    if col-1 >= 0 and grid[row][col-1] != 1:
        ret.append((row,col-1))
    if col+1 <= xMax and grid[row][col+1] != 1:
        ret.append((row,col+1))
        
    return ret

def compute_value(grid,init):
    yMax = len(grid)-1
    xMax = len(grid[0])-1
    
    indices = [ (row,col) for row in range(yMax+1) for col in range(xMax+1) ]
    G = { index : {'d':-1} for index in indices }

    first_cell = (init[0],init[1])
    
    G[first_cell]['d'] = 0
    to_check = { first_cell : G[first_cell] }
    current_cell = first_cell

    while len(to_check) > 0:
        G[current_cell] = to_check.pop(current_cell)
        for cell in adjacent_cells(grid, *current_cell):
            if G[cell]['d'] != -1:  # means cell has already been checked
                continue
            if cell in to_check:  # don't add the cell again
                continue
            to_check[cell] = G[cell]
            G[cell]['d'] = G[current_cell]['d'] + 1
        if len(to_check) > 0:
            current_cell = min( to_check.keys(), key=lambda k: to_check[k]['d'] )

    return [ [ G[(row,col)]['d'] for col in range(xMax+1) ] for row in range (yMax+1) ]


def is_valid_answer(grid,init,user_answer):
    # check for correct length
    if len(grid) != len(user_answer):
        return False
    for i in range(len(grid)):
        if len(grid[i]) != len(user_answer[i]):
            return False
    height = len(grid)
    width = len(grid[0])
    
    # unreachable cells have value -1
    value_grid = compute_value(grid, init)
    
    # check that unreachable cells are marked with -1
    reachable_cells = 0
    for i in range(height):
        for j in range(width):
            if value_grid[i][j] == -1 and user_answer[i][j] != -1:
                return False
            elif value_grid[i][j] >= 0:
                reachable_cells += 1
    
    # check that every number from 0 to reachable_cells-1 is in user_answer
    present = [0]*reachable_cells
    for i in range(height):
        for j in range(width):
            if user_answer[i][j] < 0:
                continue
            else:
                present[user_answer[i][j]] = 1
    if sum(present) != reachable_cells:
        return False
    
    # check that the numbers occur in a legal pattern
    # (the expansion number of a cell should be at least the number of steps
    # away from init it takes to get to the cell)
    for i in range(height):
        for j in range(width):
            if user_answer[i][j] < 0:
                continue
            elif user_answer[i][j] < value_grid[i][j]:
                return False
    
    return True


def test_1(student_func):
    try:
        search = student_func
    except:
        # TODO put in a more relevant message
        return 2  # You didn't define a function called search
    try:
        grid = [[0, 1],
                [0, 0]]
        init = [0, 0]
        goal = [len(grid) - 1, len(grid[0]) - 1]
        cost = 1

        user_answer = search(grid, init, goal, cost)
        if not user_answer:
            return 3  # didn't return anything
    except:
        return 103  # Problem.

    try:
        grid = [[0, 0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 1, 0],
                [0, 0, 1, 1, 1, 0],
                [0, 0, 0, 0, 1, 0]]
        init = [0, 0]
        goal = [len(grid) - 1, len(grid[0]) - 1]
        cost = 1

        user_answer = search(grid, init, goal, cost)
        if user_answer != [11, 4, 5]:
            return 4  # Your code didn't work for example in lecture
    except:
        return 104

    try:
        grid = [[0, 1, 0, 0, 0, 0],
                [0, 1, 0, 1, 0, 0],
                [0, 1, 0, 1, 0, 0],
                [0, 1, 0, 1, 0, 0],
                [0, 0, 0, 1, 0, 0]]
        init = [0, 0]
        goal = [len(grid) - 1, len(grid[0]) - 1]
        cost = 1
        user_answer = search(grid, init, goal, cost)
        if user_answer != [17, 4, 5]:
            return 5
    except:
        return 105

    try:
        grid = [[0, 1, 0, 1, 0, 0, 0],
                [0, 1, 0, 1, 0, 0, 0],
                [0, 1, 0, 1, 0, 0, 0],
                [0, 1, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0]]
        init = [0, 0]
        goal = [len(grid) - 1, len(grid[0]) - 1]
        cost = 1
        user_answer = search(grid, init, goal, cost)
        if type(user_answer) != str or user_answer.lower() != 'fail':
            return 6  # Your code didn't return 'fail' when it should have.
    except:
        return 106

    return 0  # correct


def test_2(student_func):
    
    try:
        search = student_func
    except:
        return 2 #You didn't define a function called search
    
    try:
        grid = [[0, 1],
                [0, 0]]
        init = [0,0]
        goal = [len(grid)-1,len(grid[0])-1]
        cost = 1
        
        user_answer = search(grid,init,goal,cost)
        if not user_answer:
            return 3 # Your function didn't return anything.
    except:
        return 103 # problem
    
    try:
        grid = [[0, 1, 1, 1, 1],
                [0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0],
                [1, 1, 1, 1, 0],
                [0, 0, 0, 1, 0]]
        init = [0,0]
        goal = [len(grid)-1,len(grid[0])-1]
        cost = 1
        
        G = copy.deepcopy(grid)
        
        user_answer = search(G,init,goal,cost)
        if not is_valid_answer(grid,init,user_answer[1]):
            return 4 # Your code didn't work for example in lecture
    except:
        return 104
    
    try:
        grid = [[0, 1, 0, 0, 0, 1, 0],
                [0, 1, 0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0, 1, 1],
                [0, 0, 0, 1, 0, 0, 0]]
        init = [0,0]
        goal = [len(grid)-1,len(grid[0])-1]
        cost = 1
        G = copy.deepcopy(grid)
        
        user_answer = search(G,init,goal,cost)
        if not is_valid_answer(grid,init,user_answer[1]):
            return 5
    except:
        return 105

    try:
        grid = [[0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 1, 0],
                [0, 0, 1, 0, 1, 0],
                [0, 0, 1, 0, 1, 0]]
        init = [0, 0]
        goal = [len(grid)-1, len(grid[0])-1]
        cost = 1
        G = copy.deepcopy(grid)
        
        user_answer = search(G,init,goal,cost)
        if not is_valid_answer(grid,init,user_answer[1]):
            return 6
    except:
        return 106
    
    return 0


def run_grader_1(student_func):
    grade_result = dict()

    # test grids

    grid_1 = [[0, 1],
              [0, 0]]

    grid_2 = [[0, 0, 1, 0, 0, 0],
              [0, 0, 1, 0, 0, 0],
              [0, 0, 0, 0, 1, 0],
              [0, 0, 1, 1, 1, 0],
              [0, 0, 0, 0, 1, 0]]

    grid_3 = [[0, 1, 0, 0, 0, 0],
              [0, 1, 0, 1, 0, 0],
              [0, 1, 0, 1, 0, 0],
              [0, 1, 0, 1, 0, 0],
              [0, 0, 0, 1, 0, 0]]

    grid_4 = [[0, 1, 0, 1, 0, 0, 0],
              [0, 1, 0, 1, 0, 0, 0],
              [0, 1, 0, 1, 0, 0, 0],
              [0, 1, 0, 1, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 0]]
    try:
        result = test_1(student_func)
        comment = ""
        if result == 0:
            comment = ""
        elif result == 1:
            comment = "There was an error running your solution. Please make sure there are no syntax errors, \nindentation errors, etc. and try again."
        elif result == 2:
            comment = "search is not defined"
        elif result == 2.5:
            comment = "search did not return a list of three integers or the string 'fail'"
        elif result % 100 == 3:
            if result == 3:
                comment = f"search did not return anything for grid: {grid_1}"
            else:
                comment = f"search raised an exception for grid: {grid_1}"
        elif result % 100 == 4:
            if result == 4:
                comment = f"search didn't return the expected output for grid: {grid_2}"
            else:
                comment = f"search raised an exception for grid: {grid_2}"

        elif result % 100 == 5:
            if result == 5:
                comment = f"search didn't return the expected output for grid: {grid_3}"
            else:
                comment = f"search raised an exception for grid: {grid_3}"

        elif result % 100 == 6:
            if result == 6:
                comment = f"search didn't return the expected output for grid: {grid_4}"
            else:
                comment = f"search raised an exception for grid: {grid_4}"

        grade_result['correct'] = (result == 0)
        if grade_result['correct']:
            grade_result['comment'] = "Correct! " + comment
        else:
            grade_result['comment'] = comment
    except:
        grade_result['correct'] = False
        grade_result['comment'] = """There was an error running your solution. Make sure that 
    search takes four arguments: grid, init, goal, cost. Also
    make sure that you are not using any global variables other
    than delta and delta_name."""

    return grade_result.get('comment')


def run_grader_2(student_func):
    grade_result = dict()
    try:
        result = test_2(student_func)
        correct = result == 0
        comment = ""
        if result == 0:
            comment = ""
        elif result == 1:
            comment = "There was an error running your solution. Please make sure there are no syntax errors, \nindentation errors, etc. and try again."
        elif result == 2:
            comment = "search is not defined"
        elif result == 3:
            comment = "search did not return anything"
        elif result % 100 == 4:
            if result == 4:
                comment = "search didn't return the expected output for:\ngrid = ["
            else:
                comment = "search raised an exception for:\ngrid = ["
            grid = [[0, 1, 1, 1, 1],
                    [0, 1, 0, 0, 0],
                    [0, 0, 0, 1, 0],
                    [1, 1, 1, 1, 0],
                    [0, 0, 0, 1, 0]]
            for i in range(len(grid)):
                comment += str(grid[i])
                if i < len(grid) - 1:
                    comment += ',\n        '
                else:
                    comment += ']'
        elif result % 100 == 5:
            if result == 5:
                comment = "search didn't return the expected output for:\ngrid = ["
            else:
                comment = "search raised an exception for:\ngrid = ["
            grid = [[0, 1, 0, 0, 0, 1, 0],
                    [0, 1, 0, 1, 0, 1, 0],
                    [0, 1, 0, 1, 0, 1, 0],
                    [0, 1, 0, 1, 0, 1, 1],
                    [0, 0, 0, 1, 0, 0, 0]]
            for i in range(len(grid)):
                comment += str(grid[i])
                if i < len(grid) - 1:
                    comment += ',\n        '
                else:
                    comment += ']'
        elif result % 100 == 6:
            if result == 6:
                comment = "search didn't return the expected output for:\ngrid = ["
            else:
                comment = "search raised an exception for:\ngrid = ["
            grid = [[0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 1, 0],
                    [0, 0, 1, 0, 1, 0],
                    [0, 0, 1, 0, 1, 0]]
            for i in range(len(grid)):
                comment += str(grid[i])
                if i < len(grid) - 1:
                    comment += ',\n        '
                else:
                    comment += ']'

        grade_result['correct'] = correct
        if correct:
            grade_result['comment'] = "Correct! " + comment
        else:
            grade_result['comment'] = comment
    except:
        grade_result['correct'] = False
        grade_result['comment'] = """There was an error running your solution. Make sure that 
    search takes four arguments: grid, init, goal, cost. Also
    make sure that you are not using any global variables other
    than delta and delta_name."""

    return grade_result.get('comment')