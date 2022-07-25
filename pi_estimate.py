import math
import numpy as np
import matplotlib.pyplot as plt


r = 1

def get_y_coord(x, r):
    return math.sqrt(r**2 - x**2)

def get_dist_bet_points(x0, y0, x1, y1):
    return math.sqrt((x1-x0)**2 + (y1-y0)**2)

output = []
for mag_steps in range(1,7):
    num_steps = 10**mag_steps

    x_min = -1
    x_max = 1

    x_step = (x_max - x_min) / num_steps

    x = x_min
    y = get_y_coord(x, r)
    estimated_half_circum = 0
    while x <= (x_max - x_step):
        x0 = x
        y0 = y
        x += x_step
        y = get_y_coord(x, r)
        estimated_half_circum += get_dist_bet_points(x0, y0, x, y)
    act_half_circum = math.pi * r
    err = abs(act_half_circum - estimated_half_circum) / act_half_circum
    print({
        'mag_steps': mag_steps,
        'act_half_circum': act_half_circum,
        'estimated_half_circum': estimated_half_circum,
        'pct err': err,
    })
    output.append([mag_steps, err])

output = np.asarray(output)
x = output[:,0]
y = output[:,1]

plt.scatter(x,y)
plt.yscale('log')
plt.show()