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

from rait import matrix
from math import *

# KALMAN FILTER LESSON MODULES
print("KALMAN FILTER LESSON MODULES", end="")

# --------------------------------------------------------------------
# 8. MAXIMIZE GAUSSIAN
print("\n8. MAXIMIZE GAUSSIAN")
# For this problem, you aren't writing any code.
# Instead, please just change the last argument
# in f() to maximize the output.


def f(mu, sigma2, x):
    return 1/sqrt(2.*pi*sigma2) * exp(-.5*(x-mu)**2 / sigma2)

    # 1/sqrt(2.*pi*sigma2) * exp(-.5*(x-mu)**2 / sigma2)

print(f(10, 4, 8.))  # TODO: CHANGE/UPDATE CODE HERE (Change the 8. to something else!)

# --------------------------------------------------------------------
# 17. NEW MEAN AND VARIANCE
print("\n17. NEW MEAN AND VARIANCE")
# Write a program to update your mean and variance
# when given the mean and variance of your belief
# and the mean and variance of your measurement.
# This program will update the parameters of your
# belief function.


def update(mean1, var1, mean2, var2):
    new_mean = (var2*mean1 + var1*mean2) / (var1 + var2)  # TODO: CHANGE/UPDATE CODE HERE
    new_var = 1 / (1/var1 + 1/var2)

    return [new_mean, new_var]


print(update(10, 8, 13, 2))

# --------------------------------------------------------------------
# 19. PREDICT FUNCTION
print("\n19. PREDICT FUNCTION")
# Write a program that will predict your new mean
# and variance given the mean and variance of your
# prior belief and the mean and variance of your
# motion.


def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2  # TODO: CHANGE/UPDATE CODE HERE
    new_var = var1 + var2
    return [new_mean, new_var]


print(predict(10, 4, 12, 4))

# --------------------------------------------------------------------
# 20. KALMAN FILTER CODE
print("\n20. KALMAN FILTER CODE")
# Write a program that will iteratively update and
# predict based on the location measurements
# and inferred motions shown below.

measurements = [5, 6, 7, 9, 10]
motion = [1, 1, 2, 1, 1]
measurement_sig = 4
motion_sig = 2
mu = 0
sig = 10000  # Changed throughout answer video:  1000, 0.000000001

# Please print out ONLY the final values of the mean
# and the variance in a list [mu, sig].

# TODO: ADD CODE HERE

print([mu, sig])

# --------------------------------------------------------------------
# 27. KALMAN MATRICES
print("\n27. KALMAN MATRICES")
# Write a function 'kalman_filter' that implements a multi-
# dimensional Kalman Filter for the example given
'''
# #1D solution
x = matrix([[0], [0]])
P = matrix([[1000, 0], [0,1000]])
u = matrix([[0], [0]])
F = matrix([[1,1], [0,1]])
H = matrix([[1, 0]])
R = matrix([[1]])
I = matrix([[1,0], [0,1]])
def kalman_filter(x, P):
    for n in range(len(measurements)):
        # TODO: ADD CODE HERE
        # measurement update
        Z = matrix([[measurements[n]]])

        y = Z - (H*x)

        S = H * P * H.transpose() + R

        K = P * H.transpose() * S.inverse()

        x = x + (K * y)

        P = (I - (K * H)) * P

        # prediction
        x = (F*x) + u
        P = F * P * F.transpose()

        print('x = ')
        x.show()

        print('P = ')
        P.show()
    return x, P
'''
###########################3
#4D solution
##################
'''
dt = .1
x = matrix([
    [1],[1], [1], [1]
    ])
P = matrix([[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 1000, 0],
                [0, 0, 0, 1000]])

u = matrix([[0], [0], [0], [0]])
F = matrix([[1, 0, dt, 0],
      [0, 1, 0, dt],
      [0, 0, 1, 0],
      [0, 0, 0, 1]])
H = matrix([[1, 0, 0, 0],
                [0, 1, 0, 0]])
R = matrix([[.1, 0],
                [0,.1]])
I = matrix([[1, 0, 0, 0],
              [0, 1, 0, 0],
              [0, 0, 1, 0],
              [0, 0, 0, 1]])
def kalman_filter(x, P):
    for n in range(len(measurements)):
        # TODO: ADD CODE HERE
        # measurement update
        x_obs,y_obs = measurements[n]

        Z = matrix([[x_obs] ,[y_obs]])

        y = Z - (H*x)

        S = H * P * H.transpose() + R

        K = P * H.transpose() * S.inverse()

        x = x + (K * y)

        P = (I - (K * H)) * P

        # prediction
        x = (F*x) + u
        P = F * P * F.transpose()

        print('x = ')
        x.show()

        print('P = ')
        P.show()
    return x, P
'''
#########################################
####6D solution
#########################################
dt = .1
x = matrix([
    [1],[1], [1], [1], [1],[1]
    ])
