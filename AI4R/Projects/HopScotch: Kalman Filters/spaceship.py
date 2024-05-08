from rait import matrix
from utilities import distance_formula

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

# If you see different scores locally and on Gradescope this may be an
# indication that you are uploading a different file than the one you are
# executing locally. If this local ID doesn't match the ID on Gradescope then
# you uploaded a different file.
OUTPUT_UNIQUE_FILE_ID = False
if OUTPUT_UNIQUE_FILE_ID:
    import hashlib, pathlib
    file_hash = hashlib.md5(pathlib.Path(__file__).read_bytes()).hexdigest()
    print(f'Unique file ID: {file_hash}')


class Spaceship():
    """The Spaceship to guide across the galaxy."""

    def __init__(self, bounds):
        """Initialize the Spaceship."""
        self.x_bounds = bounds['x']
        self.y_bounds = bounds['y']
        # Matrices in 6D
        self.u = matrix([[0], [0], [0], [0], [0], [0]])

        self.dt = 1

        self.x = matrix([[.5], [.5], [0], [0], [0], [0]])

        self.P = matrix([
            [1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, .01, 0, 0, 0],
            [0, 0, 0, .001, 0, 0],
            [0, 0, 0, 0, .005,0 ],
            [0, 0, 0, 0, 0, .005],
        ])

        self.F = matrix([
            [1, 0, 1, 0, (1 ** 2) * .5, 0],
            [0, 1, 0, 1, 0, (1 ** 2) * .5],
            [0, 0, 1, 0, 1, 0],
            [0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1]])

        self.H = matrix([[1, 0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 0, 0]])

        self.R = matrix([
            [0.050, 0],
            [0, 0.075]
        ])

        self.I = matrix([[1, 0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 1, 0],
                    [0, 0, 0, 0, 0, 1],
                    ])
        # self.new_dict = {}
        self.xp_dict = {}
        self.asteroid_ages = {}
    def predict_from_observations(self, asteroid_observations):

        """Observe asteroid locations and predict their positions at time t+1.
        Parameters
        ----------
        self = a reference to the current object, the Spaceship
        asteroid_observations = A dictionary in which the keys represent asteroid IDs
        and the values are a dictionary of noisy x-coordinate observations,
        and noisy y-coordinate observations taken at time t.
        asteroid_observations format:
        ```
        `{1: (x-measurement, y-measurement),
          2: (x-measurement, y-measurement),
          100: (x-measurement, y-measurement),
          }`
        ```

        Returns
        -------
        The output of the `predict_from_observations` function should be a dictionary of tuples
        of estimated asteroid locations one timestep into the future
        (i.e. the inputs are for measurements taken at time t, and you return where the asteroids will be at time t+1).

        A dictionary of tuples containing i: (x, y), where i, x, and y are:
        i = the asteroid's ID
        x = the estimated x-coordinate of asteroid i's position for time t+1
        y = the estimated y-coordinate of asteroid i's position for time t+1
        Return format:
        `{1: (x-coordinate, y-coordinate),
          2: (x-coordinate, y-coordinate),
          100: (x-coordinate, y-coordinate)
          }`
        """
        # To view the visualization with the default pdf output (incorrect) uncomment the line below
        # print('asteroids')
        # print(asteroid_observations)
        # print('----------------------------------------------------')
        # return asteroid_observations

        # FOR STUDENT TODO: Update the Spaceship's estimate of where the asteroids will be located in the next time step

        ##########################################################################################################################################

        def kalman_filter(x, P, x_obs, y_obs):
            #For each key, get the corresponding values
            #The following code is from: https://gatech.instructure.com/courses/364682/pages/27-kalman-matrices-answer?module_item_id=3773206
            Z = matrix([[x_obs], [y_obs]])

            Y = Z - (self.H * x)

            S = self.H * P * self.H.transpose() + self.R
            K = P * self.H.transpose() * S.inverse()

            x = x+ (K * Y)
            P = (self.I - (K * self.H)) * P


            x = (self.F * x)
            P = self.F * P * self.F.transpose()


            return x,P

            #end of code citation
        new_dict = {}
        for key in asteroid_observations.keys():
            #get values for KF
            x_obs, y_obs = asteroid_observations[key]

            x,P = self.xp_dict.get(key, (self.x, self.P))

            x, P = kalman_filter(x,P, x_obs, y_obs)

            self.xp_dict[key] = x, P
            new_dict[key] = (x[0][0], x[1][0])


        return new_dict


    def jump(self, asteroid_observations, agent_data):
            """ Return the id of the asteroid the spaceship should jump/hop onto in the next timestep
            ----------
            self = a reference to the current object, the Spaceship
            asteroid_observations: Same as predict_from_observations method
            agent_data: a dictionary containing agent related data:
            'jump_distance' - a float representing agent jumping distance,
            'ridden_asteroid' - an int representing the ID of the ridden asteroid if available, None otherwise.
             'xpos_start' - A tuple representing the (x, y) position of the agent at t = 0 of the agent which is a tuple of
            (x, y) at t=0.

            agent_data format:

            {'ridden_asteroid': None,
             'jump_distance': agent.jump_distance,
             'xypos_start':  (x, y),
             }

            Returns
            -------
            You are to return two items.
            1: idx, this represents the ID of the asteroid on which to jump if a jump should be performed in the next timestep.
            Return None if you do not intend to jump on an asteroid in the next timestep
            2. Return the estimated positions of the asteroids (i.e. the output of 'predict_from_observations method)
            IFF you intend to have them plotted in the visualization. Otherwise return None
            -----
            an example return
            idx to hop onto in the next timestep: 3,
            estimated_results = {1: (x-coordinate, y-coordinate),
              2: (x-coordinate, y-coordinate)}

            return 3, estimated_return

            """
            # FOR STUDENT TODO: Update the idx of the asteroid on which to jump
            idx = None


            predictions = self.predict_from_observations(asteroid_observations) #Asteroid predictions

            curr_asteroid = agent_data['ridden_asteroid'] #Track ID of asteroid you are riding
            jd = agent_data['jump_distance'] * .5
            # inrange_dict = {}

            x_bounds = self.x_bounds
            y_bounds = self.y_bounds
            def inrange(pt1, pt2, jump_dist):
                ed = distance_formula(pt1, pt2)
                if (ed < jump_dist):
                    return True
                else:
                    return False

            ##Build dictionary of possible asteroids
            # if agent_data['ridden_asteroid'] is None:
            #     for key in predictions.keys():
            #         new_pt = predictions[key]
            #         curr_pt = agent_data['xypos_start']
            #         if inrange(curr_pt, new_pt, jd):
            #             inrange_dict[key] = (new_pt[0], new_pt[1])
            # else:
            #     for key in predictions.keys():
            #         # print('not none')
            #         new_pt = predictions[key]
            #         curr_pt = predictions[curr_asteroid]
            #         if inrange(curr_pt, new_pt, jd):
            #             inrange_dict[key] = (new_pt[0], new_pt[1])

            def build_dict():
                _dict = {}
                if agent_data['ridden_asteroid'] is None:
                    for key in predictions.keys():
                        new_pt = predictions[key]
                        curr_pt = agent_data['xypos_start']
                        if inrange(curr_pt, new_pt, jd):
                            _dict[key] = (new_pt[0], new_pt[1])
                else:
                    for key in predictions.keys():
                        # print('not none')
                        new_pt = predictions[key]
                        curr_pt = predictions[curr_asteroid]
                        if inrange(curr_pt, new_pt, jd):
                            _dict[key] = (new_pt[0], new_pt[1])
                return _dict
            inrange_dict = build_dict()
            ###get id of max y

            # for key in inrange_dict:
            #     x, P = self.xp_dict[key]
            #     y_vel = P[3][3] #y_velocity
            #     y_acc = P[5][5] #y acceleration
            #     x,y = inrange_dict[key]
            #     if (y > 1.95 and y_vel > 0 and y_acc > 0):
            #         idx = None
            #         return idx, predictions
            #     if (max_y < y):
            #         max_y = y
            #         idx = key

            def decision(inrange_dict, predictions):
