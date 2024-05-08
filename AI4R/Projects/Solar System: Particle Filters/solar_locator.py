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

# These import statements give you access to library functions which you may
# (or may not?) want to use.
import random
import time
from math import *
from body import *
from solar_system import *
from satellite import *

def estimate_next_pos(gravimeter_measurement, get_theoretical_gravitational_force_at_point, distance, steering, other=None):
    """
    Estimate the next (x,y) position of the satelite.
    This is the function you will have to write for part A.
    :param gravimeter_measurement: float
        A floating point number representing
        the measured magnitude of the gravitation pull of all the planets
        felt at the target satellite at that point in time.
    :param get_theoretical_gravitational_force_at_point: Func
        A function that takes in (x,y) and outputs a float representing the magnitude of the gravitation pull from
        of all the planets at that (x,y) location at that point in time.
    :param distance: float
        The target satellite's motion distance
    :param steering: float
        The target satellite's motion steering
    :param other: any
        This is initially None, but if you return an OTHER from
        this function call, it will be passed back to you the next time it is
        called, so that you can use it to keep track of important information
        over time. (We suggest you use a dictionary so that you can store as many
        different named values as you want.)
    :return:
        estimate: Tuple[float, float]. The (x,y) estimate of the target satellite at the next timestep
        other: any. Any additional information you'd like to pass between invocations of this function
        optional_points_to_plot: List[Tuple[float, float, float]].
            A list of tuples like (x,y,h) to plot for the visualization
    """


    # example of how to get the gravity magnitude at a point in the solar system:
    gravity_magnitude = get_theoretical_gravitational_force_at_point(-1*AU, 1*AU)

    # TODO - remove this canned answer which makes this template code
    # pass one test case once you start to write your solution....
    ##WHERE I ThINK THE TARGET SATELLITE IS AT. -> colored as "skyblue square"
    ## "red circle" is where the target satellite actually is
    xy_estimate = (139048139368.39096, -2225218287.6720667)


    ##Step 1 Making random particles

    def particle_init(N):
        #N = number of particles u want
        arr = []  # Particle array



        #if other is None -> create a new set of particles ELSE return Other as the list of particles
        if other is not None:
            # print('other is not none')
            # print(other)
            return other

            # print('other is none')
            # arr.append((139048139368.39096, -2225218287.6720667, 1))
        for i in range(N):
            x = (random.uniform(-4, 4)) * AU
            y = (random.uniform(-4, 4)) * AU

            ######################3
            #Exact sateliite coordinates for testing
            # x = 139048139368.39096
            # y = 2225218287.6720667

            ####################3
            orientation = atan2(y,x) + pi/2
            arr.append((x, y, orientation))

        return arr
    # #######################################################################################################
    #
    # time.sleep(.01)  # uncomment to pause for the specified seconds each timestep
    #
    # #######################################################################################################
    # p_arr = particle_init(5000)
    # print(len(p_arr))
    ##Step 2 - Weightign of the particles



    def Gaussian(mu, sigma, x):
        # calculates the probability of x for 1-dim Gaussian with mean mu and var. sigma
        return exp(- ((mu - x) ** 2) / (sigma ** 2) / 2.0) / sqrt(2.0 * pi * (sigma ** 2))




    def weighting(particles):
        '''
        Takes an array of particles and creates their corresponding (normalized) weights
        '''
        weights = []
        for i in range(len(particles)):
            #This for loop gets the likelihood of particle[i] compares to a Gaussian distribution (mu = gravimeter-measurement, sigma = 1)
            x = particles[i][0]
            y = particles[i][1]


            # print('particle gravity')
            # print(get_theoretical_gravitational_force_at_point(x,y))
            # print('----------------')
            gauss = Gaussian(gravimeter_measurement,.0000001, get_theoretical_gravitational_force_at_point(x,y))


            weights.append(gauss)
        # print('non normalized weights')
        # print(weights)
        # print('---------------------')
        sum_weights = sum(weights)
        for i in range(len(particles)):
            weights[i] = weights[i]/sum_weights

        # print(' normalized weights')
        # print(weights)
        # print('---------------------')

        return weights

    # w_arr = weighting(p_arr) #array of particles weightings

    ##Step 3 Resampling - Resampling wheel:
    def resampling_wheel(particles, particle_weights):
        '''
        Takes in particles array and their corresponding weights
        and uses them in the resampling wheel to return an array of new particles

        '''


        ###Following code cited from: https://gatech.instructure.com/courses/364682/pages/21-resampling-wheel-answer?module_item_id=3773346
        N = len(particles)
        beta = 0.0
        index = int(random.random()* len(particles)) #Choose a random index to start at
        max_weight = max(particle_weights) #Highest weighted particle in particle_arr
        #INCORRECTINCORRECTINCORRECTINCORRECTINCORRECTINCORRECT
        new_particles_array = []#new particle array BUT the new array becomes old so this is INCORRECT
        #Because you have to update the old particle array, not just create a new one
        for i in range(N):
            #resampling wheel algo
            beta += random.random()*2.0 * max_weight
            while beta > particle_weights[index]:
                beta -= particle_weights[index]
                index = (index + 1) % N
            new_particles_array.append(p_arr[index])

        #End of code citation
        return new_particles_array

    # p_arr = resampling_wheel(p_arr, w_arr) #takes in the current particles and their cooressponding weights and returns a new set of particles


    ##Step 4: Fuzzing
    def fuzzing(particles):
        #Fuzzing particles array
        #Tuning parameter of how much you want to spread out the stacked particles after resampling


        for i in range(len(particles)):
            x,y, orientation = particles[i]
            x_fuzz = (random.uniform(-.05 * AU, .05 * AU))
            y_fuzz = (random.uniform(-.05 * AU, .05 * AU))

            new_x = x + x_fuzz
            new_y = y + y_fuzz
            new_orientation = atan2(y,x) + pi/2
            particles[i] = (new_x,new_y, new_orientation)

        return particles
    # p_arr = fuzzing(p_arr)

    ##Step 5: Bicycle motion for each particle
    def bicycle_motion(particles, distance, steering):
        # print('biyccle motion')
        #distance = forward_motion
        #steering = steering angle

        ###Setup
        #distance, motion are given
        sat_length = 10.2 #length satellite
        beta = (distance/sat_length) * tan(steering)

        #Following code cited from:https://gatech.instructure.com/courses/364682/pages/kinematic-bicycle-model-27-formulas?module_item_id=3773438
        tolerance = .000001 #if < than this, you consider it just going straight
        for i in range(len(particles)):
            x,y, orientation = particles[i]
            if abs(beta) < tolerance:
                x_new = x + distance * cos(orientation)
                y_new = y + distance * sin(orientation)
                orientation_new = orientation+beta

            else:
                #Step 1; determine radius
                radius = sat_length / tan(steering)

                #step 2: determine center of circle
                x_dist = sin(orientation) * radius
                y_dist = cos(orientation) * radius
                center_x = x - x_dist
                center_y = y + y_dist

                #Step 3: determine arc length
                beta = distance / radius

                #Determine 4: calc new x,y orientation
                x_dist_new = sin(orientation + beta) * radius
                y_dist_new = cos(orientation+beta) * radius
                x_new = center_x + x_dist_new
                y_new = center_y - y_dist_new

                orientation_new = (orientation+beta) % (2*pi)

            particles[i] = (x_new, y_new, orientation_new)
        #end of code citation
        return particles

    # print('before bicycle model')
    # print(p_arr)
    # p_arr = bicycle_motion(p_arr, distance, steering)
    # print('after bicycle model')
    # print(p_arr)
    ##Step 6: Evaluation

    def eval(particles):

        ##Random evaluate
        # index = int(random.random() * len(particles))
        # x,y = particles[index][0], particles[index][1]
        # return (x,y)

        #unweighted average
        x_sum = 0
        y_sum = 0
        for i in range(len(particles)):
            x,y,orientation = particles[i]
            x_sum += x
            y_sum += y
        x_avg = x_sum / len(particles)
        y_avg = y_sum / len(particles)

        return x_avg, y_avg



    # predicted_xy = eval(p_arr)
    # print(p_arr)


    ##Step 7: new particles become old

    '''
    # You may optionally also return a list of (x,y,h) points that you would like
    # the PLOT_PARTICLES=True visualizer to plot for visualization purposes.
    # If you include an optional third value, it will be plotted as the heading
    # of your particle.

    optional_points_to_plot = [(1*AU, 1*AU), (2*AU, 2*AU), (3*AU, 3*AU)]  # Sample (x,y) to plot
    optional_points_to_plot = [(1*AU, 1*AU, 0.5),
                               (2*AU, 2*AU, 1.8),
                               (3*AU, 3*AU, 3.2),
                               (1.5*AU, 1.5*AU, 2.2),
                               (2.5*AU, 2.5*AU, 1.2)]  # (x,y,heading)
    '''


    ###Particle filter control function
    #######################################################################################################

    # time.sleep(.01)  # uncomment to pause for the specified seconds each timestep

    #######################################################################################################

    #initialization
    p_arr = particle_init(5000)

    #weighting

    w_arr = weighting(p_arr)

    #Resampling
    p_arr = resampling_wheel(p_arr, w_arr)

    #fuzzing
    p_arr = fuzzing(p_arr)

    #Mimicking via bicycle motion model
    p_arr = bicycle_motion(p_arr, distance, steering)

    #Evaluation of particle filter
    predicted_xy = eval(p_arr)
    #
    # xy_estimate = (139048139368.39096, -2225218287.6720667)
    #
    # if other is None:
    #     print('other is none')
    #     xy_estimate = (139048139368.39096, -2225218287.6720667)
    #     other = [(139048139368.39096, -2225218287.6720667)]
    # else:
    #     print('other is not none')
    #     xy_estimate = bicycle_motion(xy_estimate, distance, steering)
    #     other = bicycle_motion(xy_estimate, distance, steering)


    other = p_arr
    # predicted_xy
    return predicted_xy, other, p_arr


