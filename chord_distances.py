import numpy as np
import math
import random
import matplotlib.pyplot as plt

epochs = 5000

radius = 1

for n in range(epochs):
    dists = []
    means = []
    for i in range(epochs):
        x1 = 2 * radius * random.random() - radius
        y1 = math.sqrt(radius**2 - x1**2)
        if random.random() < 0.5:
            y1 = -y1
        x2 = 2 * radius * random.random() - radius
        y2 = math.sqrt(radius**2 - x2**2)
        if random.random() < 0.5:
            y2 = -y2
        dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
        dists.append(dist)
    dists = np.asarray(dists)
    means.append(np.mean(dists))
    print(np.mean(dists))

means = np.asarray(means)
print(np.mean(means))