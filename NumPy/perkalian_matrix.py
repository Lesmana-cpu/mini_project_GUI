import numpy as np

a = np.array(([1,2],
              [3,4]))

b = np.ones((2,2))

print(f"matrix a = \n{a}")
print(f"matrix b = \n{b}")

# perkalian matrix

c_1 = np.dot(a,b)
c_2 = a.dot(b)

print(f"hasil perkalian a & b = \n{c_1}")
print(f"hasil perkalian a & b = \n{c_2}")