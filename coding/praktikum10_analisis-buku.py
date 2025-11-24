import os
from pathlib import Path

# Mendefinisikan nama file sebagai konstanta (konvensi UPPERCASE)
FILE_NAME = "data_buku.txt"

class BookManager:
    """
    Mengelola operasi CRUD (Create, Read, Update, Delete) 
    untuk data buku yang disimpan dalam file teks.
    """
    def __init__(self, filename=FILE_NAME):
        """Inisialisasi manajer data dan memastikan file path ada."""
        self.filepath = Path(filename)
        # Membuat file jika belum ada
        self.filepath.touch(exist_ok=True) 

    def _read_data(self):
        """Membaca semua judul buku dari file."""
        try:
            # Menggunakan encoding 'utf-8' untuk kompatibilitas yang lebih baik
            with self.filepath.open('r', encoding='utf-8') as f:
                # Menggunakan list comprehension untuk pembacaan yang ringkas dan membersihkan newline
                data = [line.strip() for line in f if line.strip()]
            return data
        except IOError as e:
            print(f"ERROR: Gagal membaca file {self.filepath}: {e}")
            return []

    def _write_data(self, data):
        """Menulis (menimpa) semua data buku kembali ke file."""
        try:
            with self.filepath.open('w', encoding='utf-8') as f:
                for judul in data:
                    f.write(judul + '\n')
            return True
        except IOError as e:
            print(f"ERROR: Gagal menulis ke file {self.filepath}: {e}")
            return False
            
    # --- Metode Publik untuk Operasi CRUD ---

    def insert_data(self, judul):
        """Menambahkan judul buku baru ke list dan menulis ke file."""
        data = self._read_data()
        data.append(judul)
        if self._write_data(data):
            print(f"Buku '{judul}' berhasil ditambahkan.")

    def show_all_data(self):
        """Menampilkan semua data buku yang tersimpan, diurutkan secara alfabetis."""
        data_buku = self._read_data()
        
        print("\n" + "="*30)
        print("DATA BUKU TERSIMPAN")
        print("="*30)
        
        if not data_buku:
            print("Belum ada data buku yang masuk.")
        else:
            data_buku.sort() 
            for i, judul in enumerate(data_buku, 1):
                print(f"{i}. {judul}")
        
        print("="*30)

    def search_data(self, search_term):
        """Mencari buku berdasarkan kata kunci."""
        data_buku = self._read_data()
        search_term = search_term.lower().strip()
        # Menggunakan list comprehension untuk filtering yang bersih
        found_books = [judul for judul in data_buku if search_term in judul.lower()]
        
        print("\n" + "="*30)
        print("HASIL PENCARIAN")
        print("="*30)
        
        if not found_books:
            print(f"Buku dengan kata kunci '{search_term}' tidak ditemukan.")
        else:
            for judul in found_books:
                print(f"-> {judul}")

    def update_data(self, judul_lama, judul_baru):
        """Mengubah judul buku lama menjadi judul baru."""
        data_buku = self._read_data()
        
        try:
            # Mencari indeks buku yang akan diubah
            index_to_edit = data_buku.index(judul_lama)
            data_buku[index_to_edit] = judul_baru
            
            if self._write_data(data_buku):
                print(f"Buku '{judul_lama}' berhasil di-update menjadi '{judul_baru}'.")
            return True
        except ValueError:
            print(f"Buku dengan judul '{judul_lama}' tidak ditemukan.")
            return False

    def delete_data(self, judul_hapus):
        """Menghapus satu data buku berdasarkan judul."""
        data_buku = self._read_data()
        
        try:
            data_buku.remove(judul_hapus)
            if self._write_data(data_buku):
                print(f"Buku '{judul_hapus}' berhasil dihapus.")
            return True
        except ValueError:
            print(f"Buku dengan judul '{judul_hapus}' tidak ditemukan.")
            return False

    def delete_all(self):
        """Menghapus semua data buku (mengosongkan file)."""
        if self._write_data([]):
            print("Semua data buku berhasil dihapus.")
            return True
        return False

