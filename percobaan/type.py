from stat import IO_REPARSE_TAG_APPEXECLINK


w = 13
print('data =', w, ',',  'typenya = ', type(w))

x = float(w)
print('data =', x, ',', 'typenya = ', type(x))

y = str(w)
print('data =', y, ',', 'typenya = ', type(y))

z = bool(w)
print('data =', z, ',', 'typenya = ', type(z))

p = bool(int(input("masukkan input")))

print(type(p))

print(IO_REPARSE_TAG_APPEXECLINK)