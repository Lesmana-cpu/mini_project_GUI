import numpy as np

a = np.array(([1,2,3],
              [4,5,6]
              ))

print(f"matrix a degan ukuran: {a.shape}")
print(a)

# transpose matrix
print(f"\ntranspose matrix a :")
print(a.transpose())
# or
print(f"\n{np.transpose(a)}")
# or
print(f"\n{a.T}")
                                     
print(f"\nmatrix a degan ukuran: {a.shape}")  
print(a)


# flatten array \ vector baris
print(f"\nflatten array a :")
print(a.ravel())
# or
print(np.ravel(a))


# reshape array
print("\nreshape matrix a:")
print(a.reshape(3,2))

# resize matrix
print("\nresize matrix a:")
# print(a.resize(3,2))  <-- error
a.resize(3,2)
print(a)