########ISSUE EARLIRE WAS THAT I WAS NOT HANDLING BASE CASE OF NEEDING TO USE XYPOS_START BECAUSE RIDDEN ASTEROID IS NONE
                #Setup variables
                idx = None
                max_y = -1.
                max_x_pos = -1.
                min_x_pos = 100.
                return_key = -1
                x_bounds = 100.
                ###Handling X OOB
                #lower bound X
                if (agent_data['ridden_asteroid'] is None and agent_data['xypos_start'][0]  < 1):
                    #lower bounds check

                    for key in inrange_dict.keys():
                        x, P = self.xp_dict[key]
                        curr_x_pos = x[0][0]

                        if (max_x_pos < curr_x_pos ):
                            max_x_pos = curr_x_pos
                            return_key = key
                    return return_key if return_key else None

                if (agent_data['ridden_asteroid'] is not None and predictions[agent_data['ridden_asteroid']][0]  < 1):
                    #lower bounds check
                    for key in inrange_dict.keys():
                        x, P = self.xp_dict[key]
                        curr_x_pos = x[0][0]

                        if (max_x_pos < curr_x_pos):
                            max_x_pos = curr_x_pos
                            return_key = key
                    return return_key if return_key else None

                #Upper bound X
                if (agent_data['ridden_asteroid'] is None and agent_data['xypos_start'][0]  > (x_bounds -(x_bounds*.3) )):
                    #upper bounds check
                    for key in inrange_dict.keys():
                        x, P = self.xp_dict[key]
                        curr_x_pos = x[0][0]

                        if (min_x_pos > curr_x_pos):
                            min_x_vel = curr_x_pos
                            return_key = key
                    return return_key if return_key else None

                if (agent_data['ridden_asteroid'] is not None and predictions[agent_data['ridden_asteroid']][0] > (x_bounds -(x_bounds*.3) )):
                    #lower bounds check
                    for key in inrange_dict.keys():
                        x, P = self.xp_dict[key]
                        curr_x_pos = x[0][0]

                        if (min_x_pos > curr_x_pos):
                            min_x_vel = curr_x_pos
                            return_key = key
                    return return_key if return_key else None
                #If None + near out of bounds:
                    #iterate through and find max_x velocity

                #if bounds none + near out of bounds

            ###End of Handling X OOB

            ####if in bounds, you just want to go up
                for key in inrange_dict.keys():

                    x, P = self.xp_dict[key]
                    y_vel = P[3][3]  # y_velocity
                    y_acc = P[5][5]  # y acceleration
                    x, y = inrange_dict[key]

                    x_vel = P[2][2]
                    x_acc = P[4][4]

                    # ##Trying to handle x OOB
                    # if (curr_x < 0.1 and x_vel > 0):
                    #     # on lower bounds, find an asteroid that goes toawrds the center
                    #     print('stopping red underlines')
                    #     return key
                    #
                    #
                    # if (curr_x > (self.x_bounds - (self.x_bounds * .05))) and x_vel <0:
                    #     # close to upper bounds, find an asteroid that goes towards the center
                    #     print('stopping red underlines')
                    #     return key
                    #
                    #
                    #
                    # ##End of trying to handle x OOB



                    if (y > 1.95 and y_vel > 0 and y_acc > 0):
                        #If close to the goal and the asteroid you are on is going up, just ride it UNLESS it falls out of bounds
                        idx = None
                        return None
                    if (max_y < y):
                        max_y = y
                        idx = key
                return idx


            idx = decision(inrange_dict, predictions)
            return idx, predictions

def who_am_i():
    # Please specify your GT login ID in the whoami variable (ex: jsmith124).
    whoami = 'tcheng99'
    return whoami

