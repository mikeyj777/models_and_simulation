import cmath
import matplotlib.pyplot as plt
import numpy as np
import math

def iterate(x_in, c=0.25, maxval = 2):
    
    if x_in.real > maxval:
        return None
    iters = 50

    z = x_in
    for i in range(iters):
        z = z**2 + c
        if z.real > maxval:
            return None
    
    return z

start = 0
stop = math.pi * 2

xy_in = np.linspace(start, stop, 1000)
# xy_in = [cmath.exp(1j * x) for x in xy_in]


xy_out = [iterate(x) for x in xy_in]
xy_out = [[x.real, x.imag] for x in xy_out if x is not None]
# xy_out = [cmath.log(x)/cmath.log(1j) for x in xy_in]

# xy_out = [[x.real, x.imag] for x in xy_out]
xy_out = np.asarray(xy_out)

if len(xy_out) > 0:
    plt.plot(xy_out[:,0], xy_out[:,1])
    plt.show()