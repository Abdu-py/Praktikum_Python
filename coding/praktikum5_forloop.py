
# Program 1: Penjumlahan Dua Matriks
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

hasil = [[0, 0], [0, 0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        hasil[i][j] = A[i][j] + B[i][j]

print("Hasil Penjumlahan Matriks:")
for r in hasil:
    print(r)



# Program 2: Total Pembelian N Barang
total = 0
N = int(input("Masukkan jumlah barang: "))

for i in range(N):
    harga = float(input(f"Masukkan harga barang ke-{i+1}: "))
    jumlah = int(input(f"Masukkan jumlah barang ke-{i+1}: "))
    total += harga * jumlah

print("Total pembelian =", total)



# Program 3: Hitung Bilangan Ganjil dan Genap
N = int(input("Masukkan banyak bilangan: "))
ganjil = genap = 0

for i in range(N):
    bil = int(input(f"Masukkan bilangan ke-{i+1}: "))
    if bil % 2 == 0:
        genap += 1
    else:
        ganjil += 1

print("Jumlah bilangan genap:", genap)
print("Jumlah bilangan ganjil:", ganjil)



# Program 4: Bilangan Kelipatan 3
a = int(input("Masukkan batas awal: "))
b = int(input("Masukkan batas akhir: "))

print("Bilangan kelipatan 3 diantara", a, "dan", b, ":")
for i in range(a, b + 1):
    if i % 3 == 0:
        print(i, end=" ")



# Program 5: Pola Angka Bertingkat
n = int(input("Masukkan bilangan: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()



# Program 6: Menghitung Nilai Akhir Mahasiswa
n = int(input("Masukkan jumlah mahasiswa: "))

for i in range(1, n + 1):
    nama = input(f"Nama mahasiswa ke-{i}: ")
    tugas = float(input("Nilai Tugas: "))
    kuis = float(input("Nilai Kuis: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))

    nilai_akhir = (tugas * 0.2) + (kuis * 0.2) + (uts * 0.3) + (uas * 0.3)
    print(f"{i}. {nama} - Nilai Akhir: {nilai_akhir:.2f}")
