import cmath
import numpy as np
import matplotlib.pyplot as plt

seed = 1j
ans = cmath.sqrt(seed)
output = [[ans.real, ans.imag]]

for i in range(100):
    ans = cmath.sqrt(seed * ans)
    output.append([ans.real, ans.imag])

output = np.asarray(output)
x = output[:,0]
y = output[:,0]

plt.scatter(x,y)
plt.show()