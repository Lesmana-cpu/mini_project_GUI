import numpy as np

a = np.array(([1, 2, 3]))
b = np.array(([4, 5, 6]))

a_matrix = np.ones((2, 3))
b_matrix = np.zeros((2, 3))

# stacking matrix / menumpuk matrix

c = np.hstack((a,b))   # <-- horizontal stacking
print(f"result stacking (horizontal) matrix a & b = \n{c}")
d = np.vstack((a,b))   # <-- vertical stacking
print(f"result stacking (vertical) matrix a & b = \n{d}")


c_matrix = np.hstack((a_matrix, b_matrix))  # <-- horizontal stacking
print(f"result stacking (horizontal) matrix a_matrix & b_matrix = \n{c_matrix}")
d_matrix = np.vstack((a_matrix, b_matrix))  # <-- vertical stacking
print(f"result stacking (vertical) matrix a_matrix & b_matrix = \n{d_matrix}")