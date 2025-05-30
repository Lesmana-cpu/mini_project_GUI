import numpy as np

# list python
a = [1,2,3,4,5]
b= [6,7,8,9,10]

# array numpy
a_np = np.array([1,2,3,4,5])
b_np = np.array([6,7,8,9,10])
# ELEMENTWISE OPERATIONS

# penjumlahan, pengurangan, perkalian, pembagian di list python:
hasil = a + b
print(f"hasil penjumlahan list a + b = {hasil}")

# hasil = a - b
# print(f"\nhasil pengurangan list a - b = {hasil}")  <-- akan error

# hasil = a * b
# print(f"\nhasil perkalian list a * b = {hasil}")   <-- ini juga akan error

# hasil = a / b
# print(f"\nhasil pembagian list a / b = {hasil}")   <-- ini juga error


# penjumlahan, pengurangan, perkalian, pembagian, kuadrat di array numpy:
hasil = a_np + b_np
print(f"\nhasil penjumlahan array a_np + b_np = {hasil}")
hasil = a_np - b_np
print(f"\nhasil pengurangan array a_np - b_np = {hasil}")
hasil = a_np * b_np
print(f"\nhasil perkalian array a_np * b_np = {hasil}")
hasil = a_np / b_np
print(f"\nhasil pembagian array a_np / b_np = {hasil}")
hasil = a_np ** 2
print(f"\nhasil kuadrat array a_np = {hasil}")

# multidimensional array numpy

c = np.array([[1,2,3],[4,5,6]])
d = np.array([[7,8,9],[-1,-7,-3]])

hasil = c + d
print(f"\nhasil penjumlahan array c + d = {hasil}")
hasil = d**2
print(f"\nhasil kuadrat array d = {hasil}")

# contoh lain
j = 1,2,3,4,5
k = 6,7,8,9,10
l = 11,12,13,14,15

x = np.array([j])
y = np.array([k])
z = np.array([l])


hasil = x + y
print(f"\nhasil penjumlahan array x + y = {hasil}")

hasil = y - z
print(f"\nhasil pengurangan array z - j = {hasil}")


h = sum(20,98)
print(h)
