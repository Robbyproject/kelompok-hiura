from .Buku import Buku
from .Penulis import Penulis

class ManajerPerpustakaan:

    def __init__(self):
        self.koleksi = []
        self.terurut = False

    def validasi_id_unik(self, id_baru): # return bool,,, Robby
        for buku in self.koleksi:
            if buku.id_item == id_baru: # dibaca mas nama attribute nya id_item bukan id doang -haris
                return False
        return True

    def tambah_buku_baru(self): # void
        print("\n--- Form Penambahan Buku Baru ---")

        id_buku = int(input("Masukkan ID Buku (Angka): "))

        # validasi ID unik
        if not self.validasi_id_unik(id_buku):
            print("[GAGAL] ID Buku sudah digunakan!")
            return

        judul = input("Masukkan Judul Buku: ")
        nama_penulis = input("Masukkan Nama Penulis: ")
        negara_penulis = input("Masukkan Asal Negara Penulis: ")

        penulis_baru = Penulis(nama_penulis, negara_penulis)

        buku_baru = Buku(id_buku, judul, penulis_baru)

        self.koleksi.append(buku_baru)

        self.terurut = False

        print(f"[SUKSES] '{judul}' karya {nama_penulis} berhasil ditambahkan.")


    def tampilkan_koleksi(self): # void
        if len(self.koleksi) == 0:
            print("\nBelum ada koleksi buku.")
            return

        print("\nID        | Informasi Buku")
        print("-" * 70)

        for buku in self.koleksi:
            print(buku.deskripsi())

    def urutkan_koleksi(self): # return void, bubble sort,,,, Robby
        if self.terurut:
            print("[SISTEM] Koleksi sudah terurut.")
            return
        n = len(self.koleksi)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.koleksi[j].id_item > self.koleksi[j+1].id_item:
                    self.koleksi[j], self.koleksi[j+1] = self.koleksi[j+1], self.koleksi[j]
        self.terurut = True
        print("[SISTEM] Koleksi berhsil diurutkan.")

    def cari_buku(self, id_target): # return object dari class Buku / None, binary search
        if not self.terurut:
            print("\n[Peringatan] Mohon untuk mengurutkan data terlebih dahulu!")
            return None

        low = 0
        high = len(self.koleksi) - 1

        while low <= high:
            # Tentukan tengah
            mid = (low + high) // 2
            
            # cek targetnya ditengah ga
            if self.koleksi[mid].id_item == id_target:
                return self.koleksi[mid]
            # Target lebih gede, buang bagian kiri
            elif self.koleksi[mid].id_item < id_target:
                low = mid + 1
            # Target lebih gede, buang bagian kanan
            else:
                high = mid - 1
        
        return None