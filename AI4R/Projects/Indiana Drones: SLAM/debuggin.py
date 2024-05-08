potential_dist = [0.0, 0.1, 0.2, 0.3, .4, .5, .6, .7, .8, .9, .99]
potential_steering = [0.0, 0.1, 0.2, 0.3, .4, .5, .6, .7, .8, .9, .99, -0.1, -0.2, -0.3, -.4, -.5, -.6, -.7, -.8, -.9, -.99]
# potential_dist = [1.2]
# potential_steering = [1]
max_dist = 0
max_steering = 0

for i in range(len(potential_dist)):
    for j in range(len(potential_steering)):
        print(potential_dist[i])

