# PROGRAM KASIR SEDERHANA DENGAN PERULANGAN

# 1. Daftar Harga Barang
daftar_harga = {
    "Beras": 30000,
    "Minyak": 15000,
    "Gula": 10000,
    "Telur": 25000,
    "Kopi": 12000
}

# 2. Inisialisasi Keranjang Belanja dan Total
keranjang = []
total_harga = 0
nomor_item = 1

print("="*40)
print("    PROGRAM KASIR SEDERHANA PYTHON    ")
print("="*40)

# Tampilkan Daftar Menu
print("Daftar Barang Tersedia:")
for barang, harga in daftar_harga.items():
    # Menggunakan f-string dan format ribuan
    print(f"- {barang:<10}: Rp {harga:,.0f}")
print("-"*40)
print("Ketik 'selesai' untuk menyelesaikan belanja.")
print("-"*40)

# 3. Perulangan untuk Input Belanja (While Loop)
while True:
    try:
        # Input nama barang
        input_barang = input(f"[{nomor_item}] Masukkan nama barang: ").strip().capitalize()

        # Kondisi keluar dari perulangan
        if input_barang.lower() == 'selesai':
            break

        # Cek apakah barang ada di daftar harga
        if input_barang in daftar_harga:
            # Perulangan untuk memastikan input jumlah valid
            while True:
                try:
                    input_jumlah = int(input(f"Masukkan jumlah {input_barang}: "))
                    if input_jumlah > 0:
                        break
                    else:
                        print("Jumlah harus lebih dari nol.")
                except ValueError:
                    print("Input jumlah tidak valid. Harap masukkan angka.")

            # Hitung Subtotal
            harga_satuan = daftar_harga[input_barang]
            subtotal = harga_satuan * input_jumlah

            # Tambahkan ke keranjang dan total
            keranjang.append((input_barang, input_jumlah, harga_satuan, subtotal))
            total_harga += subtotal
            nomor_item += 1
            print(f"-> {input_barang} x {input_jumlah} (Rp {subtotal:,.0f}) berhasil ditambahkan.")

        else:
            print(f"Barang '{input_barang}' tidak ditemukan dalam daftar. Coba lagi.")

    except Exception as e:
        print(f"Terjadi kesalahan input: {e}")

# 4. Proses Struk/Pembayaran
print("\n"+"="*40)
print("            STRUK BELANJA           ")
print("="*40)

if not keranjang:
    print("Keranjang belanja kosong.")
else:
    for i, (barang, jumlah, harga_satuan, subtotal) in enumerate(keranjang, 1):
        print(f"{i}. {barang:<10} ({jumlah} x Rp {harga_satuan:,.0f}) = Rp {subtotal:,.0f}")

    print("-"*40)
    print(f"TOTAL HARGA BELANJA: Rp {total_harga:,.0f}")
    print("-"*40)

    # Input Pembayaran
    while True:
        try:
            input_bayar = int(input("Masukkan jumlah pembayaran (Rp): "))
            if input_bayar >= total_harga:
                kembalian = input_bayar - total_harga
                print(f"Pembayaran diterima: Rp {input_bayar:,.0f}")
                print(f"Kembalian: Rp {kembalian:,.0f}")
                break
            else:
                print("Jumlah pembayaran kurang. Harap bayar sesuai atau lebih dari total harga.")
        except ValueError:
            print("Input pembayaran tidak valid. Harap masukkan angka.")

print("\nTerima Kasih Telah Berbelanja!")
