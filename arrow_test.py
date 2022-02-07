import numpy as np
import matplotlib.pyplot as plt
import math, cmath
import decimal

def float_range(start, stop, step):
  while start < stop:
    yield float(start)
    start += decimal.Decimal(step)

def fxn(x):
    return x**2

ans = []
for x in float_range(10,10,0.1):
    ans.append([x, fxn(x)])

plt.arrow(x,y,dx,dy,head_width=0.05, head_length=0.1)
plt.show()