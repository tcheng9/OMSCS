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

# LOCALIZATION LESSON MODULES
print("LOCALIZATION LESSON MODULES", end="")

# --------------------------------------------------------------------
# 6. UNIFORM DISTRIBUTION
print("\n6. UNIFORM DISTRIBUTION")
# Modify the empty list, p, so that it becomes a UNIFORM probability
# distribution over five grid cells, as expressed in a list of
# five probabilities.

p = []  # TODO: CHANGE/UPDATE CODE HERE

print(p)

# --------------------------------------------------------------------
# 7. GENERALIZED UNIFORM DISTRIBUTION
print("\n7. GENERALIZED UNIFORM DISTRIBUTION")
# Modify your code to create probability vectors, p, of arbitrary
# size, n. Use n=5 to verify that your new solution matches
# the previous one.

p = []
n = 5
# TODO: ADD CODE HERE

print(p)

# --------------------------------------------------------------------
# 11. PHIT AND PMISS
print("\n11. PHIT AND PMISS")
# Write code that outputs p after multiplying each entry
# by pHit or pMiss at the appropriate places. Remember that
# the red cells 1 and 2 are hits and the other green cells
# are misses.
# Reminder, we're looking for: [miss, hit, hit, miss, miss]

p = [0.2, 0.2, 0.2, 0.2, 0.2]
pHit = 0.6
pMiss = 0.2

# TODO:  ADD CODE HERE

print(p)

# --------------------------------------------------------------------
# 12. SUM OF PROBABILITIES
print("\n12. SUM OF PROBABILITIES")
# Modify the program to find and print the sum of all
# the entries in the list p.

# TODO:  ADD CODE HERE
print(p)

# --------------------------------------------------------------------
# 13. SENSE FUNCTION
print("\n13. SENSE FUNCTION")
# Modify the code below so that the function sense, which
# takes p and Z as inputs, will output the NON-normalized
# probability distribution, q, after multiplying the entries
# in p by pHit or pMiss according to the color in the
# corresponding cell in world.

p = [0.2, 0.2, 0.2, 0.2, 0.2]
world = ['green', 'red', 'red', 'green', 'green']
Z = 'red'
pHit = 0.6
pMiss = 0.2


def sense(p, Z):
    q = None
    # TODO:  ADD CODE HERE
    return q


print(sense(p, Z))

# --------------------------------------------------------------------
# 14. NORMALIZED SENSE FUNCTION
print("\n14. NORMALIZED SENSE FUNCTION")
# Modify your code so that it normalizes the output for
# the function sense. This means that the entries in q
# should sum to one.


def sense(p, Z):
    q = None
    # Copy and paste your solution code from previous exercise (#13)
    # TODO: ADD CODE HERE
    return q


print(sense(p, Z))

# --------------------------------------------------------------------
# 15. TEST SENSE FUNCTION
print("\n15. TEST SENSE FUNCTION")
# Try using your code with a measurement of 'green' and
# make sure the resulting probability distribution is correct.

p = [0.2, 0.2, 0.2, 0.2, 0.2]
world = ['green', 'red', 'red', 'green', 'green']
Z = 'red'  # TODO: CHANGE/UPDATE CODE HERE
pHit = 0.6
pMiss = 0.2


# You are using the 'sense' function from the previous exercise (#14)

print(sense(p, Z))

# --------------------------------------------------------------------
# 16. MULTIPLE MEASUREMENTS
print("\n16. MULTIPLE MEASUREMENTS")
# Modify the code so that it updates the probability twice
# and gives the posterior distribution after both
# measurements are incorporated. Make sure that your code
# allows for any sequence of measurement of any length.
# Do not modify the sense function. Add code so that p is the correct
# probability after making the two measurements. Make sure your code works for
# measurement lists of arbitrary length.

