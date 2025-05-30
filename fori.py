# x = str(input('masukkan simbol atau karkaternya '))
# y = int(input('mulainya dari berapa? '))
# s = int(input('full nya berapa? '))
# for z in range(y, s):
#     if z >= 10:
#         print(f'loopinng ke  {z} -->{x.rjust(54)}')
#     else:
#         print(f'loopinng ke   {z} -->{x.rjust(54)}')
#     x += (x**0)
    
# while True:
#     huruf = str(input('masukkan kata kuncinya '))
#     for h in huruf:
#         if h == 'o':
#             print(f'{h}, kamu cerdas')
#         else:
#             print('nothing')
#         pilihan = str(input('apakah kamu ingin ulang y/n'))
#     if pilihan == 'n':
#      break



angka = int(input('masukkan angkanya '))
a = angka
b = 1


for angka in range(a, b):
    print(a)
    a, b = b , a+b    
    