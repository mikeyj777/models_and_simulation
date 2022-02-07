import cmath
import matplotlib.pyplot as plt
import numpy as np
import math

start = 0
stop = math.pi / 2

xy_in = np.linspace(start, stop, 50)
xy_in = [cmath.exp(1j * x) for x in xy_in]

xy_out = [cmath.log(x) for x in xy_in]

xy_out = [[x.real, x.imag] for x in xy_out]
xy_out = np.asarray(xy_out)

plt.plot(xy_out[:,0], xy_out[:,1])
plt.show()