def next_angle(solar_system, percent_illuminated_measurements, percent_illuminated_sense_func,
               distance, steering, other=None):
    """
    Gets the next angle at which to send out an sos message to the home planet,
    the last planet in the solar system.
    This is the function you will have to write for part B.
    :param solar_system: SolarSystem
        A model of the solar system containing the sun and planets as Bodys (contains positions, velocities, and masses)
        Planets are listed in order from closest to furthest from the sun
    :param percent_illuminated_measurements: List[float]
        A list of floating point number from 0 to 100 representing
        the measured percent illumination of each planet in order from closest to furthest to sun
        as seen by the target satellite.
    :param percent_illuminated_sense_func: Func
        A function that takes in (x,y) and outputs the list of percent illuminated measurements of each planet
        as would be seen by satellite at that (x,y) location.
    :param distance: float
        The target satellite's motion distance
    :param steering: float
        The target satellite's motion steering
    :param other: any
        This is initially None, but if you return an OTHER from
        this function call, it will be passed back to you the next time it is
        called, so that you can use it to keep track of important information
        over time. (We suggest you use a dictionary so that you can store as many
        different named values as you want.)
    :return:
        bearing: float. The absolute angle from the satellite to send an sos message between -pi and pi
        xy_estimate: Tuple[float, float]. The (x,y) estimate of the target satellite at the next timestep
        other: any. Any additional information you'd like to pass between invocations of this function
        optional_points_to_plot: List[Tuple[float, float, float]].
            A list of tuples like (x,y,h) to plot for the visualization
    """


    particles = [] #array to store all particles -> {Ith particle: (x,y,h)} structure
    bearings = [] #array to store all bearings  -> {Ith particle: bearing}
    weightings = [] #Array to store weightings -> need to unpack in other


    #Step 1: Initialization
    def particle_init(N):
        # print('N particles')

        particles = []
        bearings = []
        weightings = []
        '''
        #For later
        #if other is not none:
            unpack the other into weightings, 
        
        
        other = {'particles': p_arr, 'bearings': b_arr, 'weights': w_arr}
        '''
        # if other is None -> create a new set of particles ELSE return Other as the list of particles
        if other is not None:
            # print('other is not none')
            # print(other)
            particles = other['particles']
            bearings = other['bearings']

            return particles, bearings

            # print('other is none')
            # arr.append((139048139368.39096, -2225218287.6720667, 1))


        for i in range(N):
            x = random.uniform(-4, 4) * AU
            y = random.uniform(-4, 4) * AU
            orientation = atan2(y,x) + pi / 2
            ##new thing to follow
            bearing = atan2(y,x) % (2*pi)

            # print(x,y, orientation, bearing)
            particles.append((x,y,orientation))
            bearings.append(bearing)


        return particles, bearings #Return a dict of particles and bearings


    def Gaussian(mu, sigma, x):
        # calculates the probability of x for 1-dim Gaussian with mean mu and var. sigma
        return exp(- ((mu - x) ** 2) / (sigma ** 2) / 2.0) / sqrt(2.0 * pi * (sigma ** 2))
    #Step 2: Weighting
    def weighting(particles, bearings):
        weights = []


        #getting likelihood of particle
        for i in range(len(particles)):
            prob = 1.0
            x,y, orientation = particles[i]
            particle_measurements = percent_illuminated_sense_func(x,y)
            target_measurements = percent_illuminated_measurements
            # print('particle measurement')
            # print(particle_measurements)
            # print('target measurements')
            # print(target_measurements)
            # print('--------------------------------------')
            for i in range(len(percent_illuminated_measurements)):
                prob *= Gaussian(target_measurements[i], 5, particle_measurements[i])



            weights.append(prob)

        sum_weights = sum(weights)
        for i in range(len(particles)):
            weights[i] = weights[i] / sum_weights



        return weights

    #Step 3: Resampling
    def resampling_wheel(particles, particle_weights):
        '''
        Takes in particles array and their corresponding weights
        and uses them in the resampling wheel to return an array of new particles

        '''
        ###Following code cited from: https://gatech.instructure.com/courses/364682/pages/21-resampling-wheel-answer?module_item_id=3773346
        N = len(particles)
        beta = 0.0
        index = int(random.random()* len(particles)) #Choose a random index to start at
        max_weight = max(particle_weights) #Highest weighted particle in particle_arr
        #INCORRECTINCORRECTINCORRECTINCORRECTINCORRECTINCORRECT
        new_particles_array = []#new particle array BUT the new array becomes old so this is INCORRECT
        #Because you have to update the old particle array, not just create a new one
        # id_arr = []
        # for i in range(N):
        #     id_arr.append(id(particles[i]))
        # print('ids before resampling')
        # print(id_arr)
        for i in range(N):
            #resampling wheel algo
            beta += random.random()*2.0 * max_weight
            while beta > particle_weights[index]:
                beta -= particle_weights[index]
                index = (index + 1) % N
            new_particles_array.append(p_arr[index])




        #End of code citation
        return new_particles_array


    #Step 4 Fuzzing:
    def fuzzing(particles, bearings):
        #Fuzzing particles array
        #Tuning parameter of how much you want to spread out the stacked particles after resampling


        for i in range(len(particles)):
            x,y, orientation = particles[i]
            x_fuzz = (random.uniform(-2, 2))
            y_fuzz = (random.uniform(-2, 2))

            new_x = x + x_fuzz
            new_y = y + y_fuzz
            new_orientation = atan2(y,x) + pi/2
            new_bearing = atan2(y,x) % (2*pi)
            particles[i] = (new_x,new_y, new_orientation)
            bearings[i] = new_bearing


        return particles, bearings


    #Step 5: motion model
    def bicycle_motion(particles, distance, steering):
        # print('biyccle motion')
        #distance = forward_motion
        #steering = steering angle

        ###Setup
        #distance, motion are given
        sat_length = 10.2 #length satellite
        # beta = (distance/sat_length) * tan(steering)

        # Following code cited from:https://gatech.instructure.com/courses/364682/pages/kinematic-bicycle-model-27-formulas?module_item_id=3773438
        for i in range(len(particles)):
            x,y, orientation = particles[i]


            #Step 1; determine radius
            radius = sat_length / tan(steering)

            #step 2: determine center of circle
            x_dist = sin(orientation) * radius
            y_dist = cos(orientation) * radius
            center_x = x - x_dist
            center_y = y + y_dist

            #Step 3: determine arc length
            beta = distance / radius

            #Determine 4: calc new x,y orientation
            x_dist_new = sin(orientation + beta) * radius
            y_dist_new = cos(orientation+beta) * radius
            x_new = center_x + x_dist_new
            y_new = center_y - y_dist_new

            orientation_new = (orientation+beta) % (2*pi)

            particles[i] = (x_new, y_new, orientation_new)


        #end of code citation
        return particles

    #Step 6: evaluation
    def eval(particles):

        ##Random evaluate
        # index = int(random.random() * len(particles))
        # x,y = particles[index][0], particles[index][1]
        # return (x,y)

        #unweighted average
        x_sum = 0
        y_sum = 0
        for i in range(len(particles)):
            x,y,orientation = particles[i]
            x_sum += x
            y_sum += y
        x_avg = x_sum / len(particles)
        y_avg = y_sum / len(particles)

        return x_avg, y_avg

    #future control panel function
    # time.sleep(.01)
    p_arr, b_arr =  particle_init(2000)
    w_arr = weighting(p_arr, b_arr)
    p_arr = resampling_wheel(p_arr, w_arr)
    p_arr, b_arr = fuzzing(p_arr, b_arr)

    p_arr = bicycle_motion(p_arr, distance, steering)

    x_predicted, y_predicted = eval(p_arr)
    ####

    # # At what angle to send an SOS message this timestep
    # bearing = 0.0
    # xy_estimate = (110172640485.32968, -66967324464.19617)
    #
    # # You may optionally also return a list of (x,y) or (x,y,h) points that
    # # you would like the PLOT_PARTICLES=True visualizer to plot.
    # optional_points_to_plot = [ (1*AU,1*AU), (2*AU,2*AU), (3*AU,3*AU) ]  # Sample plot points

    # return_bearing = b_arr[0]
    # x,y, orientation = p_arr[0]
    # xy_estimate = (x_predicted,y_predicted)
    # p_arr = [(x,y,orientation)]
    # return bearing, xy_estimate, other, optional_points_to_plot


    ####Crafting actual return values
    #Move solarsystem first
    outer_planet = solar_system.planets[-1]
    outer_planet = SolarSystem.move_body(outer_planet)
    print('outer planet')
    print(outer_planet)
    home_planet_x = solar_system.planets[-1].r[0]
    home_planet_y = solar_system.planets[-1].r[1]

    predicted_bearing = (atan2(home_planet_y - y_predicted, home_planet_x-x_predicted)) % (2*pi)
    xy_estimate = (x_predicted,y_predicted)
    other = {'particles': p_arr, 'bearings': b_arr, 'weights': w_arr}
    # print('solar system')
    # print(solar_system.planets[-1].r[0]) #prints a list
    # home_planet_x = solar_system.planets[-1].r[0]
    # home_planet_y = solar_system.planets[-1].r[1]

    # print('--------------')
    return predicted_bearing, xy_estimate, other, p_arr

    ###Code to set so that my return works properly
    # p_arr = p_arr
    # print('iter ended')
    # other = {}
    # p_arr =[ (1*AU,1*AU), (2*AU,2*AU), (3*AU,3*AU) ]
    # return 0.0, (110172640485.32968, -66967324464.19617), other, p_arr
    ####
def who_am_i():
    # Please specify your GT login ID in the whoami variable (ex: jsmith124).
    whoami = 'tcheng99'
    return whoami
