import numpy as np
import os
os.system('cls' if os.name == 'nt' else 'clear')

# membuat matrix dengan tipe data bebas (x)
a = np.array(([1,0,3], [4,5,6]), dtype = bool)
print(a)

# membuat array with function
def kuadrat(baris, kolom):
    return kolom **2
    return np.full((baris, kolom), 2)

def jumlah(baris, kolom):
    return (baris + kolom)
    return np.full((baris, kolom), 2)

# x = np.fromfunction(fungsi, matrix, tipe)  <-- rumus
b = np.fromfunction(kuadrat, (1,7), dtype = int)
c = np.fromfunction(jumlah, (5,5), dtype = float)
print(f"b: \n{b}")
print(f"c: \n{c}\n")

# membuat matrix / array with iterable
iterable_L7 = (x ** 2 for x in range(1,19,2))
d = np.fromiter(iterable_L7, dtype = int)
print(d)

# multitype array
tipe = [('nama', 'S17'), ('tinggi', float)]

data = [('Asep', 170),
        ('Leo', 180),
        ('Jennifer', 175)
]

e = np.array (data, dtype = tipe)
print(e[2])



t = [("ngasa", "S17"), ("tinggi", bool)]

date = [("kidu", 7),
        ("kadu", 0),
        ("kede", 1)
        
]

f = np.array(date, dtype = t )
print(f)