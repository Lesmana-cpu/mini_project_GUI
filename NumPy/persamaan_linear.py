import numpy as np

A = np.array([(2,3), (1,2)])
Y = np.array([23,14])

A_inv = np.linalg.inv(A)

x = np.dot(A_inv, Y)
print(x)

# cara lain
x2 = np.linalg.solve(A, Y)
print(x2)