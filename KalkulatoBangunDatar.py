def infinite():
    while True:
        yield None

class KalkulatorBangunDatar:
    def luasPersegi():
        sisi = int(input("Masukkan Sisi : "))
        print("Luas Persegi = ",sisi*sisi)
        print("")

    def kelilingPersegi():
        sisi = int(input("Masukkan Sisi : "))
        print("Keliling Persegi = ",sisi*4)
        print("")

    def luasPersegiPanjang():
        panjang = int(input("Masukkan Panjang : "))
        lebar = int(input("Masukkan Lebar : "))
        print("Luas Persegi Panjang = ",panjang*lebar)
        print("")

    def kelilingPersegiPanjang():
        panjang = int(input("Masukkan Panjang : "))
        lebar = int(input("Masukkan Lebar : "))
        print("Keliling Persegi Panjang = ",(panjang+lebar)*2)

    def luasSegitiga():
        alas = int(input("Masukkan Alas : "))
        tinggi = int(input("Masukkan Tinggi : "))
        print("Keliling Persegi Panjang = ",(1/2)*alas*tinggi)
        print("")

    def kelilingSegitiga(a,b,c):
        a = int(input("Masukkan Panjang : "))
        b = int(input("Masukkan Lebar : "))
        c = int(input("Masukkan Panjang : "))
        print(a+b+c)
        print("")

i = 0
for j in infinite():
    print("\nKalkulator Bangun Datar")
    print("=====================================")
    print("1. Luas Persegi")
    print("2. Keliling Persegi")
    print("3. Luas Persegi Panjang")
    print("4. Keliling Persegi Panjang")
    print("5. Luas Segitiga")
    print("6. Keliling Segitiga")
    print("=====================================\n")
    pilih = int(input("Masukkan Pilihan : "))
    if pilih == 1:
        KalkulatorBangunDatar.luasPersegi()
    elif pilih == 2:
        KalkulatorBangunDatar.kelilingPersegi()
    elif pilih == 3:
        KalkulatorBangunDatar.luasPersegiPanjang()
    elif pilih == 4:
        KalkulatorBangunDatar.kelilingPersegiPanjang()
    elif pilih == 5:
        KalkulatorBangunDatar.luasSegitiga()
    elif pilih == 6:
        KalkulatorBangunDatar.kelilingSegitiga()
    else:
        print("Pilihan Tidak Ada")
    lanjut = input("\nLanjutkan (Y/T) : ")
    if lanjut == "T" or lanjut == "t":
        break
    else:
        i = 0