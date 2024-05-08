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

"""
 === Introduction ===

   The assignment is broken up into two parts.

   Part A:
        Create a SLAM implementation to process a series of landmark measurements (location of tree centers) and movement updates.
        The movements are defined for you so there are no decisions for you to make, you simply process the movements
        given to you.
        Hint: A planner with an unknown number of motions works well with an online version of SLAM.

    Part B:
        Here you will create the action planner for the drone.  The returned actions will be executed with the goal being to navigate to 
        and extract the treasure from the environment marked by * while avoiding obstacles (trees). 
        Actions:
            'move distance steering'
            'extract treasure_type x_coordinate y_coordinate' 
        Example Actions:
            'move 1 1.570963'
            'extract * 1.5 -0.2'

    Note: All of your estimates should be given relative to your drone's starting location.

    Details:
    - Start position
      - The drone will land at an unknown location on the map, however, you can represent this starting location
        as (0,0), so all future drone location estimates will be relative to this starting location.
    - Measurements
      - Measurements will come from trees located throughout the terrain.
        * The format is {'landmark id':{'distance':0.0, 'bearing':0.0, 'type':'D', 'radius':0.5}, ...}
      - Only trees that are within the horizon distance will return measurements. Therefore new trees may appear as you move through the environment.
    - Movements
      - Action: 'move 1.0 1.570963'
        * The drone will turn counterclockwise 90 degrees [1.57 radians] first and then move 1.0 meter forward.
      - Movements are stochastic due to, well, it being a robot.
      - If max distance or steering is exceeded, the drone will not move.
      - Action: 'extract * 1.5 -0.2'
        * The drone will attempt to extract the specified treasure (*) from the current location of the drone (1.5, -0.2).
      - The drone must be within 0.25 distance to successfully extract a treasure.

    The drone will always execute a measurement first, followed by an action.
    The drone will have a time limit of 10 seconds to find and extract all of the needed treasures.
"""

from typing import Dict, List
from rait import matrix
from drone import Drone
from math import *
from copy import deepcopy
from time import *
# If you see different scores locally and on Gradescope this may be an indication
# that you are uploading a different file than the one you are executing locally.
# If this local ID doesn't match the ID on Gradescope then you uploaded a different file.
OUTPUT_UNIQUE_FILE_ID = False
if OUTPUT_UNIQUE_FILE_ID:
    import hashlib, pathlib

    file_hash = hashlib.md5(pathlib.Path(__file__).read_bytes()).hexdigest()
    print(f'Unique file ID: {file_hash}')


