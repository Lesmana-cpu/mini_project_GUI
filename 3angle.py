# sisi = int(input('mau sampai berapa '))

# L = 1
# for i in range(sisi):
#     print("*" * L)
#     L += 1 
    
    
    
# 2. while
jumlah = int(input('masukkan angka nya '))
nol = 1
jumlah += 1


while nol < jumlah:
    print('*' * nol )
    nol += 1
    
# 3.while true
count = 14
x = 1
spasi = int(count/2)
while True:
    if x%2 != 0:
        print(" "*spasi, '+' * x)
        pr = " "*spasi, '+' * x
        spasi -= 1
        x += 1
    else:
        x += 1
        continue

    if x > count:
        break
        
        
print(len(pr))