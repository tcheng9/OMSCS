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

from Utilities.robot_pf import *

# PARTICLE FILTER LESSON MODULES
print("PARTICLE FILTER LESSON MODULES", end="")

# --------------------------------------------------------------------
# 8. USING A ROBOT CLASS
print("\n8. USING A ROBOT CLASS")
# For this lesson, (and the following lesson #9),
# please familiarize yourself with the robot class.

myrobot = robot()
myrobot.set(10, 10, 0)
# print(myrobot)
# myrobot = myrobot.move(pi/2, 10)
# print(myrobot)
# print(myrobot.sense())


'''
My notes:
Sense() - figures out the distance of the robot to the 4 landmarks
Move() - MOVES the robot in the x,y direction and TURNS the robot by Theta (some angle)

'''
# --------------------------------------------------------------------
# 10. MOVING ROBOT
print("\n10. MOVING ROBOT")
# Make a robot called myrobot that starts at
# coordinates 30, 50 heading north (pi/2).
# Have your robot turn clockwise by pi/2, move>
# 15 m, and sense. Then have it turn clockwise
# by pi/2 again, move 10 m, and sense again.
# Your program should print out the result of
# your two sense measurements.

myrobot = robot()
# TODO: ADD CODE HERE
'''
Notes:
1. make robot start at 30, 50, pi/2
2. Turn robot by pi/2 and move 15m
3. Call and PRINT sense function
4. Turn robot by pi/2 and move 10m
5. Call and PRINT sense function again

'''

myrobot.set(30, 50, pi/2)
myrobot = myrobot.move(pi/2, 15)
# print(myrobot.sense())
# myrobot = myrobot.move(pi/2, 10)
# print(myrobot.sense())

# --------------------------------------------------------------------
# 11. ADD NOISE
print("\n11. ADD NOISE")
# Now add noise to your robot as follows:
# forward_noise = 5.0, turn_noise = 0.1, sense_noise = 5.0.
#
# Once again, your robot starts at 30, 50,
# heading north (pi/2), then turns clockwise
# by pi/2, moves 15 meters, senses,
# then turns clockwise by pi/2 again, moves
# 10 m, then senses again.

myrobot = robot()
# TODO: ADD CODE HERE
myrobot.set_noise(5, 0.1, 5.0)
myrobot.set(30, 50, pi/2)
myrobot = myrobot.move(pi/2, 15)
# print(myrobot.sense())
# myrobot = myrobot.move(pi/2, 10)
# print(myrobot.sense())

# --------------------------------------------------------------------
# 13. CREATING PARTICLES
print("\n13. CREATING PARTICLES")
# Now we want to create particles,
# p[i] = robot(). In this assignment, write
# code that will assign 1000 such particles
# to a list.
# Your program should print out the length
# of your list (don't cheat by making an
# arbitrary list of 1000 elements!)

N = 1000
p = []
# TODO: ADD CODE HERE
for i in range(N):
    p.append(robot())




# --------------------------------------------------------------------
# 14. ROBOT PARTICLES
print("\n14. ROBOT PARTICLES")
# Now we want to simulate robot
# motion with our particles.
# Each particle should turn by 0.1
# and then move by 5.

# TODO: ADD CODE HERE
############ Lecture solution:
# p2 = []
# for i in range(N):
#     p2.append(p[i].move(0.1, 5.0))
# p = p2

############My solution:
#Question: Does this save the value?
# for particle in range(N):
#     particle = particle.move(0.1, 5.0)
# print(len(p))

##########MY alternative solution:
for i in range(len(p)):
    p[i] = p[i].move(0.1, 5.0)

# --------------------------------------------------------------------
# 15. IMPORTANCE WEIGHT
print("\n15. IMPORTANCE WEIGHTS")
# Now we want to give weight to our
# particles. This program will print a
# list of 1000 particle weights.


#################initial robot setup

#This setups up the actual robot
myrobot = robot()
myrobot = myrobot.move(0.1, 5.0)
Z = myrobot.sense() #Normal distribution of robot's location likelihoods

##This sets up the 1000 various particles in the environment
N = 1000
p = []
for i in range(N):
    x = robot()
    x.set_noise(0.05, 0.05, 5.0)
    p.append(x)

##Moves each particle around (to mimic robot movement?)
p2 = []

for i in range(N):
    p2.append(p[i].move(0.1, 5.0))
p = p2

# Copy and paste your solution code from the previous exercises (#13 and #14)
# Note that there will need to be a small modification for setting noise to the
# previous code as stated in the video

w = []
# TODO: ADD CODE HERE
##Create the importance weighting for each individual particle
##Use measurement_prob to take in the measurement of the robot and calculate likelihood how far the measurement from the actual measurements
##Need to asssume measurment noise for each particle


for i in range(N):
    particle = p[i] #Particle at Ith iteration
    # Using robot's measurement (aka gaussian distribution) with measurement_prob function value FIND OUT the Likelihood of this particle's location USING the robot's normal distribution curve
    w.append(particle.measurement_prob(Z))
print(w)
print('sum of w', sum(w))




# --------------------------------------------------------------------
# 20. NEW PARTICLE
print("\n20. NEW PARTICLE")
# In this exercise, try to write a program that
# will resample particles according to their weights.
# Particles with higher weights should be sampled
# more frequently (in proportion to their weight).