class SLAM:
    """Create a basic SLAM module.
    """

    def __init__(self):
        """Initialize SLAM components here.
        """
        # TODO
        self.omega = matrix([[1.0, 0.0], [0.0, 1.0]])
        self.xi = matrix([[0.0], [0.0]])
        self.drone = Drone()
        self.orientation = 0 * pi

        self.x = 0
        self.y = 0
        self.locations = {
            'self': (self.x, self.y),  # This dict will contains the actual location of drone and landmarks

        }
        self.mu = matrix()
        self.steering = 0
        self.matrix_tracker = {}  # This dict will contain the row/col for drone/landmarks in the omega/xi matrix

    # Provided Functions
    def get_coordinates(self):
        """
        Retrieves the estimated (x, y) locations in meters of the drone and all landmarks (trees) when called.

        Args: None

        Returns:
            The (x,y) coordinates in meters of the drone and all landmarks (trees) in the format:
                    {
                        'self': (x, y),
                        '<landmark_id_1>': (x1, y1),
                        '<landmark_id_2>': (x2, y2),
                        ....
                    }
        """

        # print(self.locations)

        return self.locations

    def process_measurements(self, measurements: Dict):
        """
        Process a new series of measurements and update (x,y) location of drone and landmarks

        Args:
            measurements: Collection of measurements of tree positions and radius
                in the format {'landmark id':{'distance': float <meters>, 'bearing':float <radians>, 'type': char, 'radius':float <meters>}, ...}

        """

        # setting up local versions of self properties so i don't have to keep typing self
        matrix_tracker = self.matrix_tracker
        xi = self.xi
        omega = self.omega

        # Step 1 - Expand matrices THEN add to matrix tracker to track rows/col
        for key, val in measurements.items():
            landmark_id = measurements[key]['type']  # sub this out if I want to use names instead of IDs
            # I think you use IDs for internal logic, 'type'/actual name for return dictioanry
            if key not in matrix_tracker:
                # Expanding omega and xi
                new_lx = omega.dimx + 1
                new_ly = omega.dimx + 2
                omega = omega.expand(omega.dimx + 2, omega.dimy + 2, list(range(omega.dimx)), list(range(omega.dimy)))
                xi = xi.expand(xi.dimx + 2, xi.dimy, list(range(xi.dimx)), list(range(xi.dimy)))
                matrix_tracker[key] = (
                new_lx, new_ly)  # placeholder row/col tracker #NOTTTTTTTTTTTTT ACTUAL Landmark XY positions.

        # Print statements
        # print(matrix_tracker)
        # omega.show()
        # xi.show()

        # hyperparameter
        measurement_noise = 0.05

        for key in measurements.keys():
            # Step 2 -calc theta, delta_x, delta_y
            theta = self.orientation + measurements[key]['bearing']
            dx = cos(theta) * measurements[key]['distance']
            dy = sin(theta) * measurements[key]['distance']

            # Updating omega and theta
            delta = [dx, dy]
            landmark = matrix_tracker[key]

            for i in range(2):
                # Updating omega
                # #main diagonal
                omega.value[i][i] += 1.0 / measurement_noise
                omega.value[landmark[i] - 1][landmark[i] - 1] += 1.0 / measurement_noise
                # #crossdiagonal
                omega.value[i][landmark[i] - 1] += -1.0 / measurement_noise
                omega.value[landmark[i] - 1][i] += -1.0 / measurement_noise

                # Updating xi
                xi.value[i][0] += -delta[i] / measurement_noise
                xi.value[landmark[i] - 1][0] += delta[i] / measurement_noise

        # Step 3.5 - updating object's omega, xi AND calculating mu -> just a checkpoint step
        self.omega = omega
        self.xi = xi
        # omega.show()
        # xi.show()
        # self.omega.show()
        # self.xi.show()
        mu = self.omega.inverse() * self.xi

        # Step 4 - extract values from mu and actually build it into a return dictionary
        locations = self.locations
        # updating x,y via updated mu
        locations['self'] = (mu[0][0], mu[1][0])

        # print(mu)
        # updating landmarks via updated mu
        for key in measurements.keys():
            name = measurements[key]['type']
            landmark_x_row, landmark_y_row = matrix_tracker[key]
            # print(name)
            # print(landmark_x_row, landmark_y_row)

            locations[key] = (mu[landmark_x_row - 1][0], mu[landmark_y_row - 1][0])
            # print(locations)

        # updating object's omega, xi AND calculating mu
        self.omega = omega
        self.xi = xi
        self.mu = mu
        self.locations = locations

        # TODO:
        # print('measurements are', measurements)
        # print(measurements)
        # return {}

    def process_movement(self, distance: float, steering: float):
        """
        Process a new movement and update (x,y) location of drone

        Args:
            distance: distance to move in meters
            steering: amount to turn in radians
        """
        xi = self.xi
        omega = self.omega
        # updating orientation first THEN calc new x, y

        self.orientation = self.orientation + steering
        dx = (cos(self.orientation) * distance)
        dy = (sin(self.orientation) * distance)
        self.x = self.x + dx
        self.y = self.y + dy
        self.locations['self'] = (self.x, self.y)

        idxs = [0, 1] + list(range(4, omega.dimx + 2))
        omega = omega.expand(omega.dimx + 2, omega.dimy + 2, idxs, idxs)

        # omega.show()
        # update xi size

        xi = xi.expand(xi.dimx + 2, 1, idxs, [0])
        # xi.show()

        ###Step C -> updating omega/xi
        motion_noise = 0.05
        for b in range(4):
            omega.value[b][b] += 1.0 / motion_noise

        motion = [dx, dy]
        for b in range(2):
            omega.value[b][b + 2] += -1.0 / motion_noise
            omega.value[b + 2][b] += -1.0 / motion_noise
            xi[b][0] += -motion[b] / motion_noise
            xi[b + 2][0] += motion[b] / motion_noise

        # Step D: extracting a,b,c
        newidxs = list(range(2, len(omega.value)))
        a = omega.take([0, 1], newidxs)
        b = omega.take([0, 1])  # symetrical because it takes the rows and uses as col when col paramter is empty
        c = xi.take([0, 1], [0])

        omega = omega.take(newidxs) - a.transpose() * b.inverse() * a
        xi = xi.take(newidxs, [0]) - a.transpose() * b.inverse() * c
        # LEAVE THIS AT THE END  -> updating this functions local xi/omega to be the global xi/omega
        # doing this to avoid typing self.omega, self.xi constantly
        # print('self.omega/xi at the end of fn')

        self.omega = omega
        self.xi = xi

        # self.mu = self.omega.inverse() * self.xi
        # # mu.show()
        # self.x = self.mu[0][0]
        # self.y = self.mu[1][0]
        # self.locations['self'] = (self.x, self.y)
        # self.mu.show()


