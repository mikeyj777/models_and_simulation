import numpy as np
from itertools import permutations


# def permute(a, l, r): 
#     if l==r: 
#         permuts.append(a)
        
#     else: 
#         for i in range(l,r+1): 
#             a[l], a[i] = a[i], a[l] 
#             permute(a, l+1, r) 
#             a[l], a[i] = a[i], a[l] # backtrack 

a = [*range(1,10)]

permuts = list(permutations(a))
print(permuts[-2])
b = np.asarray(permuts[len(permuts)-2]).reshape(3,3)
c = b.flatten()

print(b)
print(c)


print(permuts)