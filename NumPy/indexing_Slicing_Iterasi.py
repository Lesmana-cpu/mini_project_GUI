import numpy as np

a = np.arange(11)**2
print(f"a = {a}")

print(type(a))

# mengambil nilai
print(f"elemen ke 1 dari a = {a[0]}")
print(f"elemen ke 5 dari a = {a[4]}")
print(f"elemen akhir from a = {a[-1]}")

# slicing
print(f"elemen ke 1 sampai 5 dari a = {a[0:6]}")  
print(f"elemen 3 sampai akhir = {a[2:]}")
print(f"elemen awal sampai 7 = {a[:7]}")


# iterasi
for index, i in enumerate(a):
    print(f"value {index} = {i}")
    