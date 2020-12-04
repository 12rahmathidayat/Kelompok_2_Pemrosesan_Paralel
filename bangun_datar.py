import math

def persegi():
    sisi = int(input("Sisi:"))
    luas = sisi * sisi
    keliling = sisi * 4
    lk(luas, keliling)

def persegi_panjang():
    panjang = int(input("Panjang:"))
    print()
    lebar = int(input("Lebar:"))
    luas = panjang * lebar
    keliling = (2 * panjang) + (2 * lebar)
    lk(luas, keliling)

def lingkaran():
    jari_jari = int(input("Jari-jari:"))
    luas = 3.14 * jari_jari * jari_jari
    keliling = 2 * 3.14 * jari_jari
    lk(luas, keliling)

def segitiga():
    alas = int(input("Alas:"))
    print()
    tinggi = int(input("Tinggi:"))

    luas = alas * tinggi / 2

    print("\n\n==========+ Hasil +==========")
    print("\nLuas:", luas)
    # ========= Segitiga Sama Sisi =========
    print("Keliling segitiga sama sisi: ", alas * 3)

    # ========= Segitiga Sama Kaki
    setengahAlas = alas * 0.5
    kaki = math.sqrt((setengahAlas ** 2) + (tinggi ** 2))
    print("Keliling segitiga sama kaki:", 2 * kaki + alas)

    # ========= Segitiga Siku Siku =========
    miring = math.sqrt((alas ** 2) + (tinggi ** 2))
    print("Keliling segitiga siku - siku:", alas + tinggi + miring)

def lk(luas, keliling):
    print("\n\n==========+ Hasil +==========")
    print("\nLuas: {}".format(luas))
    print("Keliling: {}".format(keliling))

print("===========+ Program hitung luas dan jari - jari bangun datar +===========\n")

print("1) Persegi")
print("2) Persegi Panjang")
print("3) Segitiga")
print("4) Lingkaran\n")

pilihan = int(input("Silahkan masukkan pilihan: "))
if pilihan == 1:
    persegi()
elif pilihan == 2:
    persegi_panjang()
elif pilihan == 3:
    segitiga()
elif pilihan == 4:
    lingkaran()
elif pilihan == 5:
    trapesium
else:
    print("Maaf, masukan anda salah, silahkan masukkan pilihan yang benar!\n")