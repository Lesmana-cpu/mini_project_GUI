import numpy as np
import os
os.system('cls' if os.name == 'nt' else 'clear')

a = np.floor(np.random.randn(3,3))*7  # <-- floor merubah ke int
print(a)

print(f"nilai max from a: {a.max()}")
print(f"posisi max from a: {a.argmax()}")
print(f"nilai min from a: {np.min(a)}")
print(f"posisi min from a: {a.argmin()}")

# urutin
print("="*25 + " MENGURUTKAN a " + "="*25)
print(f"urutin a: {np.sort(a)}")
print(f"berdasarkan argument: {np.argsort(a)}") # <-- dari yang terkecil ke terbesar, berdasarkan index


