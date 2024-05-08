from rait import matrix
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
    [1, 0, 1, 0, (1**2)*.5, 0],
    [0, 1, 0, 1, 0, (1**2)*.5],
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
    for i in asteroid_observations.keys():
        tup = asteroid_observations[i]


        #measurement update
        Z = matrix([[tup[0]], [tup[1]]])
        Y = Z - (H * x)
        S = H * P * H.transpose() + R
        K = P * H.transpose() * S.inverse()

        x = x+ (K * Y)
        P = (I - (K * H)) * P

        # Prediction update
        # X = (F * X) + u
        x = (F * x)
        P = F * P * F.transpose()

        x_new, y_new = x[0][0], x[1][0]
        new_dict[i] = (x_new, y_new)

        print('x is')
        x.show()
        print('P is')
        P.show()

    # return x,P
kalman_filter(x,P)
