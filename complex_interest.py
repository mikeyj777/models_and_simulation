import matplotlib.pyplot as plt
import numpy as np

ans = []
mags = []

a = complex(1,1)

ans.append(a)
mags.append(abs(a))

for i in range(1,100):
    a *= complex(1,1)
    ans.append(a)
    mags.append(abs(a))

ans = np.asarray(ans)

x = ans.real
y = ans.imag

# plt.scatter(x, y, label="star", marker="*", color="green", s=30)
# plt.xlabel('real axis')
# plt.ylabel('imaginary axis')
# plt.title('complex numbers')
# plt.legend()
# plt.show()

plt.semilogy(mags, color="red")
plt.xlabel('year')
plt.ylabel('magnitude')
plt.show()
