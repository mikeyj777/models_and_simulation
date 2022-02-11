import cmath

seed = 1j
ans = cmath.sqrt(seed)
print(ans)
for i in range(100):
    ans = cmath.sqrt(seed * ans)
    print(ans)