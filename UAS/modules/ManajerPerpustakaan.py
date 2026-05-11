from .Buku import Buku
from .Penulis import Penulis

class ManajerPerpustakaan:

    def _init_(self):
        self.koleksi = []
        self.terurut = False

    def validasi_id_unik(self, id_baru): # return bool
        pass

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

    def urutkan_koleksi(self): # return void, bubble sort
        pass

    def cari_buku(self, id_target): # return object dari class Buku / None, binary search
        pass