#
# test = SLAM()
# test.get_coordinates()
# test.process_movement(5, 2)
# measurements = {282589425900826719688085225668504563362: {'distance': 2.986106590746365, 'bearing': 1.5790924612915944, 'type': 'B',
#                                            'radius': 0.2},
#  148224656581792672884491322522799971648: {'distance': 2.932896779434399, 'bearing': -3.120182127536145, 'type': 'A',
#                                            'radius': 0.5},
#  137551100291914355458239239134341445524: {'distance': 3.934359688171381, 'bearing': -0.01661414864955102, 'type': 'C',
#                                            'radius': 0.3}}
# test.process_measurements(measurements)
class IndianaDronesPlanner:
    """
    Create a planner to navigate the drone to reach and extract the treasure marked by * from an unknown start position while avoiding obstacles (trees).
    """

    def __init__(self, max_distance: float, max_steering: float):
        """
        Initialize your planner here.

        Args:
            max_distance: the max distance the drone can travel in a single move in meters.
            max_steering: the max steering angle the drone can turn in a single move in radians.
        """
        # TODO
        # self.x = 0
        # self.y = 0
        # self.locations = {
        #     'self': (self.x, self.y)
        # }
        # print('max_distance', max_distance)
        # print('max_steering is', max_steering)
        self.max_distance = max_distance
        self.max_steering = max_steering
        self.drone = SLAM()
        # print(self.drone)

    def compute_distance(self, p: tuple, q: tuple):
        """Compute the distance between two points.

        Args:
            p: Point 1
            q: Point 2

        Returns:
            The Euclidean distance between the points.
        """

        x1, y1 = p
        x2, y2 = q

        dx = x2 - x1
        dy = y2 - y1

        return sqrt(dx ** 2 + dy ** 2)

    def truncate_angle(self, t: float):
        """
        Truncate the angle between -PI and PI

        Args:
            t: angle to truncate.

        Returns:
            Truncated angle.
        """
        return ((t + pi) % (2 * pi)) - pi

    def compute_bearing(self, p: tuple, q: tuple):
        """
        Compute bearing between two points.

        Args:
            p: Point 1
            q: Point 2

        Returns:
            The bearing as referenced from the horizontal axis.
        """
        x1, y1 = p
        x2, y2 = q

        dx = x2 - x1
        dy = y2 - y1

        return atan2(dy, dx)

    ### Beginning of Code citation
    # This code is from the testing_suite_indiana_drones.py file

    def line_circle_intersect(self, first_point, second_point, origin, radius):
        """ Checks if a line segment between two points intersects a circle of a certain radius and origin

        Args:
            first_point : (x,y)
            second_point : (x,y)
            origin : (x,y)
            radius : r

        Returns:
            intersect : True/False

        """

        ###REFERENCE###

        # https://math.stackexchange.com/questions/275529/check-if-line-intersects-with-circles-perimeter
        x1, y1 = first_point
        x2, y2 = second_point

        ox, oy = origin
        r = radius
        x1 -= ox
        y1 -= oy
        x2 -= ox
        y2 -= oy
        a = (x2 - x1) ** 2 + (y2 - y1) ** 2
        b = 2 * (x1 * (x2 - x1) + y1 * (y2 - y1))
        c = x1 ** 2 + y1 ** 2 - r ** 2
        disc = b ** 2 - 4 * a * c

        if a == 0:
            if c <= 0:
                return True
            else:
                return False
        else:

            if (disc <= 0):
                return False
            sqrtdisc = sqrt(disc)
            t1 = (-b + sqrtdisc) / (2 * a)
            t2 = (-b - sqrtdisc) / (2 * a)
            if ((0 < t1 and t1 < 1) or (0 < t2 and t2 < 1)):
                return True
            return False

        # end of code citation

    def crash_check(self, measurements, locations, x,y, hx, hy):
        crash = False
        for key in measurements:
            cx, cy = locations[key]  # center of circle
            r = measurements[key]['radius']  # radius
            val = self.line_circle_intersect((x, y), (hx, hy), (cx, cy), r+.20)
            type = measurements[key]['type']

            if val:
                # print('crash with ', type)
                crash = True
        return crash

    def next_move(self, measurements: Dict, treasure_location: Dict):
        """Next move based on the current set of measurements.

        Args:
            measurements: Collection of measurements of tree positions and radius in the format
                          {'landmark id':{'distance': float <meters>, 'bearing':float <radians>, 'type': char, 'radius':float <meters>}, ...}
            treasure_location: Location of Treasure in the format {'x': float <meters>, 'y':float <meters>, 'type': char '*'}

        Return: action: str, points_to_plot: dict [optional]
            action (str): next command to execute on the drone.
                allowed:
                    'move distance steering'
                    'move 1.0 1.570963'  - Turn left 90 degrees and move 1.0 distance.

                    'extract treasure_type x_coordinate y_coordinate'
                    'extract * 1.5 -0.2' - Attempt to extract the treasure * from your current location (x = 1.5, y = -0.2).
                                           This will succeed if the specified treasure is within the minimum sample distance.

            points_to_plot (dict): point estimates (x,y) to visualize if using the visualization tool [optional]
                            'self' represents the drone estimated position
                            <landmark_id> represents the estimated position for a certain landmark
                format:
                    {
                        'self': (x, y),
                        '<landmark_id_1>': (x1, y1),
                        '<landmark_id_2>': (x2, y2),
                        ....
                    }
        """

        locations = self.drone.get_coordinates()
        x,y = locations['self']
        tx, ty = treasure_location['x'], treasure_location['y']
        self.drone.process_measurements(measurements)
        # print('measurements are', measurements)
        #Part C - If you are close enough to treasure, start honing in
        ed = self.compute_distance((x,y), (tx, ty))
        # print('ed is', ed)

        if ed < 1.0:
            bearing = self.compute_bearing((x, y), (tx, ty))
            steering = bearing - self.drone.orientation
            steering = self.truncate_angle(steering)

            # Truncation fix when close to 0.0 and 3.14 radinas
            if steering > self.max_steering:
                steering = self.max_steering - 0.25

            if steering < -self.max_steering:
                steering = -self.max_steering + 0.25


            if -0.01 < steering <0:
                steering = -0.01

            if 0 <= steering < 0.1:
                steering = 0.01



            dist_adj = [.01, .02, .03, .04, .05, .06, .07, .08, .09, .1]
            best_ed = self.compute_distance((x, y), (tx, ty))

            for i in range(len(dist_adj)):
                '''
                Slowly increment distance assuming i'm using the best steering and test if it crashes
                '''
                test_dist = 0
                test_orientation = self.drone.orientation + steering
                test_dist += dist_adj[i]
                hx = x + (cos(test_orientation) * test_dist)
                hy = y + (sin(test_orientation) * test_dist)
                crashed_flag = self.crash_check(measurements, locations, x, y, hx, hy)
                curr_ed = self.compute_distance((hx, hy), (tx, ty))
                if crashed_flag:
                    continue
                else:
                    if curr_ed < best_ed:
                        test_dist = dist_adj[i]

            # print('steering is', steering)
            # print('dist is ', test_dist)
            # print('max dist is', self.max_distance)
            # print('max steering is', self.max_steering)
            if ed < 0.20:
                print('ed is', ed)
                # print('extract * ' + str(x) + ' ' + str(y))
                res = 'extract ' + '*' + ' ' + str(x) + ' ' + str(y)
                print('res is', res)
                return res, self.drone.get_coordinates()
            str_res = 'move ' + str(test_dist) + ' ' + str(steering)
            self.drone.process_movement(test_dist, steering)
            # print('under 1 ed')
            return str_res, self.drone.get_coordinates()








        # Part A - Calc the default of going straight to treasure and seeing if its safe
        # Computing bearing and correct steering/orientation to treasure
        bearing = self.compute_bearing((x, y), (tx, ty))
        steering = bearing - self.drone.orientation
        steering = self.truncate_angle(steering)

        # Truncation fix when close to 0.0 and 3.14 radinas
        if steering > self.max_steering:
            steering = self.max_steering - 0.25

        if steering < -self.max_steering:
            steering = -self.max_steering + 0.25

        test_dist = self.max_distance
        test_orientation = self.drone.orientation + steering


        #computing val
        hx = x + (cos(test_orientation) * test_dist)
        hy  = y + (sin(test_orientation) * test_dist)

        hyp_ed = self.compute_distance((hx, hy), (tx, ty))


        #initial check of going to treasure is safe
        crashed_flag = self.crash_check(measurements, locations, x,y, hx, hy)

        #Base case, if going straight is safe , just retunr thatv value
        if crashed_flag == False:
            ############################################################3
            #Return case
            #########################################################
            print('base case steering is', steering)

            if steering < -self.max_steering:
                steering = -self.max_steering + .25
            if steering > self.max_steering:
                steering = self.max_steering - .25
            str_res = 'move ' + str(test_dist) + ' ' + str(steering)
            self.drone.process_movement(test_dist, steering)
            print('chose striaght')
            return str_res, self.drone.get_coordinates()


        '''Part A end ---------------------------------'''

        '''
        Part B: If you crashed, adjust orientation/dist until your first fix for it
        '''

        steering_adj = [.05, .1, .15, .2, .25, .3, .35, .4, .45, .5, .55, .6, .65, .7, .75]
        dist_adj = [.05, .1, .15, .2, .25, .3, .35, .4, .45, .5, .55, .6, .65, .7, .75]


        '''
        Strategy for best adjustment - adjust steering and dist until. Save the parameters that give you the min ED without crashing
        
        Note: always print steering and orientation to figure out max_steering error
        '''

        best_ed = self.compute_distance((x,y), (tx, ty))
        best_steering = 0
        best_dist = self.max_distance
        print('drones distance to treasure')

        for i in range(len(steering_adj)):
            for j in range(len(dist_adj)):

                '''
                calculating updated orientation, x,y
                '''
                bearing = self.compute_bearing((x, y), (tx, ty))
                steering = bearing - self.drone.orientation
                steering = self.truncate_angle(steering)

                if steering < 0:
                    steering = steering + (-1 * steering_adj[i])
                    steering = self.truncate_angle(steering)
                else:
                    steering = steering + steering_adj[i]
                    steering = self.truncate_angle(steering)
                test_dist = 1 - dist_adj[j]
                test_orientation = self.drone.orientation + steering
                # print('adjusted steering is', steering)
                #
                # print('chosen orientation is', test_orientation)
                # print('max_steering is', max_steering)
                #
                # print('-')
                # print('max distance is', max_distance)
                # print('chosen dist is', test_dist)

                hx = x + (cos(test_orientation) * test_dist)
                hy = y + (sin(test_orientation) * test_dist)

                ##Euclidean distance to treasure
                ed = self.compute_distance((hx, hy), (tx, ty))
                crash = self.crash_check(measurements, locations, x,y, hx, hy)

                # print('crash status is', crash)
                if crash:
                    continue
                else:
                    if ed < best_ed:
                        best_ed = ed
                        best_steering = steering
                        best_dist = test_dist

                #print(crash)

        # sleep(1)

        print('best dist is', best_dist)
        print('best steering is', best_steering)
        if best_steering < -self.max_steering:
            best_steering = -self.max_steering + .1

        if best_steering > self.max_steering:
            best_steering = self.max_steering - .1
        str_res = 'move ' + str(best_dist) + ' ' + str(best_steering)
        self.drone.process_movement(best_dist, best_steering)

        return str_res, self.drone.get_coordinates()












        print('--------------------------------------------------------------')
        #
        # str_res = 'move ' + str(test_dist) + ' ' + str(steering)
        # self.drone.process_movement(test_dist, steering)
        #
        # return str_res, self.drone.get_coordinates()