p3 = []
# TODO: ADD CODE HERE
##He didn't show any feasible solution
p = p3

# --------------------------------------------------------------------
# 21. RESAMPLING WHEEL
print("\n21. RESAMPLING WHEEL")
# In this exercise, you should implement the
# resampler shown in the previous video.
'''
The pseudocode in the video should be like this (instead of an if-else block):

while w[index] < beta:
    beta = beta - w[index]
    index = (index + 1) % N

select p[index]
'''
myrobot = robot()
myrobot = myrobot.move(0.1, 5.0)
Z = myrobot.sense()

N = 1000
p = []

# Copy and paste your solution code from the previous exercise (#15)
myrobot = robot()
myrobot = myrobot.move(0.1, 5.0)
Z = myrobot.sense() #Normal distribution of robot's location likelihoods

##This sets up the 1000 various particles in the environment
N = 1000
p = []
for i in range(N):
    x = robot()
    x.set_noise(0.05, 0.05, 5.0)
    p.append(x)

##Moves each particle around (to mimic robot movement?)
p2 = []
for i in range(N):
    p2.append(p[i].move(0.1, 5.0))
p = p2


w = []

for i in range(N):
    particle = p[i] #Particle at Ith iteration
    # Using robot's measurement (aka gaussian distribution) with measurement_prob function value FIND OUT the Likelihood of this particle's location USING the robot's normal distribution curve
    w.append(particle.measurement_prob(Z))
# print('weighted particles arr)')
# print(w)
# print(w)

p3 = []
# TODO: ADD CODE HERE
beta = 0.0
index = int(random.random()*N) #Get a random int random from 0 to 1 and scale by 1000
mw = max(w) #Max weight needed for calc
for i in range(N):
    beta = beta + random.random() * 2.0 * mw
    while w[i] < beta:
        beta = beta - w[index]
        index = (index + 1 ) % N
    p3.append(p[index]) #New particle at iteration I is particle[at some specific index you land on in the resampling wheel]

p = p3

# --------------------------------------------------------------------
# 23. ORIENTATION 2
print("\n23. ORIENTATION 2")
# In this exercise, write a program that will
# run your previous code twice.

N = 1000
myrobot = robot()
p = []

# Copy and paste your code from the previous exercise (#21)
# TODO: CHANGE/UPDATE CODE HERE
myrobot = robot()


##This sets up the 1000 various particles in the environment
N = 1000
p = []
for i in range(N):
    x = robot()
    x.set_noise(0.05, 0.05, 5.0)
    p.append(x)

for i in range(2):
    myrobot = myrobot.move(0.1, 5.0)
    Z = myrobot.sense()
##Moves each particle around (to mimic robot movement?)

    p2 = []
    for i in range(N):
        p2.append(p[i].move(0.1, 5.0))
    p = p2


    w = []

    for i in range(N):
        particle = p[i] #Particle at Ith iteration
        # Using robot's measurement (aka gaussian distribution) with measurement_prob function value FIND OUT the Likelihood of this particle's location USING the robot's normal distribution curve
        w.append(particle.measurement_prob(Z))

    # print(w)

    p3 = []
    # TODO: ADD CODE HERE
    beta = 0.0
    index = int(random.random()*N) #Get a random int random from 0 to 1 and scale by 1000
    mw = max(w) #Max weight needed for calc
    for i in range(N):
        beta = beta + random.random() * 2.0 * mw
        while w[i] < beta:
            beta = beta - w[index]
            index = (index + 1 ) % N
        p3.append(p[index]) #New particle at iteration I is particle[at some specific index you land on in the resampling wheel]
    p = p3



# print(p)

# --------------------------------------------------------------------
# 24. ERROR
print("\n24. ERROR")
# In this exercise, write a program that will
# print out the quality of your solution
# using the eval function. (Should print T times!)

T = 10
N = 1000
myrobot = robot()
p = []

# Copy and paste your code from the previous exercise (#23)
# TODO: CHANGE/UPDATE CODE HERE
for i in range(N):
    x = robot()
    x.set_noise(0.05, 0.05, 5.0)
    p.append(x)

for i in range(T):
    print(eval(myrobot, p))
    myrobot = myrobot.move(0.1, 5.0)
    Z = myrobot.sense()
##Moves each particle around (to mimic robot movement?)

    p2 = []
    for i in range(N):
        p2.append(p[i].move(0.1, 5.0))
    p = p2


    w = []

    for i in range(N):
        particle = p[i] #Particle at Ith iteration
        # Using robot's measurement (aka gaussian distribution) with measurement_prob function value FIND OUT the Likelihood of this particle's location USING the robot's normal distribution curve
        w.append(particle.measurement_prob(Z))

    # print(w)

    p3 = []
    # TODO: ADD CODE HERE
    beta = 0.0
    index = int(random.random()*N) #Get a random int random from 0 to 1 and scale by 1000
    mw = max(w) #Max weight needed for calc
    for i in range(N):
        beta = beta + random.random() * 2.0 * mw
        while w[i] < beta:
            beta = beta - w[index]
            index = (index + 1 ) % N
        p3.append(p[index]) #New particle at iteration I is particle[at some specific index you land on in the resampling wheel]
    p = p3
