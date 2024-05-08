if nr < 0 or nr >= len(warehouse) or nc < 0 or nc >= len(warehouse[0]) or warehouse[nr][nc] == '#':
    #stochatic motion hits wall
    stochastic_cost = (motion_cost[(k+l) % len(motion)] + 100 + values[i][j]) * s_probabilities[l + 2]
else:
    # stochastic motion is normal
    stochastic_cost = (motion_cost[(k+l) % len(motion)] + warehouse_cost[nr][nc] + values[nr][nc])*s_probabilities[l+2]