# from rait import *
#
# a = matrix([[3,5,7, 9], [19, 123, 12, 13], [6, 31, 12, 31]])
# ####
# #Expanding matrices
# ####
#
# #Omega expansion testing
# b = matrix([[1,0], [0,1]])
# b_dimx = b.dimx
# b_dimy = b.dimy
#
# # row = len(b)
# # col = len(b[0])
# # print('before')
# # b.show()
#
# row = list(range(b.dimx))
# col = list(range(b.dimy))
# b = b.expand(b_dimx+1, b_dimy+1, row, col)
# #
# # print('after')
# # b.show()
#
#
# #Xi expansion Testing
#
# xi = matrix([[1.0], [1.0]])
# xi_dimx = xi.dimx
# xi_dimy = xi.dimy
#
# row = list(range(xi.dimx))
# col = list(range(xi.dimy))
#
# xi.show()
# xi = xi.expand(xi.dimx + 2, xi.dimy, row, col)
# xi.show()
#
#
#
# ##############################################################
# #


# _dict = {282589425900826719688085225668504563362: {'distance': 2.986106590746365, 'bearing': 1.5790924612915944, 'type': 'B',
#                                            'radius': 0.2},
#  148224656581792672884491322522799971648: {'distance': 2.932896779434399, 'bearing': -3.120182127536145, 'type': 'A',
#                                            'radius': 0.5},
#  137551100291914355458239239134341445524: {'distance': 3.934359688171381, 'bearing': -0.01661414864955102, 'type': 'C',
#                                            'radius': 0.3}}
#
# for key, val in _dict.items():
#     print(key)
#     print(val)

from math import *


def truncate_angle(t: float):
    """
    Truncate the angle between -PI and PI

    Args:
        t: angle to truncate.

    Returns:
        Truncated angle.
    """
    return ((t + pi) % (2 * pi)) - pi

potential_orientations = [0, pi/4, pi/2, 3*pi/4, .99*pi, -pi/4, -pi/2, -3*pi/4, -.99*pi]
potential_dist = 1
x,y = 0,0
for i in range(len(potential_orientations)):
    robot_orientation = 0.0 #self.orientation
    x, y = 0, 0 #self.x,y
    a = robot_orientation + potential_orientations[i]
    truncated_a = truncate_angle(a)
    print(truncated_a)
    ###
    #apply motion -> x + dx, y + dy
    ###
    x += .5

    ###
    #calc ed
    ###

    '''
    if ed < curr_ed:
        choose best steering
        choose best dist to move
        
    '''


#truncate oirentation

