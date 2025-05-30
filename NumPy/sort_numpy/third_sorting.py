import numpy as np

tipe = [('nama', 'S17'), ('tinggi', float)]

data = [('jajang', 175),
        ('Les', 180),
        ('ucuy', 170)
]

a = np.array(data, dtype = tipe)
print(a)

print(np.sort(a, order = 'tinggi')) # <-- sorting berdasarkan tinggi
print(np.sort(a, order = 'nama')) # <-- sorting berdasarkan nama    