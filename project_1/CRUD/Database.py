from . import Operasi

DB_NAME = "data.txt"
TEMPLATE = {
    "pk":"XXXXXX",
    "date_add":"yyyy-mm-dd",
    "judul":255*" ",
    "penulis":255*" ",
    "tahun":"yyyy"
    
}

def init_console():
    try:
        with open(DB_NAME, mode="r", encoding="utf-8") as file:
            print("database tidak tersedia")
    except:
        print("Databse tidak di temukan, silahkan membuat database baru")
        Operasi.create_first_data()