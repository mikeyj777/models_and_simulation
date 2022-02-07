import numpy as np
import matplotlib.pyplot as plt
import math, cmath
import decimal

def float_range(start, stop, step):
  while start < stop:
    yield float(start)
    start += decimal.Decimal(step)

def polynom(z):
    return z**3 - z**2 + 4

inputs = []
outputs = []
dels = []

common_bounds = [-5, 5, 0.1]

r_start, r_end, r_step = common_bounds
c_start, c_end, c_step = common_bounds

# r_start, r_end, r_step = [0.9, 1.1, 0.01]
# c_start, c_end, c_step = [0.9, 1.1, 0.01]


r = r_start
while r <= r_end:
    c = c_start
    while c <= c_end:
        inputs.append([r, c])
        ans = polynom(complex(r, c))
        outputs.append([ans.real, ans.imag])
        dels.append([ans.real - r, ans.imag - c])
        c += c_step
    r += r_step

outputs = np.asarray(outputs)
inputs = np.asarray(inputs)
dels = np.asarray(dels)

x_out = outputs[:,0]
y_out = outputs[:,1]

x_in = inputs[:,0]
y_in = inputs[:,1]

dx = dels[:,0]
dy = dels[:,1]

# alpha = np.hypot(inputs[:,0], inputs[:,1])
# alpha /= (np.max(alpha) - np.min(alpha))

# color = (2**24 - 1) * alpha
# color = color.astype(int)
# vhex = np.vectorize(hex)

# color = vhex(color)

# color = np.char.replace(color, '0x', '#')

# for i in range(len(color)):
#     if len(color[i]) != 7:
#         a = len(color[i])
#         z = '0'
#         num_zeros = 7 - a
#         z *= num_zeros
#         color[i] = '#' + z + color[i][1:]

fig, ax = plt.subplots()

AB = ax.scatter(x_in, y_in, c = 'blue', marker = 'o', s = 0.1, zorder = 3)
CD = ax.scatter(x_out, y_out, c = 'red', marker = 'o', s = 0.1, zorder = 2)

# ax.quiver(x_in, y_in, dx, dy, angles='xy', scale_units='xy', scale=1, width = 1e-3)

ax.grid(True)
fig.tight_layout()

plt.show()

# plt.arrow(x,y,dx,dy,head_width=0.05, head_length=0.1)
# plt.scatter(x, y, s = 0.1, c = color)
# plt.show()






