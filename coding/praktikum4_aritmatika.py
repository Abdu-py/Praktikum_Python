# Penjumlahan
print(13 + 2)
mangga = 7
pisang = 9
buah = mangga + pisang
print(buah)

# Pengurangan
hutang = 10000
bayar = 5000
sisaHutang = hutang - bayar
print('Sisa hutang Anda adalah ', sisaHutang)

# Perkalian
panjang = 15
lebar = 8
luas = panjang * lebar
print(luas)

# Pembagian
kue = 16
anak = 4
kuePerAnak = kue / anak
print('Setiap anak akan mendapatkan bagian kue sebanyak ', kuePerAnak)

# Sisa Bagi / Modulus
bilangan1 = 14
bilangan2 = 5
hasil = bilangan1 % bilangan2
print('Sisa bagi dari bilangan ', bilangan1, ' dan ', bilangan2, ' adalah ', hasil)

# Pangkat
bilangan3 = 8
bilangan4 = 2
hasilPangkat = bilangan3 ** bilangan4
print(hasilPangkat)

# Pembagian Bulat
print(10 // 3)
# 10 dibagi 3 = 3.3333, dibulatkan menghasilkan 3

BilanganPertama = 15
BilanganKedua = 8
BilanganKetiga = 100

RumusPengjumlahan = BilanganPertama + BilanganKedua + BilanganKetiga
RumusPengurangan = BilanganPertama - BilanganKedua - BilanganKetiga
RumusPerkalian = BilanganPertama * BilanganKedua * BilanganKetiga

print('Pengjumlahan = ', BilanganPertama, '+', BilanganKedua, '+', BilanganKetiga, '=', RumusPengjumlahan)
print('Pengurangan = ', BilanganPertama, '-', BilanganKedua, '-', BilanganKetiga, '=', RumusPengurangan)
print('Perkalian   = ', BilanganPertama, 'x', BilanganKedua, 'x', BilanganKetiga, '=', RumusPerkalian)

# 1. Luas Persegi
panjang_sisi = 20
luas_persegi = panjang_sisi * panjang_sisi

# 2. Luas Persegi Panjang
panjang_pp = 50
lebar_pp = 25.5
luas_pp = panjang_pp * lebar_pp

# 3. Luas Segitiga
alas_segitiga = 40
tinggi_segitiga = 60
luas_segitiga = 0.5 * alas_segitiga * tinggi_segitiga

# 4. Luas Lingkaran
phi = 3.14
jari_jari = 14
luas_lingkaran = phi * jari_jari * jari_jari

# 5. Luas Jajaran Genjang
alas_jg = 30
tinggi_jg = 25
luas_jg = alas_jg * tinggi_jg

# 6. Luas Trapesium
alas1_trapesium = 40
alas2_trapesium = 25
tinggi_trapesium = 20
luas_trapesium = 0.5 * (alas1_trapesium + alas2_trapesium) * tinggi_trapesium

print('Luas Persegi =', luas_persegi)
print('Luas Persegi Panjang =', luas_pp)
print('Luas Segitiga =', luas_segitiga)
print('Luas Lingkaran =', luas_lingkaran)
print('Luas Jajaran Genjang =', luas_jg)
print('Luas Trapesium =', luas_trapesium)

a = 10  # 1010 dalam biner
b = 4   # 0100 dalam biner

print('a & b =', a & b)
print('a | b =', a | b)
print('a ^ b =', a ^ b)
print('~a =', ~a)
print('a << 2 =', a << 2)
print('a >> 2 =', a >> 2)