p = [0.2, 0.2, 0.2, 0.2, 0.2]
world = ['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2

# You are using the 'sense' function from the previous exercise (#14)

#
# TODO: ADD CODE HERE
#


print(p)

# --------------------------------------------------------------------
# 19. MOVE FUNCTION
print("\n19. MOVE FUNCTION")
# Program a function that returns a new distribution
# q, shifted to the right by U units. If U=0, q should
# be the same as p.

p = [0, 1, 0, 0, 0]
world = ['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2


def move(p, U):
    q = None
    #
    # TODO: ADD CODE HERE
    #
    return q


print(move(p, 1))

# --------------------------------------------------------------------
# 23. INEXACT MOVE FUNCTION
print("\n23. INEXACT MOVE FUNCTION")
# Modify the move function to accommodate the added
# probabilities of overshooting or undershooting
# the intended destination.

p = [0, 1, 0, 0, 0]
world = ['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1


def move(p, U):
    q = None
    # Copy and paste your solution code from previous exercise (#19)
    # TODO: ADD CODE HERE
    return q


print(move(p, 1))

# --------------------------------------------------------------------
# 25. MOVE TWICE
print("\n25. MOVE TWICE")
# Write code that makes the robot move twice and then prints
# out the resulting distribution, starting with the initial
# distribution p = [0, 1, 0, 0, 0]

p = [0, 1, 0, 0, 0]
world = ['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1


# You are using the 'move' function from the previous exercise (#23)

#
# TODO: ADD CODE HERE
#

print(p)

# --------------------------------------------------------------------
# 26. MOVE 1000
print("\n26. MOVE 1000")
# Write code that moves 1000 times and then prints the
# resulting probability distribution.

p = [0, 1, 0, 0, 0]
world = ['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1


# You are using the 'move' function from the previous exercise (#23)

#
# TODO: ADD CODE HERE
#

print(p)

# --------------------------------------------------------------------
# 27. SENSE AND MOVE
print("\n27. SENSE AND MOVE")

# Given the list motions=[1,1] which means the robot
# moves right and then right again, compute the posterior
# distribution if the robot first senses red, then moves
# right one, then senses green, then moves right again,
# starting with a uniform prior distribution.

'''Clarification Regarding Entropy

The video mentions that entropy will decrease after the motion update step and
that entropy will increase after measurement step. What is meant is that that
entropy will decrease after the measurement update (sense) step and that
entropy will increase after the movement step (move). In general, entropy
represents the amount of uncertainty in a system. Since the measurement update
step decreases uncertainty, entropy will decrease. The movement step increases
uncertainty, so entropy will increase after this step. Let's look at our
current example where the robot could be at one of five different positions.
The maximum uncertainty occurs when all positions have equal probabilities
[0.2,0.2,0.2,0.2,0.2][0.2, 0.2, 0.2, 0.2, 0.2][0.2,0.2,0.2,0.2,0.2]
Following the formula
Note: If your text editor / python IDE is not able to render UTF-8
coding as specified by the "# -*- coding: utf-8 -*-" at the top of this
file, the equation that follows will not render correctly.
Entropy=Σ(−p×log(p))Entropy = \Sigma (-p \times log(p))Entropy=Σ(−p×log(p)),
we get −5×(.2)×log(0.2)=0.699-5 \times (.2)\times log(0.2) = 0.699−5×(.2)×log(0.2)=0.699.

Taking a measurement will decrease uncertainty and entropy. Let's say after
taking a measurement, the probabilities become [0.05,0.05,0.05,0.8,0.05]
[0.05, 0.05, 0.05, 0.8, 0.05][0.05,0.05,0.05,0.8,0.05].
Now we have a more certain guess as to where the robot is located and our
entropy has decreased to 0.338.'''

p = [0.2, 0.2, 0.2, 0.2, 0.2]
world = ['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
motions = [1, 1]
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

# You are using the 'sense' function from the previous exercise (#14) and
# the 'move' function from the previous exercise (#23)

#
# TODO: ADD CODE HERE
#

print(p)

# --------------------------------------------------------------------
# 28. SENSE AND MOVE 2
print("\n28. SENSE AND MOVE 2")
# Modify the previous code so that the robot senses red twice.

p = [0.2, 0.2, 0.2, 0.2, 0.2]
world = ['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']  # TODO: CHANGE/UPDATE CODE HERE
motions = [1, 1]
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

# You are using the 'sense' function from the previous exercise (#14) and
# the 'move' function from the previous exercise (#23)

# Copy and paste your solution code from the previous exercise (#27)

print(p)
