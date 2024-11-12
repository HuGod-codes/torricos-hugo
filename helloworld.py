import numpy as np

a = np.array([[4, 1], [3, 2]])
b = np.array([[9, 4], [4, 3]])

c = np.dot(a, b)

print(c)
print(np.linalg.inv(c))
print(c.T)