# max_dist = 1.8
# max_steering = 1.5807963267948966
# test2 = IndianaDronesPlanner(max_dist, max_steering)
# treasure_location = {'type': '*', 'x': 0.0, 'y': 5.0}
# measurements = {257812140632085890620834044694192037619: {'distance': 2.987337003560054, 'bearing': 1.555662221186565, 'type': 'B', 'radius': 0.5}, 301535294639192173618660412099336083906: {'distance': 2.082765320204951, 'bearing': 2.6513128345780235, 'type': 'A', 'radius': 0.5}, 35965569574824054224629799135315165772: {'distance': 2.2879079829557685, 'bearing': 0.49017992848658887, 'type': 'C', 'radius': 0.3}}
#
#
#
# test2.next_move(measurements, treasure_location)
def who_am_i():
    # Please specify your GT login ID in the whoami variable (ex: jsmith124).
    whoami = 'tcheng99'
    return whoami


'''



        locations = self.drone.get_coordinates()
        x, y = locations['self']
        tx, ty = treasure_location['x'], treasure_location['y']
        self.drone.process_measurements(measurements)
        
        # Computing bearing and correct steering/orientation to treasure
        bearing = self.compute_bearing((x, y), (tx, ty))
        steering = bearing - self.drone.orientation
        steering = self.truncate_angle(steering)

        # Truncation fix when close to 0.0 and 3.14 radinas
        if steering > self.max_steering:
            steering = self.max_steering - 0.25

        if steering < -self.max_steering:
            steering = -self.max_steering + 0.25

        #########################Crash testing:
        # hypothetical update
        test_dist = 1
        test_orientation = self.drone.orientation + steering
        # x1,y1 - potential dx, dy for drone
        x1 = x + (cos(test_orientation) * test_dist)
        y1 = y + (sin(test_orientation) * test_dist)

        ed = self.compute_distance((x1, y1), (tx, ty))

        for key in measurements:
            x2, y2 = locations[key]  # Tree
            cx, cy = locations[key]  # center of circle
            r = measurements[key]['radius']  # radius

            type = measurements[key]['type']
            val = self.line_circle_intersect((x1, y1), (x2, y2), (cx, cy), r)
            # print('crash value is  - if true that means its safe', val)
            orientation_adj = [.05, .1, .15, .2, .25, .3, .35, .4, .45, .5, .55, .6, .65, .7, .75, .8, .85, .9, .95, 1]
            # orientation_adj = [.1, .2, .3, .4,.5, .6, .7, .8, .9, 1, 1.25, 1.5]
v
            if val == False:
                crash_flag = True  # True = crash, False= safe
                counter = 0
                while crash_flag:
                    print(orientation_adj[counter])
                    if steering < 0:

                        steering = steering + (-1 * orientation_adj[counter])
                        steering = self.truncate_angle(steering)

                    else:
                        steering = steering -
                        orientation_adj[counter]
                        steering = self.truncate_angle(steering)
                    print('counter is ', counter)
                    print('steering is', steering)

                    test_dist -= orientation_adj[
                        counter]  # This works because it's just an incremeent that i'm adding/subtracting
                    test_orientation = self.drone.orientation + steering
                    # x1,y1 - potential dx, dy for drone
                    x1 = x + (cos(test_orientation) * test_dist)
                    y1 = y + (sin(test_orientation) * test_dist)
                    all_3_trees_safe_check = True  # True means all 3 are safe, false = not safe
                    for key in measurements:
                        x2, y2 = locations[key]  # Tree
                        cx, cy = locations[key]  # center of circle
                        r = measurements[key]['radius']  # radius

                        type = measurements[key]['type']
                        val2 = self.line_circle_intersect((x1, y1), (x2, y2), (cx, cy), r)

                        if not val2:
                            all_3_trees_safe_check = False

                    if all_3_trees_safe_check == True:
                        crash_flag = False
                    counter += 1
                    if counter >= 9:
                        counter = 0

            ed = self.compute_distance((x1, y1), (tx, ty))
            if ed < 0.2:
                print('CLOSE ENOUGH TO TARGET')

            # if not val:
            #     print('will crashed with ', type)
            #     # safe_movement = False
            # if val:
            #     print('will be safe with', type)
            #     # safe_movement = True

        str_res = 'move ' + str(.5) + ' ' + str(steering)
        self.drone.process_movement(.5, steering)

        return str_res, self.drone.get_coordinates()
'''