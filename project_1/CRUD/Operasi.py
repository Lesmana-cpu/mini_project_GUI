from importlib.resources import contents
from . import Database
from .Util import random_string
import random
import string
import time
import os


def delete(no_buku):
    try:
        with open(Database.DB_NAME, mode="r", encoding="utf-8") as file:
            lines = file.readlines()
        
        # Pastikan nomor buku valid
        if no_buku < 1 or no_buku > len(lines):
            print("Nomor buku tidak valid!")
            return

        with open("data_temp.txt", mode="w", encoding="utf-8") as temp_file:
            for index, line in enumerate(lines):
                if index != no_buku - 1:  # Hanya tulis data yang tidak dihapus
                    temp_file.write(line)
    except Exception as e:
        print(f"Database error: {e}")
        return
    
    # Hapus file lama sebelum mengganti nama
    if os.path.exists(Database.DB_NAME):
        os.remove(Database.DB_NAME)
    
    os.rename("data_temp.txt", Database.DB_NAME)
    print("Data berhasil dihapus!")


def update(no_buku,pk,data_add,judul,penulis,tahun):
    data = Database.TEMPLATE.copy()
    
    data["pk"] = pk
    data["date_add"] = data_add
    data["judul"] = judul.strip() + Database.TEMPLATE["judul"][len(judul):]
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["tahun"] = str(tahun)
    
    data_str = f'{data["pk"]},{data["date_add"]},{data["judul"]},{data["penulis"]},{data["tahun"]}\n'

    panjang_data = len(data_str)
    
    try:
        with(open(Database.DB_NAME, mode="r+",encoding="utf-8")) as file:
            file.seek(panjang_data*(no_buku-1))
            file.write(data_str)
    except:
        print("error dalam update data")
        
def create(tahun, judul, penulis):
    data = Database.TEMPLATE.copy()
    
    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["judul"] = judul.strip()
    data["penulis"] = penulis.strip()
    data["tahun"] = str(tahun)
    
    data_str = f'{data["pk"]},{data["date_add"]},{data["judul"]},{data["penulis"]},{data["tahun"]}\n'

    try:
        with open(Database.DB_NAME, mode="a", encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Gagal menambahkan data")
        
def create_first_data(): 
    penulis = input("Penulis: ")
    judul = input("Judul: ")
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

    
    data = Database.TEMPLATE.copy()
    
    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["tahun"] = str(tahun)
    
    data_str = f'{data["pk"]},{data["date_add"]},{data["judul"]},{data["penulis"]},{data["tahun"]}\n'
    try:
        with open(Database.DB_NAME,mode="w",encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Udah lah gagal cuy!!")
        
def read(**kwargs):
    
    try:
        with open(Database.DB_NAME, mode="r") as file:
            content = file.readlines()
            jumlah_buku = len(content)
            if "index" in kwargs:
                index_buku = kwargs["index"]-1
                if index_buku < 0 or index_buku > jumlah_buku:
                    return False
                else:
                    return content[index_buku]
            else:    
                return content
    except:
        print("Database error")
        return False