import os
import CRUD as CRUD

if __name__ == "__main__":
    sistem_operasi = os.name
    
    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")
        
    print("SELAMAT DATANG DI PROGRAM")
    print("DATABASE PEERPUSTAKAAN")
    print("=========================")
    
    # check database ada atau tidak
    CRUD.init_console()
    
    while True:
        match sistem_operasi:
            case "posix": os.system("clear")
            case "nt": os.system("cls")
        
        print("SELAMAT DATANG DI PROGRAM")
        print("DATABASE PEERPUSTAKAAN")
        print("=========================")
        print(f"1. Create Data")
        print(f"2. Read Data")
        print(f"3. Update Data")
        print(f"4. Delete Data\n")
        
        user_input = input("masukkan pilihan anda = ")
        
        match user_input:
            case "1": CRUD.create_console()
            case "2": CRUD.read_console()
            case "3": CRUD.update_console()
            case "4": CRUD.delete_console()
        
        is_done = input("Apakah sudah selesai (y/n)?\n")
        if is_done == "y" or is_done == "Y":
            break
        
    print("Program Telah Berakhir, Thank's!!")