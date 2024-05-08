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

import math
from heapq import heapify, heappush, heappop
# If you see different scores locally and on Gradescope this may be an indication
# that you are uploading a different file than the one you are executing locally.
# If this local ID doesn't match the ID on Gradescope then you uploaded a different file.
OUTPUT_UNIQUE_FILE_ID = False
if OUTPUT_UNIQUE_FILE_ID:
    import hashlib, pathlib

    file_hash = hashlib.md5(pathlib.Path(__file__).read_bytes()).hexdigest()
    print(f'Unique file ID: {file_hash}')


class DeliveryPlanner_PartA:
    '''
    !!! WHERE I STOPPED !!! "stopping at 8/10 solved. Need to work on testcase 4 (moving off of dropzone if you are standing on it) and testcase 9 (not sure issue but (9,3) is in open_list twice and tie is not broken for some reason"
    '''



    """
    Note: All print outs must be conditioned on the debug parameter.

    Required methods in this class are:
    
      plan_delivery(self, debug = False):
       Stubbed out below.  You may not change the method signature
        as it will be called directly by the autograder but you
        may modify the internals as needed.
    
      __init__:
        Required to initialize the class.  Signature can NOT be changed.
        Basic template starter code is provided.  You may choose to
        use this starter code or modify and replace it based on
        your own solution.
    """

    def __init__(self, warehouse_viewer, dropzone_location, todo, box_locations):

        self.warehouse_viewer = warehouse_viewer
        self.dropzone_location = dropzone_location
        self.todo = todo
        self.box_locations = box_locations

        # You may use these symbols indicating direction for visual debugging
        # ['^', '<', 'v', '>', '\\', '/', '[', ']']
        # or you may choose to use arrows instead
        # ['🡑', '🡐', '🡓', '🡒',  '🡔', '🡕', '🡖', '🡗']


    def findCoordsInList(self, x, y, listToSearch):
        '''
        find a set of coordinates in a given list
        -> Specifically, find a (x,y) in the visited list
        '''

        for i in range(len(listToSearch)):
            f,g,h,list_x,list_y, par_x, par_y = listToSearch[i]
            # print(f,g,h,list_x,list_y, par_x, par_y)
            if x == list_x and y == list_y:
                # print(x,y)
                return x,y

        return -1, -1

    def heuristic_calc(self, curr_node, goal_node):
        # Heuristic calculator
        x, y = curr_node[0], curr_node[1]
        goal_x, goal_y = goal_node[0], goal_node[1]

        #more specific heuristic
        #Code refrenced from https://theory.stanford.edu/~amitp/GameProgramming/Heuristics.html#heuristics-for-grid-maps
        dx = abs(x - goal_x)
        dy = abs(y - goal_y)

        return (2 * (dx + dy)) + ((3 - 2 * 2) * min(dx, dy))

        #end of code citation



    def a_star(self, start_x, start_y, goal_x, goal_y, box_in_hand, boxes_delivered):
        '''

        Implementation of A star algo
        '''

        #Setup A* given any start and goal coordinates
        g = 0
        h = self.heuristic_calc((start_x, start_y), (goal_x, goal_y))
        f = g + h
        open_list = [(f, g, h, start_x, start_y, -1, -1)] #aka minheap
        heapify(open_list)
        open_set = set()
        open_set.add((start_x, start_y))
        closed_set = set()
        parent_dict = {(start_x,start_y): None}

        #motion tables
        motion_cost = [2, 2, 2, 2, 3, 3, 3, 3]

        motion = [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        motion_dict = {
            (-1, 0): 'n',  # (row, col)
            (1, 0): 's',
            (0, 1): 'e',
            (0, -1): 'w',
            (-1, -1): 'nw',
            (-1, 1): 'ne',
            (1, -1): 'sw',
            (1, 1): 'se'
        }

        while open_list:
            curr_node = heappop(open_list)
            curr_x, curr_y = curr_node[3], curr_node[4]
            open_set.remove((curr_x, curr_y))
            closed_set.add((curr_x, curr_y))
            # print('curr x, curry is', curr_x, curr_y)
            # print('closed set is', closed_set)
            #--------------
            #code fragment for if curr_x, curr_y is the goal
            #---------------
            # if curr_x == goal_x and curr_y == goal_y:
            #     # Code to backtrack up parents dict
            #     #####Tracking f,g,h
            #     # optimal path and motion
            #     optimal_path = [(curr_x, curr_y)]
            #     optimal_motion = []
            #
            #     while parent_dict[(curr_x, curr_y)] != None:
            #         parent_x, parent_y = parent_dict[(curr_x, curr_y)]
            #         # optimal motion:
            #         x_diff = curr_x - parent_x
            #         y_diff = curr_y - parent_y
            #
            #         optimal_motion.append(motion_dict[(x_diff, y_diff)])
            #         # optimal path
            #         optimal_path.append((parent_x, parent_y))
            #         curr_x, curr_y = parent_x, parent_y
            #     # print('final path is', optimal_path)
            #     optimal_path.reverse()
            #     optimal_motion.reverse()
            #
            #     # print('local optimal path', optimal_path)
            #     # print('local optimal motion', optimal_motion)
            #
            #     return optimal_motion, optimal_path
            #---------------------

            # Remove curr_x, curr_y to minheap
            # Check all neighbors

            for i in range(len(motion)):
                cx, cy = motion[i]
                neighbor_x = curr_x + cx  # x + change_x
                neighbor_y = curr_y + cy  # y + change_y
                neighbor_g = motion_cost[i] + curr_node[1]
                neighbor_h = self.heuristic_calc((neighbor_x, neighbor_y), (goal_x, goal_y))
                neighbor_f = neighbor_g + neighbor_h

                ##if you find the goal
                if neighbor_x == goal_x and neighbor_y == goal_y:
                    path_to_goal = [(curr_x, curr_y)]

                    motions_to_goal = []

                    #This is the motion of lifting/dropping box when you are right next to the goal
                    if not box_in_hand:
                        #looking for box
                        motions_to_goal.append('lift ' + self.warehouse_viewer[neighbor_x][neighbor_y])
                    else:
                        #look for dropzone
                        x_diff = neighbor_x - curr_x
                        y_diff = neighbor_y - curr_y
                        motions_to_goal.append('down ' + motion_dict[(x_diff, y_diff)])

                    #Creating motion path
                    while parent_dict[(curr_x, curr_y)] != None:
                        parent_x, parent_y = parent_dict[(curr_x, curr_y)]
                        # optimal motion:
                        x_diff = curr_x - parent_x
                        y_diff = curr_y - parent_y

                        motions_to_goal.append('move ' + motion_dict[(x_diff, y_diff)])
                        # optimal path
                        path_to_goal.append((parent_x, parent_y))
                        curr_x, curr_y = parent_x, parent_y
                        # print('final path is', optimal_path)
                    path_to_goal.reverse()
                    motions_to_goal.reverse()
                    # print(motions_to_goal)
                    # print(path_to_goal)
                    # print(path_to_goal[-1][0], path_to_goal[-1][1])

                    return motions_to_goal, path_to_goal[-1][0], path_to_goal[-1][1] #return

                # if we encounter a box that blocks the way but it is not the one we want
                # if self.warehouse_viewer[neighbor_x][neighbor_y].isalum() and self.warehouse_viewer[neighbor_x][neighbor_y] != box_name:
                #     continue
                if self.warehouse_viewer[neighbor_x][neighbor_y] in self.todo and self.warehouse_viewer[neighbor_x][neighbor_y] not in boxes_delivered:
                    continue
                # Search the closed list
                if self.warehouse_viewer[neighbor_x][neighbor_y] == '#' or (neighbor_x, neighbor_y) in closed_set:
                    continue

                #if neighborx, neighbor_y is in the open_set, compare the values and keep the one with the lower G value
                if (neighbor_x, neighbor_y) in open_set:
                    match_index = 0
                    for j in range(len(open_list)):
                        # Find neighbor_x, neighbor_y in open_list and retrieve the G in the openlist
                        open_x, open_y = open_list[j][3], open_list[j][4]
                        if (open_x == neighbor_x and open_y == neighbor_y):
                            open_g = open_list[j][1]
                            match_index = j

                    #Compare neighbor_g to open_g and replace or keep
                    if (neighbor_g >= open_g):
                        # print('here3')
                        continue
                    else:
                        '''
                        Cheesy way to replace the higher G. If the new node has a lower G value, replace that node's value and re-heapify
                        '''
                        open_list[match_index] = [neighbor_f, neighbor_g, neighbor_h, neighbor_x, neighbor_y, curr_x, curr_y]
                        parent_dict[(neighbor_x, neighbor_y)] = (curr_x, curr_y)
                        heapify(open_list)
                        continue

                # print('here4')
                heappush(open_list, [neighbor_f, neighbor_g, neighbor_h, neighbor_x, neighbor_y, curr_x, curr_y])
                open_set.add((neighbor_x, neighbor_y))
                parent_dict[(neighbor_x, neighbor_y)] = (curr_x, curr_y)
                # optimal_motion.append(motion_name[i])
                # print(motion_path)
                # print('motion is', motion_name[i])
        print('not found')
        return [-1], [-1], -1 ,-1

    def plan_delivery(self, debug=False):
        """
        plan_delivery() is required and will be called by the autograder directly.
        You may not change the function signature for it.
        All print outs must be conditioned on the debug flag.
        """

        # The following is the hard coded solution to test case 1
        # params to track actual project problem as needed
        self.warehouse_viewer
        self.dropzone_location
        self.todo
        self.box_locations

        # You may use these symbols indicating direction for visual debugging
        # ['^', '<', 'v', '>', '\\', '/', '[', ']']
        # or you may choose to use arrows instead
        # ['🡑', '🡐', '🡓', '🡒',  '🡔', '🡕', '🡖', '🡗']
        # print(warehouse_viewer)
        # print(dropzone_location)
        # print(todo)
        # print(box_locations)

        ##Motion cost tables
        motion_cost = [2, 2, 2, 2, 3, 3, 3, 3]
        motion_name = ['n', 's', 'e', 'w', 'se', 'sw', 'nw', 'ne']
        motion = [(-1, 0), (1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, -1), (1, 1)]

        motion_dict = {
            (-1, 0): 'n',  # (row, col)
            (1, 0): 's',
            (0, 1): 'e',
            (0, -1): 'w',
            (-1, -1): 'nw',
            (-1, 1): 'ne',
            (1, -1): 'sw',
            (1, 1): 'se'
        }
        # Up, down, right, left, se, sw, nw, ne

        box_in_hand = False  # Flag if box is in hand
        overall_motions = []
        overall_path = []
        boxes_delivered = ''
        # goal_x, goal_y = self.box_locations[self.todo[0]] #Very first goal
        start_x, start_y = self.dropzone_location
        counter = 0
        #main function to solve all boxes
        for i in range(len(self.todo)):
            goal_x, goal_y = self.box_locations[self.todo[i]]
            #find the box
            box_in_hand = False
            path_motions, last_x, last_y = self.a_star(start_x, start_y, goal_x, goal_y, box_in_hand, boxes_delivered)
            for j in range(len(path_motions)):
                #sloppy way of crafting overall box finding steps
                overall_motions.append(path_motions[j])

            boxes_delivered += self.todo[i] #technically, this isn't boxes_delivered but boxes_moved ->
                                            # i use this as a flag in A* to check for "old" boxes that have been moved so they aren't obstructing the way anymore
            #find the dropzone
            box_in_hand = True
            path_motions, last_x, last_y = self.a_star(last_x, last_y, self.dropzone_location[0], self.dropzone_location[1], box_in_hand, boxes_delivered)
            for j in range(len(path_motions)):
                #sloppy way of crafting overall box finding steps
                overall_motions.append(path_motions[j])


            ##update for next iteration

            start_x = last_x
            start_y = last_y

        # print(overall_motions)



        #
        # if debug:
        #     for i in range(len(moves)):
        #         print(moves[i])

        moves = overall_motions
        return moves

##Project version
# #test case 1
# warehouse_viewer = [
#                       '########',
#                       '#5######',
#                       '#I#234J#',
#                       '#H#1##6#',
#                       '#G#0@#7#',
#                       '#F####8#',
#                       '#EDCBA9#',
#                       '########'
#                   ]
# todo = list('12')
#
# dropzone_location = (4, 4)
# box_locations = {
#
#     '1':(2,2),
#     '2':(2,4)
# }
#
# testinstance = DeliveryPlanner_PartA(warehouse_viewer, dropzone_location, todo, box_locations)
# testinstance.plan_delivery()
#


##Testcase 4
# warehouse_viewer = [
#     #01234567
#     '########',#0
#     '#5######',#1
#     '#I#234J#',#2
#     '#H#1##6#',#3
#     '#G#0@#7#',#4
#     '#F####8#',#5
#     '#EDCBA9#',#6
#     '########'#7
# ]
# todo = list('01234J6789ABCDEFGHI5')
# #
# dropzone_location = (4, 4)
# box_locations = {
#
#     '0': (4,3),
#     '1': (3,3),
#     '2': (2,3),
#     '3': (2,4),
#     '4': (2,5),
#     '5': (1,1),
#     '6': (3,6),
#     '7': (4,6),
#     '8': (5,6),
#     '9': (6,6),
#     'A': (6,5),
#     'B': (6,4),
#     'C': (6,3),
#     'D': (6,2),
#     'E': (6,1),
#     'F': (5,1),
#     'G': (4,1,),
#     'H': (3,1),
#     'I': (2,1),
#     'J': (2,6)
# }


#testcase 9
# warehouse_viewer = [
#     #01234567
#     '###########',#0
#     '#....1....#',#1
#     '#....###..#',#2
#     '#...##.##.#',#3
#     '#..##.....#',#4
#     '###.#..#.##',#5
#     '#..##..#..#',#6
#     '#...#####.#',#7
#     '#.#..#@...#',#8
#     '#.........#',#9
#     '###########'#10
# ]
# todo = list('1')
#
# dropzone_location = (8, 6)
# box_locations = {
#
#
#     '1': (1,5),
#
#
# }

# testinstance = DeliveryPlanner_PartA(warehouse_viewer, dropzone_location, todo, box_locations)
# testinstance.plan_delivery()
class DeliveryPlanner_PartB:
    """
    Note: All print outs must be conditioned on the debug parameter.

    Required methods in this class are:

        generate_policies(self, debug = False):
         Stubbed out below. You may not change the method signature
         as it will be called directly by the autograder but you
         may modify the internals as needed.

        __init__:
         Required to initialize the class.  Signature can NOT be changed.
         Basic template starter code is provided.  You may choose to
         use this starter code or modify and replace it based on
         your own solution.

    The following method is starter code you may use.
    However, it is not required and can be replaced with your
    own method(s).

        _set_initial_state_from(self, warehouse):
         creates structures based on the warehouse map

    """

    def __init__(self, warehouse, warehouse_cost, todo):

        self._set_initial_state_from(warehouse)
        self.warehouse_cost = warehouse_cost
        self.todo = todo



        # You may use these symbols indicating direction for visual debugging
        # ['^', '<', 'v', '>', '\\', '/', '[', ']']
        # or you may choose to use arrows instead
        # ['🡑', '🡐', '🡓', '🡒',  '🡔', '🡕', '🡖', '🡗']

    def _set_initial_state_from(self, warehouse):
        """Set initial state.

        Args:
            warehouse(list(list)): the warehouse map.
        """
        rows = len(warehouse)
        cols = len(warehouse[0])

        self.warehouse_state = [[None for j in range(cols)] for i in range(rows)]
        self.dropzone = None
        self.boxes = dict()

        for i in range(rows):
            for j in range(cols):
                this_square = warehouse[i][j]

                if this_square == '.':
                    self.warehouse_state[i][j] = '.'

                elif this_square == '#':
                    self.warehouse_state[i][j] = '#'

                elif this_square == '@':
                    self.warehouse_state[i][j] = '@'
                    self.dropzone = (i, j)

                else:  # a box
                    box_id = this_square
                    self.warehouse_state[i][j] = box_id
                    self.boxes[box_id] = (i, j)

    def generate_policies(self, debug=False):
        """
        generate_policies() is required and will be called by the autograder directly.
        You may not change the function signature for it.
        All print outs must be conditioned on the debug flag.
        """
        motion_cost = [2, 2, 2, 2, 3, 3, 3, 3]
        motion_name = ['n', 's', 'e', 'w', 'se', 'sw', 'nw', 'ne']
        motion = [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        # motion_dict = {
        #     'n': (-1, 0),  # (row, col)
        #     's': (1, 0),
        #     'e': (0, 1),
        #     'w': (0, -1),
        #     'nw': (-1, -1),
        #     'ne': (-1, 1),
        #     'sw': (1, -1),
        #     'se': (1, 1)
        # }
        motion_dict = {
            (-1, 0): 'n',  # (row, col)
            (1, 0): 's',
            (0, 1): 'e',
            (0, -1): 'w',
            (-1, -1): 'nw',
            (-1, 1): 'ne',
            (1, -1): 'sw',
            (1, 1): 'se'
        }
        # Up, down, right, left, se, sw, nw, ne

        ##Action cost tables
        action_cost = [4, 2]
        action_name = ['lift', 'down']
        action = ['Anything go here?????']

        def vi_search(goal_symbol, goal_x, goal_y, box_in_hand):
            values = [[200000 for col in range(len(self.warehouse_state[0]))] for row in range(len(self.warehouse_state))]
            policy = [[' ' for col in range(len(self.warehouse_state[0]))] for row in range(len(self.warehouse_state))]
            warehouse = self.warehouse_state
            warehouse_cost = self.warehouse_cost
            convergence = True
            # print('self.warehouse is', self.warehouse_state)
            # print('warehouse is', warehouse)

            while convergence:
                convergence = False
                closed_set = set()
                for i in range(len(warehouse)):
                    for j in range(len(warehouse[0])):

                        # print('coordsa are', i,j)

                        if warehouse[i][j] == '#':
                            values[i][j] = -1
                            continue
                        #if goal is foud
                        # change self_todo to goal_symbol ie @ or boxname
                        if warehouse[i][j] == goal_symbol:
                            # print('goal is at ', i,j)
                            # print(values[r][c])
                            if values[i][j] >0:
                                # if goal is found but that is the first time you are visiting it, update it and recalc grid
                                values[i][j] = 0
                                warehouse_cost[i][j] = 0
                                convergence = True
                                policy[i][j] = goal_symbol
                            # else:
                            #     #Conditon to end VI as you've found thee goal
                            #
                            #     policy[i][j] = goal_symbol
                            #     # convergence = True
                            #     # print('goal is found')
                            #     # print('policy is', policy)
                            #     # print('values is', values)
                            #     # return policy, values
                        else:
                            #if goal isn't found, check the neighbors
                            min_cost = values[i][j]
                            min_direction = ''

                            for k in range(len(motion_name)):
                                #neww neighbor calc
                                rc, cc = motion[k] #row change, column change
                                # print('coords are', i, j)
                                # print('motion is', (rc, cc))
                                # print('motion direction is', motion_dict[(rc, cc)])

                                nr = rc + i
                                nc = cc + j
                                # print('nr nc is ', nr, nc)

                                #



                                if nr < 0 or nr >= len(warehouse) or nc < 0 or nc >= len(warehouse[0]) or warehouse[nr][nc] == '#':
                                    #out of bounds OR you hit a wall
                                    total_curr_cost = motion_cost[k] + 100 + values[i][j]
                                    if total_curr_cost < min_cost:
                                        #NOTE A BIT OF A NAIVE CHECK BECAUSE THIS IS OUT OF BOUNDS SO I'M JUST CALCUATING MINCOST IN CASE
                                        min_cost = total_curr_cost
                                        print('convergence edge case')
                                        convergence = True
                                    continue
                                    #check if this cost is < recorded_min_cost

                                if warehouse[nr][nc] == goal_symbol and box_in_hand == False:
                                    #goal is a box, not a dropzone
                                    # print('warehouse cost is',warehouse_cost[nr][nc] )
                                    # print('values cost is',values[nr][nc] )
                                    total_curr_cost = 4 + warehouse_cost[nr][nc] + values[nr][nc]
                                    # print('goal neight')
                                    # print(total_curr_cost)
                                elif warehouse[nr][nc] == goal_symbol and box_in_hand == True:
                                    #dropping into dropzone
                                    total_curr_cost = 2 + warehouse_cost[nr][nc] + values[nr][nc]
                                else:
                                    #normal squre
                                    total_curr_cost = motion_cost[k] + warehouse_cost[nr][nc] + values[nr][nc]



                                #Once total cost is calcualted, check compared to min_cost

                                if total_curr_cost < min_cost:
                                    # print('convergence flag at total cost')
                                    min_cost = total_curr_cost
                                    convergence = True


                                # neighbors_values.append(min_cost)
                                # print(neighbors_values)
                                values[i][j] = min_cost
                                policy[i][j] = motion_dict[(rc, cc)]

                        # print('values are', values)
                        # print('policy is', policy)


            print('-------------------------------------part 2 -----------------------------')

            #craft policy
            for q in range(len(warehouse)):
                for e in range(len(warehouse[0])):


                    # print('q e is', q, e)
                    #default values
                    min_value = 200000
                    min_direction = ''

                    if warehouse[q][e] == '#':
                        policy[q][e] = '-1'
                        continue

                    if warehouse[q][e] == goal_symbol and box_in_hand == False:
                        policy[q][e] = 'B'
                        print('goal is at ', q,e)
                        continue

                    #search each direction and choose lowest neighbor + corresponding directiong
                    for k in range(len(motion_name)):
                        rc, cc = motion[k]  # row change, column change
                        nr = rc + q
                        nc = cc + e

                        if nr < 0 or nr >= len(warehouse) or nc < 0 or nc >= len(warehouse[0]) or warehouse[nr][nc] == '#':
                            # print('skipping',nr,cc)
                            continue
                        # neww neighbor calc

                        # print('coords are', i, j)
                        # print('motion is', (rc, cc))
                        # print('motion direction is', motion_dict[(rc, cc)])
                        if warehouse[nr][nc] == goal_symbol and box_in_hand == False:
                            # goal is a box, not a dropzone
                            neighbor_cost = 4 + warehouse_cost[nr][nc] + values[q][e]
                            if neighbor_cost < min_value:
                                min_value = neighbor_cost
                                min_direction = 'lift ' + goal_symbol
                                policy[q][e] = min_direction
                        elif warehouse[nr][nc] == goal_symbol and box_in_hand == True:
                            # dropping into dropzone
                            neighbor_cost = 2 + warehouse_cost[nr][nc] + values[nr][nc]
                            if neighbor_cost < min_value:
                                min_value = neighbor_cost
                                min_direction = 'down ' + motion_dict[(rc, cc)]
                                policy[q][e] = min_direction
                        else:
                            # normal squre
                            neighbor_cost = motion_cost[k] + warehouse_cost[nr][nc] + values[nr][nc]
                            if neighbor_cost < min_value:
                                min_value = neighbor_cost
                                min_direction = 'move ' + motion_dict[(rc, cc)]
                                policy[q][e] = min_direction




            #
            # for a in range(len(values)):
            #     print(values[a])
            #
            # for b in range(len(policy)):
            #     print(policy[b])

            # print('values are', values)
            # print('policy is', policy)
            return values, policy





        to_box_values, to_box_policy = vi_search('1', 1., 2, False)
        print('box found')

        deliver_box_values, deliver_policy = vi_search('@', 1., 2, True)
        print('box delivered')

        # deliver_policy = []

        # The following is the hard coded solution to test case 1
        # to_box_policy = [['B', 'lift 1', 'move w'],
        #           ['lift 1', '-1', 'move nw'],
        #           ['move n', 'move nw', 'move n']]
        #
        # deliver_policy = [['move e', 'move se', 'move s'],
        #           ['move ne', '-1', 'down s'],
        #           ['move e', 'down e', 'move n']]

        # if debug:
        #     print("\nTo Box Policy:")
        #     for i in range(len(to_box_policy)):
        #         print(to_box_policy[i])
        #
        #     print("\nDeliver Policy:")
        #     for i in range(len(deliver_policy)):
        #         print(deliver_policy[i])

        return (to_box_policy, deliver_policy)
# w = 10000
# #test case 1
# #
# warehouse= ['1..',
#             '.#.',
#             '..@']
# warehouse_cost = [
#     [3, 5, 2],
#     [10, w, 2],
#     [2, 10, 2]
#     ]
# todo = ['1']
#test case 2
# w = math.inf
# todo = ['1']
# warehouse= ['............#...............',
#                                 '......#.....#...............',
#                                 '.....................#......',
#                                 '............................',
#                                 '..1...#.....................',
#                                 '............##########......',
#                                 '......#..#..#.........#.....',
#                                 '.........#..#....@....#.....',
#                                 '......#.....#.........#.....',
#                                 '............#.........#.....']
# warehouse_cost = [[94, 56, 14, 0, 11, 74, 4, 85, 88, 10, 12, 93, w, 45, 30, 2, 3, 95, 2, 44, 82, 79, 61, 78, 59, 19, 11, 23],
#                  [91, 14, 1, 64, 62, 31, w, 8, 85, 69, 59, 8, w, 76, 86, 11, 65, 74, 5, 34, 71, 8, 82, 38, 61, 45, 34, 31],
#                  [83, 25, 58, 67, 85, 2, 65, 9, 0, 42, 18, 90, 60, 84, 48, 21, 6, 9, 75, 63, 20, w, 9, 71, 27, 18, 3, 44],
#                  [93, 14, 67, 18, 85, 39, 58, 5, 53, 35, 84, 5, 22, 34, 19, 38, 19, 94, 59, 5, 72, 49, 92, 44, 63, 43, 74, 59],
#                  [60, 5, 95, 60, 76, 21, w, 56, 93, 94, 66, 56, 37, 35, 15, 94, 23, 53, 55, 93, 15, 67, 13, 62, 48, 84, 32, 82],
#                  [24, 44, 13, 89, 89, 20, 74, 34, 19, 92, 41, 95, w, w, w, w, w, w, w, w, w, w, 57, 92, 9, 10, 50, 27],
#                  [6, 36, 4, 28, 64, 11, w, 89, 40, w, 39, 58, w, 8, 74, 32, 9, 88, 54, 25, 12, 50, w, 24, 90, 58, 64, 30],
#                  [46, 26, 65, 89, 53, 22, 74, 26, 38, w, 7, 45, w, 68, 19, 63, 93, 70, 60, 42, 17, 16, w, 6, 79, 21, 18, 69],
#                  [8, 91, 41, 21, 0, 85, w, 86, 7, 81, 11, 92, w, 18, 27, 5, 55, 50, 94, 41, 26, 86, w, 48, 35, 68, 80, 38],
#                  [54, 40, 87, 73, 19, 68, 11, 92, 33, 35, 52, 51, w, 72, 35, 67, 14, 89, 48, 35, 27, 38, w, 91, 75, 50, 6, 44]]
#
# tester = DeliveryPlanner_PartB(warehouse, warehouse_cost, todo)
# tester.generate_policies()

class DeliveryPlanner_PartC:
    """
    [Doc string same as part B]
    Note: All print outs must be conditioned on the debug parameter.

    Required methods in this class are:

        generate_policies(self, debug = False):
         Stubbed out below. You may not change the method signature
         as it will be called directly by the autograder but you
         may modify the internals as needed.

        __init__:
         Required to initialize the class.  Signature can NOT be changed.
         Basic template starter code is provided.  You may choose to
         use this starter code or modify and replace it based on
         your own solution.

    The following method is starter code you may use.
    However, it is not required and can be replaced with your
    own method(s).

        _set_initial_state_from(self, warehouse):
         creates structures based on the warehouse map

    """

    def __init__(self, warehouse, warehouse_cost, todo, stochastic_probabilities):

        self._set_initial_state_from(warehouse)
        self.warehouse_cost = warehouse_cost
        self.todo = todo
        self.stochastic_probabilities = stochastic_probabilities

        # You may use these symbols indicating direction for visual debugging
        # ['^', '<', 'v', '>', '\\', '/', '[', ']']
        # or you may choose to use arrows instead
        # ['🡑', '🡐', '🡓', '🡒',  '🡔', '🡕', '🡖', '🡗']

    def _set_initial_state_from(self, warehouse):
        """Set initial state.

        Args:
            warehouse(list(list)): the warehouse map.
        """
        rows = len(warehouse)
        cols = len(warehouse[0])

        self.warehouse_state = [[None for j in range(cols)] for i in range(rows)]
        self.dropzone = None
        self.boxes = dict()

        for i in range(rows):
            for j in range(cols):
                this_square = warehouse[i][j]

                if this_square == '.':
                    self.warehouse_state[i][j] = '.'

                elif this_square == '#':
                    self.warehouse_state[i][j] = '#'

                elif this_square == '@':
                    self.warehouse_state[i][j] = '@'
                    self.dropzone = (i, j)

                else:  # a box
                    box_id = this_square
                    self.warehouse_state[i][j] = box_id
                    self.boxes[box_id] = (i, j)

    def generate_policies(self, debug=False):
        """
        generate_policies() is required and will be called by the autograder directly.
        You may not change the function signature for it.
        All print outs must be conditioned on the debug flag.
        """
        warehouse = self.warehouse_state
        motion_cost = [2,3,2,3,2,3,2,3]
        motion_name = ['n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw']
        motion = [(-1, 0), (-1,1), (0,1), (1, 1), (1,0), (1, -1), (0, -1), (-1,-1)  ]
        # print('warehouse is', warehouse)
        # print('self warehouse is', self.warehouse_state)
        motion_dict = {
            (-1, 0): 'n',  # (row, col)
            (1, 0): 's',
            (0, 1): 'e',
            (0, -1): 'w',
            (-1, -1): 'nw',
            (-1, 1): 'ne',
            (1, -1): 'sw',
            (1, 1): 'se'
        }


        ##Action cost tables
        # action_cost = [4, 2]
        # action_name = ['lift', 'down']
        # action = ['Anything go here?????']

        def vi_search(goal_symbol, goal_x, goal_y, box_in_hand):
            values = [[110000 for col in range(len(self.warehouse_state[0]))] for row in range(len(self.warehouse_state))]
            policy = [[' ' for col in range(len(self.warehouse_state[0]))] for row in range(len(self.warehouse_state))]
            warehouse = self.warehouse_state
            warehouse_cost = self.warehouse_cost
            probabilites = self.stochastic_probabilities
            s_probabilities = [probabilites['sideways'], probabilites['slanted'], probabilites['as_intended'], probabilites['slanted'], probabilites['sideways']]
            convergence = True


            while convergence:
                convergence = False
                for i in range(len(warehouse)):
                    for j in range(len(warehouse[0])):

                        if warehouse[i][j] == '#':
                            values[i][j] = -1
                            continue
                        # if goal is foud

                        if warehouse[i][j] == goal_symbol:
                            if values[i][j] > 0:
                                # if goal is found but that is the first time you are visiting it, update it and recalc grid
                                values[i][j] = 0
                                warehouse_cost[i][j] = 0
                                convergence = True
                                policy[i][j] = 'B'
                        else:
                            # if goal isn't found, check the neighbors
                            min_value = values[i][j]
                            ev_array = [] #get expected values for each INTENDED direction given stochastic motion
                            ev_direction = []
                            for k in range(len(motion)):
                                #for each INTENDED direction, calculate the Expected value given stochastic motion
                                # print('ij is', i, j)
                                a, b = motion[k]
                                intended_nr = a + i
                                intended_nc = b + j
                                # print(intended_nr, intended_nc)
                                #for each direction
                                prob = 0
                                ev_direction.append(motion_dict[(a,b)])

                                #checking if intended direction is the goal, if so, do deterministic drop
                                if 0 <= intended_nr < len(warehouse) and 0 <= intended_nc < len(warehouse[0]):
                                    if warehouse[intended_nr][intended_nc] == goal_symbol:
                                        #intended direction is a box
                                        if box_in_hand == False:
                                            prob = 4 + warehouse_cost[intended_nr][intended_nc] + values[intended_nr][intended_nc]
                                            if prob < min_value:
                                                # print('here')
                                                values[i][j] = prob
                                                convergence = True
                                                continue
                                        else:
                                            prob = 2 + warehouse_cost[intended_nr][intended_nc] + values[intended_nr][intended_nc]
                                            if prob < min_value:
                                                # print('here')
                                                if prob < min_value:
                                                    # print('here')
                                                    values[i][j] = prob
                                                    convergence = True
                                                    continue

                                for l in range(-2, 3):
                                    rc, cc = motion[(k+l) % len(motion)]
                                    nr = rc + i
                                    nc = cc + j

                                    if nr < 0 or nr >= len(warehouse) or nc < 0 or nc >= len(warehouse[0]) or warehouse[nr][nc] == '#':
                                        # out of bounds OR you hit a wall

                                        stochastic_cost = (motion_cost[(k+l) % len(motion)] + 100 + values[i][j]) * s_probabilities[l + 2]
                                        #motion + values + penality (which is the floor cost in this case)st
                                    elif warehouse[nr][nc] == goal_symbol and box_in_hand == False:
                                        # goal is a box, not a dropzone

                                        stochastic_cost = (4 + warehouse_cost[nr][nc] + values[nr][nc])* s_probabilities[l + 2] #motion + floor cost + values cost
                                        # print('goal neight')
                                        # print(total_curr_cost)
                                    elif warehouse[nr][nc] == goal_symbol and box_in_hand == True:
                                        # dropping into dropzone

                                        stochastic_cost = (2 + warehouse_cost[nr][nc] + values[nr][nc])*s_probabilities[l + 2]
                                    else:
                                        # normal squre

                                        stochastic_cost = (motion_cost[(k+l) % len(motion)] + warehouse_cost[nr][nc] + values[nr][nc])*s_probabilities[l+2]

                                    #add the cost of this stochastic direction to the intended direction's probability
                                    prob += stochastic_cost

                                ev_array.append(prob) #append the EV for this intended direction
                            #Now you have all directions Expected values, figure out the minimum and if it's lwoer than the existing value
                            min_ev = ev_array[0]
                            min_ev_direction = motion[0]
                            for p in range(len(ev_array)):
                                #get the min stochastic prob
                                # print('ev array is', ev_array)
                                # print('ev direction is', ev_direction)
                                if (ev_array[p] < min_ev):
                                    min_ev = ev_array[p]

                                    min_ev_direction = ev_direction[p]



                            #Compare min stochastic value to value
                            if min_ev < min_value:
                                # print('here')
                                values[i][j] = min_ev

                                convergence = True


            # print('-----------part 2-----------')
            for q in range(len(warehouse)):
                for e in range(len(warehouse[0])):

                    if warehouse[q][e] == '#':
                        #Walls -> so you don't explore these
                        policy[q][e] = -1
                        continue

                    if warehouse[q][e] == goal_symbol and box_in_hand == False:
                        #If you hit the goal and it's a box, you don't explore it.
                        #if it was a dropzone, you do explore it
                        #this is why I use the box_in_hand flag
                        policy[q][e] = 'B'
                        continue

                    ev_array = []  # get expected values for each INTENDED direction given stochastic motion
                    ev_direction = []

                    for k in range(len(motion)):
                        #For each intended motion, calculate the stochastic motion
                        #intended motion
                        a, b = motion[k]
                        intended_nr = a + q
                        intended_nc = b + e

                        prob = 0
                        if 0 <= intended_nr < len(warehouse) and 0 <= intended_nc < len(warehouse[0]):
                            if warehouse[intended_nr][intended_nc] == goal_symbol:
                                # intended direction is a box
                                if box_in_hand == False:
                                    prob = 4 + warehouse_cost[intended_nr][intended_nc] + values[intended_nr][
                                        intended_nc]
                                    if prob < values[q][e]:
                                        # print('here')
                                        policy[q][e] = 'lift ' + goal_symbol

                                        continue
                                else:
                                    prob = 2 + warehouse_cost[intended_nr][intended_nc] + values[intended_nr][
                                        intended_nc]
                                    if prob < values[q][e]:

                                        policy[q][e] = 'down ' + motion_dict[motion[k]]

                                        continue

                        for l in range(-2, 3):
                            # for each INTENDED direction, calculate the stochastic motion

                            rc, cc = motion[(k + l) % len(motion)]
                            # this intended nr, nc specifically stochastic state nr, nc
                            nr = rc + q
                            nc = cc + e

                            if nr < 0 or nr >= len(warehouse) or nc < 0 or nc >= len(warehouse[0]) or warehouse[nr][
                                nc] == '#':
                                # out of bounds OR you hit a wall
                                stochastic_cost = (motion_cost[(k + l) % len(motion)] + 100 + values[q][e]) * s_probabilities[l + 2]
                                # motion + values + penality (which is the floor cost in this case)
                            elif warehouse[nr][nc] == goal_symbol and box_in_hand == False:
                                # goal is a box, not a dropzone
                                # print('warehouse cost is',warehouse_cost[nr][nc] )
                                # print('values cost is',values[nr][nc] )
                                stochastic_cost = 4 + warehouse_cost[nr][nc] + values[nr][nc]  # motion + floor cost + values cost
                                # print('goal neight')
                                # print(total_curr_cost)
                            elif warehouse[nr][nc] == goal_symbol and box_in_hand == True:
                                # dropping into dropzone
                                stochastic_cost = 2 + warehouse_cost[nr][nc] + values[nr][nc]
                            else:
                                # normal squre
                                stochastic_cost = (motion_cost[(k + l) % len(motion)] + warehouse_cost[nr][nc] + values[nr][nc]) * s_probabilities[l + 2]

                            # add the cost of this stochastic direction to the intended direction's probability
                            prob += stochastic_cost
                        ev_array.append(prob)  # append the EV for this intended direction
                        # print('ev array is', ev_array)


                        ##use this conditonal to craft the motion for each potential intended direction (given that stochastic motion is all calced for each direction)
                        if intended_nr < 0 or intended_nr >= len(warehouse) or intended_nc < 0 or intended_nc >= len(
                                warehouse[0]) or warehouse[intended_nr][
                            intended_nc] == '#':
                            ev_direction.append('move ' + motion_dict[motion[k]])
                        elif warehouse[intended_nr][intended_nc] == goal_symbol and box_in_hand == False:
                            # print('here1')
                            ev_direction.append('lift ' + goal_symbol)

                        elif warehouse[intended_nr][intended_nc] == goal_symbol and box_in_hand == True:
                            # print('here2')
                            ev_direction.append('down ' + motion_dict[motion[k]])
                        else:
                            # print('here3')
                            ev_direction.append('move ' + motion_dict[motion[k]])
                        # print('ev array is', ev_array)
                        # print('ev directions are', ev_direction)

                        ev_min = ev_array[0]
                        ev_min_direction = ev_direction[0]
                        for d in range(1, len(ev_array)):
                            #figure out min INTENDED direction
                            if ev_array[d] < ev_min:
                                ev_min = ev_array[d]
                                ev_min_direction = ev_direction[d]

                        #add min direction to policy
                        policy[q][e] = ev_min_direction



            # for a in range(len(values)):
            #     print(values[a])
            # #
            # for b in range(len(policy)):
            #     print(policy[b])

            # print('values are', values)
            # print('policy is', policy)
            return values, policy

        to_box_values, to_box_policy = vi_search('1', 1., 2, False)
        print('box found')

        to_zone_values, to_zone_policy = vi_search('@', 1., 2, True)
        print('box delivered')

        # deliver_policy = []

        # The following is the hard coded solution to test case 1




        # The following is the hard coded solution to test case 1
        # to_box_policy = [
        #     ['B', 'lift 1', 'move w'],
        #     ['lift 1', -1, 'move nw'],
        #     ['move n', 'move nw', 'move n'],
        # ]
        #
        # to_zone_policy = [
        #     ['move e', 'move se', 'move s'],
        #     ['move se', -1, 'down s'],
        #     ['move e', 'down e', 'move n'],
        # ]

        if debug:
            print("\nTo Box Policy:")
            for i in range(len(to_box_policy)):
                print(to_box_policy[i])

            for i in range(len(to_box_values)):
                print(to_box_values[i])
            print('----')

            print("\nTo Zone Policy:")
            for i in range(len(to_zone_policy)):
                print(to_zone_policy[i])


            for i in range(len(to_zone_values)):
                print(to_zone_values[i])

        # For debugging purposes you may wish to return values associated with each policy.
        # Replace the default values of None with your grid of values below and turn on the
        # VERBOSE_FLAG in the testing suite.
        # to_box_values = None
        # to_zone_values = None
        # print(to_box_values)
        # print(to_zone_values)
        return (to_box_policy, to_zone_policy, to_box_values, to_zone_values)

#testcase 1

#Testcase 2
# w = math.inf
# warehouse = ['1..',
#             '.#.',
#             '..@']
# warehouse_cost = [[13, 5, 6],
#                  [10, w, 2],
#                  [2, 11, 2]]
# todo = ['1']
# stochastic_probabilities = {
#     'as_intended': .2,
#     'slanted': .26666666666666666,
#     'sideways': 0.13333333333333333,
# }



#testcase 3:
w = math.inf
warehouse = ['##.####1',
            '#.......',
            '@.......']
warehouse_cost = [[w, w, 3, w, w, w, w, 12],
                 [w, 8, 10, 2, 10, 4, 15, 8],
                 [15, 10, 10, 10, 7, 10, 2, 10]]
stochastic_probabilities = {
    'as_intended': .70,
    'slanted': .1,
    'sideways': .05,
}
todo = ['1']

#
partC = DeliveryPlanner_PartC(warehouse, warehouse_cost, todo, stochastic_probabilities)
partC.generate_policies(debug=True)

def who_am_i():
    # Please specify your GT login ID in the whoami variable (ex: jsmith124).
    whoami = 'tcheng99'
    return whoami


if __name__ == "__main__":
    """ 
    You may execute this file to develop and test the search algorithm prior to running 
    the delivery planner in the testing suite.  Copy any test cases from the
    testing suite or make up your own.
    Run command:  python warehouse.py
    """

    # Test code in here will NOT be called by the autograder
    # This section is just a provided as a convenience to help in your development/debugging process

    # Testing for Part A
    print('\n~~~ Testing for part A: ~~~\n')

    from testing_suite_partA import wrap_warehouse_object, Counter

    # test case data starts here
    # testcase 1
    warehouse = [
        '######',
        '#....#',
        '#.1#2#',
        '#..#.#',
        '#...@#',
        '######',
    ]
    todo = list('12')
    benchmark_cost = 23
    viewed_cell_count_threshold = 20
    dropzone = (4,4)
    box_locations = {
        '1': (2,2),
        '2': (2,4),
    }
    # test case data ends here

    viewed_cells = Counter()
    warehouse_access = wrap_warehouse_object(warehouse, viewed_cells)
    partA = DeliveryPlanner_PartA(warehouse_access, dropzone, todo, box_locations)
    # partA.plan_delivery(debug=False) ##################Change debug to True when I want to work on part A again
    # Note that the viewed cells for the hard coded solution provided
    # in the initial template code will be 0 because no actual search
    # process took place that accessed the warehouse
    print('Viewed Cells:', len(viewed_cells))
    print('Viewed Cell Count Threshold:', viewed_cell_count_threshold)

    # Testing for Part B
    # testcase 1
    print('\n~~~ Testing for part B: ~~~')
    warehouse = ['1..',
                 '.#.',
                 '..@']

    warehouse_cost = [[3, 5, 2],
                      [10, math.inf, 2],
                      [2, 10, 2]]

    todo = ['1']

    # partB = DeliveryPlanner_PartB(warehouse, warehouse_cost, todo)
    # partB.generate_policies(debug=True)

    # Testing for Part C
    # testcase 1
    print('\n~~~ Testing for part C: ~~~')
    warehouse = ['1..',
                 '.#.',
                 '..@']

    warehouse_cost = [[13, 5, 6],
                      [10, math.inf, 2],
                      [2, 11, 2]]

    todo = ['1']

    stochastic_probabilities = {
        'as_intended': .70,
        'slanted': .1,
        'sideways': .05,
    }

    # partC = DeliveryPlanner_PartC(warehouse, warehouse_cost, todo, stochastic_probabilities)
    # partC.generate_policies(debug=True)
