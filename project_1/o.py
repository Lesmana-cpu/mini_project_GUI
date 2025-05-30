def create_console():
    print("\n\n"+"="*100)
    print("Silahkan tambah data buku\n")
    penulis = input("penulis\t: ")
    judul = input("Judul\t: ")
    while True:
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
              if tahun >= 1000 and tahun < 3000:
                  break
              else:
                  print("Hanya boleh antara 1000-3000 Masehi!!") 
            else:
                print("Tahun harus 4 digit nomer!!")
                
        except:
            print("tahun harus angka, silahkan masukkan tahun yang benar!!!")    

    Operasi.create(tahun,judul,penulis)
    print("\nBerikut adalah data baru anda:")
    read_console()



def create(tahun,judul,penulis):
    data = Database.TEMPLATE.copy()
    
    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)
    
    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'

    try:
        with open(Database.DB_NAME,mode="a",encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Data sulit di tambahkan, gagal lagi")
        
        
        
        
        
        
        
        
        
        
        
def update_console():
    read_console()
    while True:
        print("Silahkan pilih nomor buku yang akan di update")
        no_buku = int(input("Nomor Buku: "))
        data_buku = Operasi.read(index=no_buku)
        
        if data_buku:
            break
        else:
            print("nomor buku nya ga ada, masukkan yg benar!!")
        
        data_break = data_buku.split(",")
        pk = data_break[0]
        data_add = data_break[1]
        judul = data_break[2]
        penulis = data_break[3]
        tahun = data_break[4][:-1]

    while True:
        # data yang ingin di update
        print("\n"+"="*100)
        print("Silahkan pilih data apa yang ingin anda ubah")
        print(f"1. judul\t: {judul:.40}")   
        print(f"2. penulis\t: {penulis:.40}")
        print(f"3. tahun\t: {tahun:.4}")
        
        # memilih untuk update
        pilihan = input("Pilih data [1,2,3]: ")
        print("\n"+"="*100)
        match pilihan:
            case "1": judul = input("judul\t: ")
            case "2": penulis = input("penulis\t: ")
            case "3":
                while True:
                    try:
                        print("Tahun   : ", end="")
                        tahun = int(input())
                        if len(str(tahun)) == 4 and 1000 <= tahun < 3000:
                            break
                        print("Tahun harus 4 digit antara 1000-3000!")
                    except ValueError:
                        print("Tahun harus angka!") 
            case _: print("index yg di pilih ga cocok")
            
        print("\nBerikut adalah data baru anda:")
        print(f"1. judul\t: {judul:.40}")   
        print(f"2. penulis\t: {penulis:.40}")
        print(f"3. tahun\t: {tahun:.4}")    
        is_done = input("Apakah data sudah selesai di update (y/n)?\n")
        if is_done == "y" or is_done == "Y":
            break
 
    Operasi.update(no_buku,pk,data_add,judul,penulis,tahun)