import numpy as np

# Membuat array 1D
arr1 = np.array([1, 2, 3, 4, 5])
print("Array 1D:", arr1)

# Membuat array 2D
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("Array 2D:\n", arr2)

# Operasi dasar pada array
print("Penjumlahan arr1 + 10:", arr1 + 10)
print("Perkalian arr2 * 2:\n", arr2 * 2)

# Mengakses elemen array
print("Elemen pertama arr1:", arr1[0])
print("Elemen baris 1 kolom 2 arr2:", arr2[1, 2])