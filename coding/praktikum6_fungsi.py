def kalimat():
    """Menampilkan kalimat Hallo, Selamat Belajar Python"""
    print("Hallo, Selamat Belajar Python")

kalimat()

def jumlah():
    """Menjumlahkan dua bilangan"""
    a = 1
    b = 2
    c = a + b
    return c

tampil = jumlah()
print("Hasil Penjumlahan =", tampil)

def identitas(nama, kota):
    """Menampilkan identitas"""
    print("Nama saya:", nama)
    print("Saya lahir di kota:", kota)

n = input("Masukkan nama Anda: ")
k = input("Masukkan kota kelahiran: ")
identitas(n, k)

def perkalian(bil1, bil2):
    """Mengalikan dua buah bilangan"""
    hasil = bil1 * bil2
    return hasil

a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))
print("Hasil perkalian =", perkalian(a, b))

def perkalian(bil1, bil2):
    """Mengalikan dua bilangan dengan keyword argument"""
    return bil1 * bil2

print("Hasil 1 =", perkalian(5, 7))
print("Hasil 2 =", perkalian(bil2=7, bil1=5))

def lokal():
    """Contoh variabel lokal"""
    teks = "Ini variabel lokal"
    print(teks)

lokal()

teks = "Ini variabel global"

def tampil():
    """Menampilkan variabel lokal dan global"""
    teks = "Ini variabel lokal"
    print(teks)

tampil()
print(teks)