P = matrix([[1, 0, 0, 0, 0,0],
            [0,1, 0, 0, 0, 0],
            [0, 0, 1000, 0, 0, 0],
            [0, 0, 0, 1000, 0, 0],
            [0, 0, 0, 0, 1000, 0],
            [0, 0, 0, 0, 0, 1000]
            ])

u = matrix([[0], [0], [0], [0], [0], [0]])
F = matrix([
        [1, 0, dt, 0, 1,0],
        [0, 1, 0, dt, 1,0],
        [0, 0, 1, 0, 1,0],
        [0, 0, 1, 0, 1,0],
        [0, 0, 1, 0, 1,0],
        [0, 0, 1, 0, 1,0],
    ])
H = matrix([[1, 0, 0, 0, 0,0],
                [0, 1, 0, 0, 0,0]])
R = matrix([[.1, 0],
                [0,.1]])
I = matrix([[1, 0, 0, 0, 0,0],
            [0, 1, 0, 0, 0,0],
            [0, 0, 1, 0, 0,0],
            [0, 0, 0, 1,0,0],
            [0, 0, 0, 1,0,0],
            [0, 0, 0, 1,0,0]
            ])

def kalman_filter(x, P):
    for n in range(len(measurements)):
        # TODO: ADD CODE HERE
        # measurement update
        x_obs,y_obs = measurements[n]

        Z = matrix([[x_obs] ,[y_obs]])

        y = Z - (H*x)

        S = H * P * H.transpose() + R

        K = P * H.transpose() * S.inverse()

        x = x + (K * y)



        P = (I - (K * H)) * P

        # prediction
        x = (F*x) + u

        P = F * P * F.transpose()
        print('end of check')
        print('x = ')
        x.show()

        print('P = ')
        P.show()
    return x, P

# use the code below to test your filter!

measurements = [[1,1], [2,10], [3,100]]


# Matrices_P =  ([[0, 0, 0, 0],
#                 [0, 0, 0, 0],
#                 [0, 0, 1000, 0],
#                 [0, 0, 0, 1000]])
#
# Matrices_F  =  ([[1, 0,.1, 0],
#                  [0, 1, 0, .1],
#                  [0, 0, 1, 0],
#                  [0, 0, 0, 1]])
#
# Matrices_H =  ([[1, 0, 0, 0],
#                 [0, 1, 0, 0]])
# # H matrix only wants X and Y, not x_vel, y_vel. Purpose: Shrinks down matrices, (In this case: 4D -> 2D)
# Matrices_R =  ([[.1, 0],
#                 [0,.1]])
#
# Matrices_I = ([[1, 0, 0, 0],
#               [0, 1, 0, 0],
#               [0, 0, 1, 0],
#               [0, 0, 0, 1]])

x, P = kalman_filter(x, P)
print('x:')
x.show()
print('P:')
P.show()
# output should be:
# x: [[3.9996664447958645], [0.9999998335552873]]
# P: [[2.3318904241194827, 0.9991676099921091], [0.9991676099921067, 0.49950058263974184]]
