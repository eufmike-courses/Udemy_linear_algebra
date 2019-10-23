#%%
import numpy as np

#%%
A = np.random.randn(4, 6)
B = np.random.randn(4, 6)

dps = np.zeros((A.shape[1], 1))

for i in range(A.shape[1]):
    dps[i, :] = np.dot(A[:, i], B[:, i])

print(dps)
#%%
# pythagoras
v1 = np.array([[1, 2, 3, 4, 5, 6,]])
vlength = np.sqrt(np.sum(v1*v1, keepdims=True))
print(vlength)
#%%
vlength2 = np.sqrt(np.dot(v1, v1.T))
print(vlength2)

#%%
w1 = np.array([[1, 3, 5]])
w2 = np.array([[3, 4, 2]])
w3 = w1 * w2
print(w3)
w3_dot = np.dot(w1, w2.T)
print(w3_dot)



#%%
