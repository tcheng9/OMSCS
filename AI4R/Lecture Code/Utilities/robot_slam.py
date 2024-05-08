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

from math import *
import random
from heapq import heapify, heappop, heappush

class SLAMRobot:

    # --------
    # init:
    #   creates robot and initializes location to 0, 0
    #

    def __init__(self, world_size=100.0, measurement_range=30.0,
                 motion_noise=1.0, measurement_noise=1.0):
        self.measurement_noise = 0.0
        self.world_size = world_size
        self.measurement_range = measurement_range
        self.x = world_size / 2.0
        self.y = world_size / 2.0
        self.motion_noise = motion_noise
        self.measurement_noise = measurement_noise
        self.landmarks = []
        self.num_landmarks = 0

    def rand(self):
        return random.random() * 2.0 - 1.0

    # --------
    #
    # make random landmarks located in the world
    #

    def make_landmarks(self, num_landmarks):
        self.landmarks = []
        for i in range(num_landmarks):
            self.landmarks.append([round(random.random() * self.world_size),
                                   round(random.random() * self.world_size)])
        self.num_landmarks = num_landmarks

    # --------
    #
    # move: attempts to move robot by dx, dy. If outside world
    #       boundary, then the move does nothing and instead returns failure
    #

    def move(self, dx, dy):

        x = self.x + dx + self.rand() * self.motion_noise
        y = self.y + dy + self.rand() * self.motion_noise

        if x < 0.0 or x > self.world_size or y < 0.0 or y > self.world_size:
            return False
        else:
            self.x = x
            self.y = y
            return True

    # --------
    #
    # sense: returns x- and y- distances to landmarks within visibility range
    #        because not all landmarks may be in this range, the list of measurements
    #        is of variable length. Set measurement_range to -1 if you want all
    #        landmarks to be visible at all times
    #

    def sense(self):
        Z = []
        for i in range(self.num_landmarks):
            dx = self.landmarks[i][0] - self.x + self.rand() * self.measurement_noise
            dy = self.landmarks[i][1] - self.y + self.rand() * self.measurement_noise
            if self.measurement_range < 0.0 or abs(dx) + abs(dy) <= self.measurement_range:
                Z.append([i, dx, dy])
        return Z

    # --------
    #
    # print robot location
    #

    def __repr__(self):
        return 'Robot: [x=%.5f y=%.5f]' % (self.x, self.y)


######################################################

# --------
# this routine makes the robot data
#

def make_data(N, num_landmarks, world_size, measurement_range, motion_noise,
              measurement_noise, distance):
    '''
        :param N: (int) time steps
        :param num_landmarks: (int) number of landmarks
        :param world_size: (float) size of world
        :param measurement_range: (float) range at which we can sense landmarks
        :param motion_noise: (float) noise in robot motion
        :param measurement_noise: (float) noise in the measurements
        :param distance: (float) distance by which robot (intends to) move each
                         iteration
        :returns data: (list) a list of N-1 items.  Each item consists of 2 parts:
                        - Part 1 represents measurement data: list of measurements to landmarks
                            Each measurement contains 3 pieces of data:
                                landmark_id
                                delta_x_distance
                                delta_y_distance
                        - Part 2 represents movement data: list of relative movement distances
                            each movement contains 2 pieces of data:
                                delta_x_distance
                                delta_y_distance
                    Example:
                    data = [
                        [
                            [
                                [landmark_id, delta_x_distance_meas, delta_y_distance_meas],
                                [...]
                            ],
                            [delta_x_distance_move, delta_y_distance_move]
                        ],
                        [...],
                    ]
        '''
    complete = False

    while not complete:

        data = []

        # make robot and landmarks
        r = SLAMRobot(world_size, measurement_range, motion_noise, measurement_noise)
        r.make_landmarks(num_landmarks)
        seen = [False for row in range(num_landmarks)]

        # guess an initial motion
        orientation = random.random() * 2.0 * pi
        dx = cos(orientation) * distance
        dy = sin(orientation) * distance

        for k in range(N - 1):

            # sense
            Z = r.sense()

            # check off all landmarks that were observed
            for i in range(len(Z)):
                seen[Z[i][0]] = True

            # move
            while not r.move(dx, dy):
                # if we'd be leaving the robot world, pick instead a new direction
                orientation = random.random() * 2.0 * pi
                dx = cos(orientation) * distance
                dy = sin(orientation) * distance

            # memorize data
            data.append([Z, [dx, dy]])

        # we are done when all landmarks were observed; otherwise re-run
        complete = (sum(seen) == num_landmarks)

    print(' ')
    print('Landmarks: ', r.landmarks)
    print(r)

    return data

####################################################

# --------------------------------
#
# print the result of SLAM, the robot pose(s) and the landmarks
#

def print_result(N, num_landmarks, result):
    print()
    print ('Estimated Pose(s):')
    for i in range(N):
        print ('    ['+ ', '.join('%.3f'%x for x in result.value[2*i]) + ', ' \
            + ', '.join('%.3f'%x for x in result.value[2*i+1]) +']')
    print()
    print( 'Estimated Landmarks:')
    for i in range(num_landmarks):
        print ('    ['+ ', '.join('%.3f'%x for x in result.value[2*(N+i)]) + ', ' \
            + ', '.join('%.3f'%x for x in result.value[2*(N+i)+1]) +']')

