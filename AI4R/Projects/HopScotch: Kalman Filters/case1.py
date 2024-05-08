from rait import matrix
class Spaceship():
    """The Spaceship to guide across the galaxy."""

    def __init__(self, bounds):
        """Initialize the Spaceship."""
        self.x_bounds = bounds['x']
        self.y_bounds = bounds['y']

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
        # return asteroid_observations

        # FOR STUDENT TODO: Update the Spaceship's estimate of where the asteroids will be located in the next time step

        ##########################################################################################################################################



        # measurements = [[5, 10], [6, 8], [7, 6], [8, 4], [9, 2], [10, 0]]
        # asteroid_observations = {1: (5,10), 2: (6, 8), 3: (7,6), 4: (8,4), 5: (9,2), 6: (10,0)}
        # asteroid_observations = {1: (0.07055633328298239, 0.4145034580753524 )}
        # initial_xy = [1, 1]
        # dt = .1
        # x = matrix([
        #     [initial_xy[0]], [initial_xy[1]], [0], [0]
        # ])
        # P = matrix([[0, 0, 0, 0],
        #             [0, 0, 0, 0],
        #             [0, 0, 1000, 0],
        #             [0, 0, 0, 1000]])
        #
        # u = matrix([[0], [0], [0], [0]])
        # F = matrix([[1, 0, dt, 0],
        #             [0, 1, 0, dt],
        #             [0, 0, 1, 0],
        #             [0, 0, 0, 1]])
        # H = matrix([[1, 0, 0, 0],
        #             [0, 1, 0, 0]])
        # R = matrix([[.1, 0],
        #             [0, .1]])
        # I = matrix([[1, 0, 0, 0],
        #             [0, 1, 0, 0],
        #             [0, 0, 1, 0],
        #             [0, 0, 0, 1]])
        #
        # new_dict = {}


#########6D test

        u = matrix([[0], [0], [0], [0], [0], [0]])

        dt = 1

        x = matrix([[1], [1], [1], [1], [1], [1]])

        P = matrix([
            [3, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, .009, 0, 0, 0],
            [0, 0, 0, .003, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ])

        F = matrix([
            [1, 0, 1, 0, (1 ** 2) * .5, 0],
            [0, 1, 0, 1, 0, (1 ** 2) * .5],
            [0, 0, 1, 0, 1, 0],
            [0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1]])

        H = matrix([[1, 0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 0, 0]])

        R = matrix([
            [4, 0],
            [0, .1]
        ])

        I = matrix([[1, 0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 1, 0],
                    [0, 0, 0, 0, 0, 1],
                    ])
        new_dict = {}
        asteroid_observations = {1: (0.07055633328298239, 0.4145034580753524)}
        def kalman_filter(x, P):
            for n in asteroid_observations.keys():
                arr = asteroid_observations[n]

                #
                #measurement updates
                Z = matrix([[arr[0]],[arr[1]]])

                y = Z - (H * x)

                S = H * P * H.transpose() + R

                K = P * H.transpose() * S.inverse()

                x = x + (K * y)

                P = (I - (K * H)) * P

                #prediction
                x = (F * x) + u
                P = F * P * F.transpose()


                print('x is')
                x.show()
                print('P is')
                P.show()

                x_new, y_new = x[0][0], x[1][0]
                new_dict[n] = (x_new, y_new)
            print('x is')
            x.show()
            print('P is')
            P.show()
            print('new_dict:')
            print(new_dict)
            return x, P


        return kalman_filter(x, P)






#
bounds = {'x': 4, 'y': 5}
x = Spaceship(bounds)
initial_xy = [4., 12.]
# measurements = [[4,10]]
asteroid_observations = {"1": (4,12)}
print(x.predict_from_observations(asteroid_observations))
