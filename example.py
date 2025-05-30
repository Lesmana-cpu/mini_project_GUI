import numpy as np

list_a = [1,2,3,4]
vector_a = np.array([1,2,3,4,5])

print(f"ini list_a = {list_a}")
# print(f"list_a ^2 = {list_a**2}")  <-- ini akan error

print(f"ini vector_a = {vector_a}")
print(f"vektor_a ^2 = {vector_a**2}")
print(f"vector_a -5 = {vector_a-5}")

matrix_b = np.array([(1,2,3), (4,5,6), (7,8,9)])
print(f"\nmatrix = \n{matrix_b}")

zeros_c = np.zeros((3,3)) # <-- np.zeros((P,L))
print(f"\nzeros_c:\n{zeros_c}")

ones_d = np.ones((3,3)) # <-- np.ones((P,L))
print(f"\nones_d:\n{ones_d}")


jumlah = matrix_b + matrix_b**2 + ones_d
print(f"\nhasil penjumlahan dari matrix_b + matrix_b**2 + ones_d adalah:\n{jumlah}")
