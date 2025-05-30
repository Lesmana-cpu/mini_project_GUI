while True:
    pilihan = str(input("Kamu ingin mengonversi dari suhu apa? (celcius/reamur/fahrenheit/kelvin) \n")).lower()

    if pilihan == "celcius":
        perubahan = str(input("Kamu mau ubah suhu Celcius ke suhu apa? (reamur/fahrenheit/kelvin) \n")).lower()
        celcius = float(input("Masukkan suhu dalam Celcius: "))

        reamur_c = (4/5) * celcius
        fahrenheit_c = (9/5) * celcius + 32
        kelvin_c = celcius + 273.15

        print(f"Suhu dalam Celcius: {celcius}")
        if perubahan == "reamur":
            print(f"Hasil konversi: {reamur_c} °Re")
        elif perubahan == "fahrenheit":
            print(f"Hasil konversi: {fahrenheit_c} °F")
        elif perubahan == "kelvin":
            print(f"Hasil konversi: {kelvin_c} K")
        else:
            print("Pilihan konversi tidak tersedia!")

    elif pilihan == "reamur":
        reamur = float(input("Masukkan suhu dalam Reamur: "))
        celcius_r = (5/4) * reamur
        fahrenheit_r = (9/4) * reamur + 32
        kelvin_r = (5/4) * reamur + 273.15

        print(f"Suhu dalam Celcius: {celcius_r} °C")
        print(f"Suhu dalam Fahrenheit: {fahrenheit_r} °F")
        print(f"Suhu dalam Kelvin: {kelvin_r} K")

    elif pilihan == "fahrenheit":
        fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
        celcius_f = 5/9 * (fahrenheit - 32)
        reamur_f = 4/9 * (fahrenheit - 32)
        kelvin_f = celcius_f + 273.15

        print(f"Suhu dalam Celcius: {celcius_f} °C")
        print(f"Suhu dalam Reamur: {reamur_f} °Re")
        print(f"Suhu dalam Kelvin: {kelvin_f} K")

    elif pilihan == "kelvin":
        kelvin = float(input("Masukkan suhu dalam Kelvin: "))
        celcius_k = kelvin - 273.15
        reamur_k = 4/5 * (kelvin - 273.15)
        fahrenheit_k = (kelvin - 273.15) * 9/5 + 32

        print(f"Suhu dalam Celcius: {celcius_k} °C")
        print(f"Suhu dalam Reamur: {reamur_k} °Re")
        print(f"Suhu dalam Fahrenheit: {fahrenheit_k} °F")

    else:
        print("Pilihan tidak tersedia, silakan coba lagi!")

    perulangan = str(input("Apakah kamu ingin mengulang? (y/n) \n")).lower()
    if perulangan != "y":
        print("Terima kasih telah menggunakan program ini!")
        break