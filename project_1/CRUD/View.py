from . import Operasi
import time


def delete_console():
    read_console()
    while True:
        print("Silahkan pilih nomor buku yang akan di delete")
        no_buku = int(input("Nomor Buku: "))
        data_buku = Operasi.read(index=no_buku)
        
        if data_buku:
            data_break = data_buku.split(",")
            pk = data_break[0]
            data_add = data_break[1]
            judul = data_break[2]
            penulis = data_break[3]
            tahun = data_break[4][:-1]
            
            # data yang ingin di update
            print("\n"+"="*100)
            print("Silahkan pilih data apa yang ingin anda hapus")
            print(f"1. judul\t: {judul:.40}")   
            print(f"2. penulis\t: {penulis:.40}")
            print(f"3. tahun\t: {tahun:.4}")
            
            is_done = input("Are you sure? (y/n)?\n")
            if is_done == "y" or is_done == "Y":
                Operasi.delete(no_buku)
                break
        else:
            print("nomor buku nya ga ada, masukkan yg benar!!")


def update_console():
    read_console()
    while True:
        print("Silahkan pilih nomor buku yang akan di update")
        no_buku = int(input("Nomor Buku: "))
        data_buku = Operasi.read(index=no_buku)
        
        if data_buku:
            data_break = data_buku.split(",")
            if len(data_break) < 5:  # Validasi jumlah data
                print("Error: Format data buku tidak valid!")
                return
                
            pk = data_break[0]
            data_add = data_break[1]
            judul = data_break[2]
            penulis = data_break[3]
            tahun = data_break[4][:-1]  # Hapus newline di akhir
            
            while True:
                print("\n"+"="*100)
                print("Silahkan pilih data apa yang ingin anda ubah")
                print(f"1. judul\t: {judul:.40}")   
                print(f"2. penulis\t: {penulis:.40}")
                print(f"3. tahun\t: {tahun:.4}")
                
                pilihan = input("Pilih data [1,2,3]: ")
                print("\n"+"="*100)
                
                match pilihan:
                    case "1": judul = input("judul\t: ")
                    case "2": penulis = input("penulis\t: ")
                    case "3":
                        while True:
                            try:
                                tahun = int(input("Tahun\t: "))
                                if len(str(tahun)) == 4 and 1000 <= tahun < 3000:
                                    break
                                print("Tahun harus 4 digit antara 1000-3000!")
                            except ValueError:
                                print("Tahun harus angka!")
                    case _: print("Pilihan tidak valid!")
                
                print("\nBerikut adalah data baru anda:")
                print(f"1. judul\t: {judul:.40}")   
                print(f"2. penulis\t: {penulis:.40}")
                print(f"3. tahun\t: {tahun:.4}")    
                
                is_done = input("Apakah data sudah selesai di update (y/n)? ")
                if is_done.lower() == "y":
                    Operasi.update(no_buku, pk, data_add, judul, penulis, tahun)
                    print("Data berhasil diupdate!")
                    return
                break
        else:
            print("Nomor buku tidak valid, silahkan coba lagi!")


def create_console():
    print("\n" + "=" * 50)
    print("Silahkan tambah data buku".center(50))
    print("=" * 50 + "\n")
    
    print("Judul   : ", end="")
    judul = input().strip()
    print("Penulis : ", end="")
    penulis = input().strip()
    
    while True:
        try:
            print("Tahun   : ", end="")
            tahun = int(input())
            if len(str(tahun)) == 4 and 1000 <= tahun < 3000:
                break
            print("Tahun harus 4 digit antara 1000-3000!")
        except ValueError:
            print("Tahun harus angka!")

    Operasi.create(tahun, judul, penulis)
    print("\n" + "=" * 50)
    print("Data berhasil ditambahkan!".center(50))
    print("=" * 50 + "\n")
    
    
    
    
# AI :
def read_console():
    data_file = Operasi.read()
    if not data_file:
        print("\nTidak ada data yang ditemukan")
        return
    
    # Header
    print("\n" + "=" * 80)
    print(f"{'No':<5} | {'Judul':<30} | {'Penulis':<25} | {'Tahun':<5}")
    print("-" * 80)
    
    # Data
    for index, data in enumerate(data_file):
        data_break = data.strip().split(",")
        
        # Pastikan data memiliki minimal 5 elemen agar tidak terjadi error
        if len(data_break) < 5:
            print(f"[WARNING] Data pada baris {index+1} rusak atau tidak lengkap: {data.strip()}")
            continue  # Lewati baris yang rusak
        
        # Ambil data dengan aman
        pk = data_break[0].strip()
        date_add = data_break[1].strip()
        judul = data_break[2].strip()
        penulis = data_break[3].strip()
        tahun = data_break[4].strip()
        
        print(f"{index+1:<5} | {judul:<30} | {penulis:<25} | {tahun:<5}")
    
    # Footer
    print("=" * 80 + "\n")

    