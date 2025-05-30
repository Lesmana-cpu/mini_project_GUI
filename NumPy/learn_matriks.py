import numpy as np

matrix_a = np.array(([1, 2],
                     [3, 4]))
print(f"matrix_a = \n{matrix_a}")

matrix_b = np.array(([5, 6],
                     [7, 8]))
print(f"matrix_b = \n{matrix_b}")

c = np.dot(matrix_a, matrix_b)
print(f"hasil matrix_a x matrix_b =\n{c}")

x = np.array(([5,6,7],
             [15,67,98]))

y = np.array(([987,678],
              [521,777],
              [765,876]))

z = np.dot(x,y)
print(f"hasil matrix x kali y =\n{z}")


