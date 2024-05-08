import math

p = [.2, .2, .2, .2, .2]
world = ['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'red']
motions = [1,1]
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1



def sense(p, Z): #p = probability, Z = pHit where world[iter] == target
    q = []
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit)*pMiss))
        s = sum(q)
    for i in range(len(p)):
        q[i] = q[i] / s #New probability / sum of new probabilities
    return q

def move(p, U): #p is the array of probabilities, U is the number of movements
    q = []
    entropy = 0
    for i in range(len(p)):
    s = pExact * p[(i-U) % len(p)]
        # s = s + pUndershoot * p[(i-U-1) % len(p)]
        # s = s + pOvershoot * p[(i-U-1) % len(p)]
        # entropy = entropy + (p[i] * math.log(p[i]))
        q.append(s)


    #print(entropy)

    return q

for k in range(len(measurements)):
    p = sense(p, measurements[k])
    p = move(p, motions[k])


print(p)