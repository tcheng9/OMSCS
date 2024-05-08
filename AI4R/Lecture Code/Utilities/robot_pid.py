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

import random
from math import *


class Robot(object):
    def __init__(self, length=20.0):
        """
        Creates robot and initializes location/orientation to 0, 0, 0.
        """
        self.x = 0.0
        self.y = 0.0
        self.orientation = 0.0
        self.length = length
        self.steering_noise = 0.0
        self.distance_noise = 0.0
        self.steering_drift = 0.0

    def set(self, x, y, orientation):
        """
        Sets a robot coordinate.
        """
        self.x = x
        self.y = y
        self.orientation = orientation % (2.0 * pi)

    def set_noise(self, steering_noise, distance_noise):
        """
        Sets the noise parameters.
        """
        # makes it possible to change the noise parameters
        # this is often useful in particle filters
        self.steering_noise = steering_noise
        self.distance_noise = distance_noise

    def set_steering_drift(self, drift):
        """
        Sets the systematical steering drift parameter
        """
        self.steering_drift = drift

    def move(self, steering, distance, tolerance=0.001, max_steering_angle=pi / 4.0):
        """
        steering = front wheel steering angle, limited by max_steering_angle
        distance = total distance driven, most be non-negative
        """
        if steering > max_steering_angle:
            steering = max_steering_angle
        if steering < -max_steering_angle:
            steering = -max_steering_angle
        if distance < 0.0:
            distance = 0.0

        # apply noise
        steering2 = random.gauss(steering, self.steering_noise) #steering angle
        distance2 = random.gauss(distance, self.distance_noise) #forward motion

        # apply steering drift
        steering2 += self.steering_drift

        # TODO: Finish filling in this method using a modified solution code
        #  of Problem Set 3 Question 4 (do NOT return anything for this method)
        # Finish code for this method here! Noise has already been applied above.
        # You just have to write code for executing motion. No need to make a copy
        # of the robot (res), just update self.x, self.y, and self.orientation.
        # turn = tan(steering2) * distance2 / self.length
        # radius =  distance2 / turn
        # cx = self.x - (sin(self.orientation) *radius)
        # cy = self.y - (cos(self.orientation) * radius)
        # self.orientation = (self.orientation + turn)  % (2.0 * pi)
        # self.x = cx + (sin(self.orientation) *radius)
        # self.y = cy - (cos(self.orientation) * radius)


        # self.y = y_new
        # self.x = x_new
        # self.orientation = orientation_new
        # Execute motion here!
        raise NotImplementedError('Student code not implemented (comment out this line when done)')

    def __repr__(self):
        return '[x=%.5f y=%.5f orient=%.5f]' % (self.x, self.y, self.orientation)
