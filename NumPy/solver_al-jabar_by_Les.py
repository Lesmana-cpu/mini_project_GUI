# WELCOME TO PROGRAM CREATED BY LESMANA (L7) wkwkwk

import numpy as np
import os

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print(" WELCOME TO PROGRAM CREATED BY LESMANA ".center(100,"="))
    
    print("pilih persamaan di bawah ini dlu bro/sis:")
    Lesmana_cpu = str(input("1.Al-jabar 2 variabel \n2.Al-jabar 3 variabel\n= ")) 

    if Lesmana_cpu == "1" or Lesmana_cpu.lower() == "al-jabar 2 variabel":
        print("\nmasukkin nilai x & y serta hasil, dari persamaan ke-1: ")
        x_1 = int(input("masukkin nilai x nya dulu: "))
        y_1 = int(input("teros nilai y: "))
        rst_1 = int(input("lalu masukkin hasilnya: "))
        
        print("\nmasukkin nilai x & y serta hasil, dari persamaan ke-2: ")
        x_2 = int(input("masukkin nilai x nya: "))
        y_2 = int(input("teros nilai y nya: "))
        rst_2 = int(input("lalu hasilnya: "))
        
        
        koefisien = np.array(([x_1, y_1],
                            [x_2, y_2],))
        
        hasil = np.array(([rst_1],
                        [rst_2]))
        
        Les_brain = np.linalg.solve(koefisien, hasil)
        x = Les_brain[0].item()
        y = Les_brain[1].item()
        print(f"jadi:\nnilai x = {x:.2f}\nnilai y = {y:.2f}")
        
    elif Lesmana_cpu == "2" or Lesmana_cpu.lower() == "al-jabar 3 variabel":
            print("masukkin nilai x, y, z serta hasil, dari persamaan ke-1: ")
            x_1 = int(input("masukkin nilai x nya dulu: "))
            y_1 = int(input("teros nilai y: "))
            z_1 = int(input("teros nilai z: "))
            rst_1 = int(input("lalu masukkin hasilnya: "))
            
            print("\nmasukkin nilai x, y, z serta hasil, dari persamaan ke-2: ")
            x_2 = int(input("masukkin nilai x nya: "))
            y_2 = int(input("teros nilai y nya: "))
            z_2 = int(input("teros nilai z nya: "))
            rst_2 = int(input("lalu masukkin hasilnya: "))
            
            print("\nmasukkin nilai x, y, z serta hasil, dari persamaan ke-3: ")
            x_3 = int(input("masukkin nilai x nya: "))
            y_3 = int(input("teros nilai y nya: "))
            z_3 = int(input("teros nilai z nya: "))
            rst_3 = int(input("lalu masukkin hasilnya: "))
            
            
            koefisien = np.array(([x_1, y_1, z_1],
                                [x_2, y_2, z_2],
                                [x_3, y_3, z_3],))
            
            hasil = np.array(([rst_1],
                            [rst_2],
                            [rst_3]))
            
            Les_brain = np.linalg.solve(koefisien, hasil)
            x = Les_brain[0].item()
            y = Les_brain[1].item()
            z = Les_brain[2].item()
            print(f"jadi:\nnilai x = {x:.2f}\nnilai y = {y:.2f}\nnilai z = {z:.2f}")
        
        
    else:
        print("masukkin pilihannya yang bener to!")
        continue
    
    end = str(input("apakah kamu pengen jajal lagi? (y/n): "))
    if end.lower() == "y":
        continue
    elif end.lower() == "n":
        print("\nthank's udah nyoba program buatan saya ini (Lesmana or L7)\n")
        nilai = int(input("masukkin ratingnya dlu cuy dari 1 sampe seterah kamu: "))
        if nilai <= 5 and nilai >= 1:
            print("parah!!")
        elif nilai >= 6 and nilai <= 10:
            print("Thank's")
        elif nilai >=10:
            print("GOOD JOB!!")
        else:
            print("LOL")
        break 
    else:
        print("masukkin pilihannya yang bener to!")
        continue
        
        




    



