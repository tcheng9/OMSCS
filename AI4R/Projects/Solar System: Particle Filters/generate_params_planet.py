import random
import math

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

PI = math.pi

for i in range(1, 10+1):
    test_case = i
    sun_mass = random.uniform(40, 60)
    sun_r = [random.uniform(-.1, .1), random.uniform(-.1, .1)]
    planets = []
    num_planets = num_planets = 1 if 2 <= i <= 5 else random.randint(2, 5)
    dist_from_sun = 0
    for _ in range(num_planets):
        dist_from_sun += random.uniform(.9, 1)
        angle = random.uniform(0, 2*math.pi)
        planet_init_x = dist_from_sun * math.cos(angle) + sun_r[0]
        planet_init_y = dist_from_sun * math.sin(angle) + sun_r[1]
        planet_mass = random.uniform(1, 1000)      # 1 <= planet_mass <= 1000
        planets.append(((planet_init_x, planet_init_y), planet_mass))
    target_dist = random.uniform(.7, 4)
    target_angle = random.uniform(0, 2*math.pi)
    target_init_x = target_dist * math.cos(target_angle)
    target_init_y = target_dist * math.sin(target_angle)
    target_mass = math.floor(random.uniform(1_000, 100_000)) # kg
    target = ((target_init_x, target_init_y), target_mass)
    elliptical_orbit_factor = 1 if i < 8 else random.uniform(.5, .75)
    map_seed = random.randint(1, 5000)
    g_measurement_noise = random.uniform(1e-7, 1e-8)
    measurement_noise = random.uniform(1e-7, 1e-8)
    pi_measurement_noise = random.uniform(.1, 1)

    output = """'test_case': {},
     'sun_mass': {},
     'sun_r': {},
     'planets': {},
     'elliptical_orbit_factor': {},
     'target': {},
     'map_seed': {},
     'g_measurement_noise': {},
     'pi_measurement_noise': {},
     'max_steps': 300
""".format(i, sun_mass, sun_r, planets, elliptical_orbit_factor, target, map_seed, g_measurement_noise, pi_measurement_noise)

    print("    {" + output + "    },")
