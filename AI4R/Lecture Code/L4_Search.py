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

from Utilities import test

# SEARCH LESSON MODULES
print("SEARCH LESSON MODULES", end="")

# --------------------------------------------------------------------
# 9. FIRST SEARCH PROGRAM
print("\n9. FIRST SEARCH PROGRAM")
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
#
#  Comment out any print statements used for debugging.

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


def search(grid, init, goal, cost):
    path = None
    # TODO: ADD CODE HERE

    ##Question: what is closed list?
    closed_list = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    closed_list[init[0]][init[1]] = 1
    # start_row, start_col = init[0], init[1]
    # start = closed_list[start_row][start_col]

    #Initial values and g = order cell is touched in
    x = init[0]
    y = init[0]
    g = 0


    open_list = [[g,x,y]] #I think this is a tracker

    found = False #Flag if goal is found -> SUCCESS return value
    resign = False  #flag is goal is not found -> FAILURE return value


    ##UCS algo

    while found is False and resign is False:
        #Check if we still have elements on the open list to search
        #open list is the queue data structure for BFS
        if len(open_list) ==0:
            #Condition for no matches found at all -> search has run out of nodes to check
            resign = True
            path = 'fail'
            # print(path)
        else:
            #Weird way to figure out min g to check
            open_list.sort() #Sort list, smallest to largest
            open_list.reverse() #Reverse it so it is largest to smallest
            next_node = open_list.pop() #Pop last value which is the smallest value

            #get next smallest g node to check
            x = next_node[1]
            y = next_node[2]
            g = next_node[0]

            #Check if we hit the goal
            if x == goal[0] and y == goal[1]:
                #Goal found, return output
                found = True
                path = next_node
                # print(path) ##this is the return output of the final node

            else:
                #Goal not found, keep looking
                for i in range(len(delta)):
                    #Check all 4 cardinal
                    x2 = x + delta[i][0] #delta[i] returns a tuple (x_direction, y_direction) then you get [0] for x
                    y2 = y + delta[i][1] #delta[i] returns a tuple (x_direction, y_direction) then you get [1] for y

                    if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                        #Check if new position (x2, y2) is in bounds AND a valid position (not a wall or something)
                        if closed_list[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open_list.append([g2, x2, y2])
                            closed_list[x2][y2] = 1



    return path

##Test code for Q9
# print(search(grid, init, goal, cost))
#
# print("EXTRA TEST CASES (1):")
# try:
#     response = test.run_grader_1(search)
#     print(response)
# except Exception as err:
#     print(str(err))

# --------------------------------------------------------------------
# 10. EXPANSION GRID
print("\n10. EXPANSION GRID")
# Modify the function search so that it returns
# a table of values called expand. This table
# will keep track of which step each node was
# expanded.
#
# Make sure that the initial cell in the grid
# you return has the value 0.
#
#  Comment out any print statements used for debugging.

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


def search(grid, init, goal, cost):
    path = None
    expand = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
    # TODO: ADD CODE HERE

    ##Question: what is closed list?
    closed_list = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    closed_list[init[0]][init[1]] = 1
    # start_row, start_col = init[0], init[1]
    # start = closed_list[start_row][start_col]

    #Initial values and g = order cell is touched in
    x = init[0]
    y = init[0]
    g = 0
    counter = 0

    open_list = [[g,x,y]] #I think this is a tracker

    found = False #Flag if goal is found -> SUCCESS return value
    resign = False  #flag is goal is not found -> FAILURE return value


    ##UCS algo

    while found is False and resign is False:
        #Check if we still have elements on the open list to search
        #open list is the queue data structure for BFS
        if len(open_list) ==0:
            #Condition for no matches found at all -> search has run out of nodes to check
            resign = True
            path = 'fail'
            # print(path)
        else:
            #Weird way to figure out min g to check
            open_list.sort() #Sort list, smallest to largest
            open_list.reverse() #Reverse it so it is largest to smallest
            next_node = open_list.pop() #Pop last value which is the smallest value

            #get next smallest g node to check
            x = next_node[1]
            y = next_node[2]
            g = next_node[0]

            #Check if we hit the goal
            if x == goal[0] and y == goal[1]:
                #Goal found, return output
                found = True
                path = next_node
                # print(path) ##this is the return output of the final node

            else:
                #Goal not found, keep looking
                for i in range(len(delta)):
                    #Check all 4 cardinal
                    x2 = x + delta[i][0] #delta[i] returns a tuple (x_direction, y_direction) then you get [0] for x
                    y2 = y + delta[i][1] #delta[i] returns a tuple (x_direction, y_direction) then you get [1] for y

                    if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                        #Check if new position (x2, y2) is in bounds AND a valid position (not a wall or something)
                        if closed_list[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open_list.append([g2, x2, y2])
                            closed_list[x2][y2] = 1
                            expand[x2][y2] = counter
                            counter += 1




    return path, expand

########print functions for Q10
path, expand = search(grid, init, goal, cost)
print('Path:', path)
print('Expand:')
for i in range(len(expand)):
    print(expand[i])


print("EXTRA TEST CASES (2):")
try:
    response = test.run_grader_2(search)
    print(response)
except Exception as err:
    print(str(err))

# --------------------------------------------------------------------
# 11. PRINT PATH
print("\n11. PRINT PATH")
# Modify the the search function so that it returns
# a shortest path as follows:
#
# [['>', 'v', ' ', ' ', ' ', ' '],
#  [' ', '>', '>', '>', '>', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', '*']]
#
# Where '>', '<', '^', and 'v' refer to right, left,
# up, and down motions. Note that the 'v' should be
# lowercase. '*' should mark the goal cell.
#
# You may assume that all test cases for this function
# will have a path from init to goal.

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


def search(grid, init, goal, cost):
    # Copy and paste your solution code from the previous exercise (#10)
    # TODO: CHANGE/UPDATE CODE
    path = None
    expand = []
    policy = []

    return path, expand, policy


path, expand, policy = search(grid, init, goal, cost)
for i in range(len(policy)):
    print(policy[i])

# --------------------------------------------------------------------
# 13. IMPLEMENT A*
print("\n13. IMPLEMENT A*")
# Modify the the search function so that it becomes
# an A* search algorithm as defined in the previous
# lectures.
#
# Your function should return the expanded grid
# which shows, for each element, the count when
# it was expanded or -1 if the element was never expanded.
#
# If there is no path from init to goal,
# the function should return the string 'fail'

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
heuristic = [[9, 8, 7, 6, 5, 4],
             [8, 7, 6, 5, 4, 3],
             [7, 6, 5, 4, 3, 2],
             [6, 5, 4, 3, 2, 1],
             [5, 4, 3, 2, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]

cost = 1

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


def search(grid, init, goal, cost, heuristic):
    # Copy and paste your solution code from the previous exercise (#11)
    # TODO: CHANGE/UPDATE CODE
    path = None
    # expand = []
    # policy = []



    closed_list = [[0 for col in range(len(grid[0]))] for i in range(len(grid))]
    closed_list[init[0]][init[1]] = 1
    expand = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
    policy = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]


    x = init[0]
    y = init[1]
    g = 0
    h = heuristic[x][y]
    f = g +h
    open_list = [[f, g, h, x, y]] #pop lowest F value instead of G

    found = False
    resign = False
    count = 0

    while found is False and resign is False:
        # print(len(open_list))
        if len(open_list) == 0:
            #No possible solution
            resign = True
            path = 'fail'
            print(path)

        else:
            #Pop node from list and search that (adjacent) node
            '''
            next 3 lines are a way to find lowest F value cost node
            '''
            open_list.sort()
            open_list.reverse()
            next_node = open_list.pop()

            ##Pulling values from the next_node (which is the next node with lowest F cost)
            x = next_node[3]
            y = next_node[4]
            g = next_node[1]

            #Add count to grid and update counte

            expand[x][y] = count
            count += 1

            #check if we are done
            if x == goal[0] and y == goal[1]:
                found = True
                '''
                Is next Node the entire path??
                '''

                path = next_node
                print(path)

            else:
                #expand winning leement and add it to next open list
                #->  essentially, search adjacent coordinates of lowest node
                for i in range(len(delta)):
                    x2 = x +  delta[i][0]
                    y2 = y + delta[i][1]

                    if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                        if closed_list[x2][y2] ==0 and grid[x2][y2] == 0:
                            '''
                            "grid[x2][y2]" == 0 => means if that cell is traversable but we haven't traversed it yet
                            '''
                            '''
                            Question: Where do you get the cost value?
                            ANSWER: outside this function, in this problem, it's cost == 1 but it can vary IF U HAVE A COST TABLE
                            '''
                            g2 = g + cost
                            h2 = heuristic[x2][y2]
                            f2 = g2 + h2
                            open_list.append([f2, g2, h2, x2, y2]) #add new node
                            closed_list[x2][y2] = 1 #Add to visited list
                            policy[x2][y2] = 1 #Which direction you want to go in based off of the corresponding delta[i]




    return path, expand, policy


path, expand, policy = search(grid, init, goal, cost, heuristic)
print(path)
for i in range(len(expand)):
    print(expand[i])

# --------------------------------------------------------------------
# 18. VALUE PROGRAM
print("\n18. VALUE PROGRAM")
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal.
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


# def compute_value(grid, goal, cost):
#     value = []
#     # TODO: ADD CODE HERE
#     # make sure your function returns a grid of values as
#     # demonstrated in the previous video.
#
#     value = [[99 for col in range(len(grid[0]))] for row in range(len(grid))]
#
#     change = True
#     # while change:
#     #     change = False
#     #
#     #     for x in range(len(grid)):
#     #         for y in range(len(grid[0])):
#     #             if goal[0] == x and goal[1] == y:
#     # #                 if value[x][y] >0:
#     # #
#     # # value = [[99 for j in range(len(grid[0]))] for i in range(len(grid))]
#     # change = True
#
#     while change:
#         change = False
#         for x in range(len(grid)):
#             for y in range(len(grid[0])):
#                 if goal[0] == x and goal[1] == y:
#                     if value[x][y] > 0:
#
#                         value[x][y] = 0
#                         change = True
#                 elif grid[x][y] == 0:
#                     for a in range(len(delta)):
#
#                         x2 = x + delta[a][0]
#                         y2 = y + delta[a][1]
#
#                         if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
#
#                         x2 = x + delta[a][0] #delta[0] -> produces array [num1, num2] THEN you get [0] index, [a][0] is not an matrix pair
#                         y2 = y + delta[a][1]
#
#                         if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x][y] == 0:
#
#                             v2 = value[x2][y2] + cost
#
#                             if v2 < value[x][y]:
#                                 change = True
#                                 value[x][y] = v2
#
#
#     return value
#
#
# value = compute_value(grid, goal, cost)
# for i in range(len(value)):
#     print(value[i])
#
# # --------------------------------------------------------------------
# # 19. OPTIMUM POLICY
# print("\n19. OPTIMUM POLICY")
# # Write a function optimum_policy that returns
# # a grid which shows the optimum policy for robot
# # motion. This means there should be an optimum
# # direction associated with each navigable cell from
# # which the goal can be reached.
# #
# # Unnavigable cells as well as cells from which
# # the goal cannot be reached should have a string
# # containing a single space (' '), as shown in the
# # previous video. The goal cell should have '*'.
#
# grid = [[0, 0, 1, 0, 0, 0],
#         [0, 0, 1, 0, 0, 0],
#         [0, 0, 1, 0, 0, 0],
#         [0, 0, 0, 0, 1, 0],
#         [0, 0, 1, 1, 1, 0],
#         [0, 0, 0, 0, 1, 0]]
#
# init = [0, 0]
# goal = [len(grid)-1, len(grid[0])-1]
# cost = 1
#
# delta = [[-1, 0],  # go up
#          [0, -1],  # go left
#          [1, 0],  # go down
#          [0, 1]]  # go right
#
# delta_name = ['^', '<', 'v', '>']
#
#
# def compute_value(grid, goal, cost):
#     value = [[99 for j in range(len(grid[0]))] for i in range(len(grid))]
#     policy = [[' ' for j in range(len(grid[0]))] for i in range(len(grid))]
#     # Copy and paste your solution code from the previous exercise (#18)
#     # TODO: CHANGE/UPDATE CODE
#     change = True
#
#     while change:
#         change = False
#
#         for x in range(len(grid)):
#             for y in range(len(grid[0])):
#                 if goal[0] == x and goal[1] == y:
#                     if value[x][y] > 0:
#                         value[x][y] = 0
#
#                         policy[x][y] = '*'
#                         change = True
#
#                         policy[x][y] = "*"
#                         change = True
#
#
#                 elif grid[x][y] == 0:
#                     for a in range(len(delta)):
#                         x2 = x + delta[a][0]
#                         y2 = y + delta[a][1]
#
#
#                         if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
#
#                         if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x][y] == 0:
#
#                             v2 = value[x2][y2] + cost
#
#                             if v2 < value[x][y]:
#                                 change = True
#                                 value[x][y] = v2
#                                 policy[x][y] = delta_name[a]
#
#
#
#     return value, policy
#
#
# value, policy = compute_value(grid, goal, cost)
# for i in range(len(policy)):
#     print(policy[i])
#
# # --------------------------------------------------------------------
# # 20. LEFT TURN POLICY
# print("\n20. LEFT TURN POLICY")
# # You are given a car in grid with initial state
# # init. Your task is to compute and return the car's
# # optimal path to the position specified in goal;
# # the costs for each motion are as defined in cost.
#
# # grid format:
# #     0 = navigable space
# #     1 = unnavigable space
# grid = [[1, 1, 1, 0, 0, 0],
#         [1, 1, 1, 0, 1, 0],
#         [0, 0, 0, 0, 0, 0],
#         [1, 1, 1, 0, 1, 1],
#         [1, 1, 1, 0, 1, 1]]
#
# init = [4, 3, 0]  # given in the form [row,col,direction]
#
# goal = [2, 0]  # given in the form [row,col]
#
# cost = [2, 1, 20]  # cost has 3 values, corresponding to making a right turn, no turn, and a left turn
#
# # There are four motion directions: up, left, down, and right.
# # Increasing the index in this array corresponds to making a
# # a left turn, and decreasing the index corresponds to making a
# # right turn.
#
# forward = [[-1,  0],  # go up
#             [0, -1],  # go left
#             [1,  0],  # go down
#             [0,  1]]  # go right
# forward_name = ['up', 'left', 'down', 'right']
#
# # action has 3 values: right turn, no turn, left turn
# action = [-1, 0, 1]
# action_name = ['R', '#', 'L']
#
#
# def optimum_policy2D(grid,init,goal,cost):
#     value = [[[999 for col in range(len(grid[0]))] for row in range(len(grid))],
#              [[999 for col in range(len(grid[0]))] for row in range(len(grid))],
#              [[999 for col in range(len(grid[0]))] for row in range(len(grid))],
#              [[999 for col in range(len(grid[0]))] for row in range(len(grid))]]
#     # TODO: ADD CODE HERE
#     policy2D = []
#     return policy2D
#
#
# policy2D = optimum_policy2D(grid, init, goal, cost)
# for i in range(len(policy2D)):
#     print(policy2D[i])