# --- Kelas Aplikasi (Antarmuka Pengguna) ---

class BookApp:
    """
    Kelas yang menangani interaksi pengguna (Menu) dan mengelola BookManager.
    """
    def __init__(self):
        self.manager = BookManager()
        # Menggunakan dictionary untuk memetakan input menu ke handler fungsi
        self.menu_options = {
            '1': self.handle_insert,
            '2': self.handle_show,
            '3': self.handle_search,
            '4': self.handle_update,
            '5': self.handle_delete,
            '6': self.handle_delete_all,
            '7': self.handle_exit
        }

    def show_menu(self):
        """Menampilkan antarmuka menu."""
        print("\n" + "="*30)
        print("📚 PROGRAM DATA BUKU SEDERHANA")
        print("="*30)
        print("1. Masukkan Data Buku")
        print("2. Tampilkan Data Buku")
        print("3. Cari Buku")
        print("4. Edit Data Buku")
        print("5. Hapus Data Buku (Per Item)")
        print("6. Hapus Semua Data Buku")
        print("7. Keluar")
        print("="*30)
        return input("Pilih Menu (1-7): ")

    # --- Menu Handlers ---
    # Fungsi-fungsi ini menangani input pengguna sebelum memanggil logika BookManager

    def handle_insert(self):
        while True:
            judul = input("Masukkan Judul Buku: ").strip()
            if not judul:
                print("Judul buku tidak boleh kosong.")
                continue
            
            self.manager.insert_data(judul)
                
            isi_lagi = input("Mau isi lagi? (y/t): ").lower()
            if isi_lagi != 'y':
                break
        self.wait_for_enter()

    def handle_show(self):
        self.manager.show_all_data()
        self.wait_for_enter()
        
    def handle_search(self):
        search_term = input("Masukkan judul buku yang ingin dicari: ").strip()
        if search_term:
            self.manager.search_data(search_term)
        self.wait_for_enter()

    def handle_update(self):
        judul_lama = input("Masukkan judul buku yang ingin di-update: ").strip()
        if not judul_lama:
            print("Input tidak valid.")
            self.wait_for_enter()
            return
            
        judul_baru = input(f"Masukkan judul buku yang baru untuk '{judul_lama}': ").strip()
        if not judul_baru:
            print("Judul buku baru tidak boleh kosong. Pembatalan edit.")
            self.wait_for_enter()
            return

        self.manager.update_data(judul_lama, judul_baru)
        self.wait_for_enter()
        
    def handle_delete(self):
        judul_hapus = input("Masukkan judul buku yang ingin dihapus: ").strip()
        if judul_hapus:
            self.manager.delete_data(judul_hapus)
        self.wait_for_enter()

    def handle_delete_all(self):
        konfirmasi = input("❗ PERINGATAN: Apakah Anda yakin akan menghapus SEMUA data buku? (y/t): ").lower()
        if konfirmasi == 'y':
            self.manager.delete_all()
        else:
            print("Penghapusan dibatalkan.")
        self.wait_for_enter()
        
    def handle_exit(self):
        print("Keluar dari program. Terima kasih!")
        return True 

    def wait_for_enter(self):
        """Fungsi sederhana untuk meminta input 'Enter'."""
        input("\nTekan ENTER untuk kembali ke menu...")
        
    def run(self):
        """Loop utama aplikasi."""
        while True:
            pilihan = self.show_menu()
            
            handler = self.menu_options.get(pilihan)
            if handler:
                if handler() is True:
                    break
            else:
                print("❌ Masukkan pilihan sesuai nomor menu yang tersedia (1-7).")
                self.wait_for_enter()

# --- Blok Eksekusi Utama ---

if __name__ == "__main__":
    app = BookApp()
    app.run()