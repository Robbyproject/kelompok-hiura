from .Buku import Buku

class ManajerPerpustakaan:

    def __init__(self):
        self.koleksi = []
        self.terurut = False

    def validasi_id_unik(self, id_baru): # return bool,,, Robby
        for buku in self.koleksi:
            if buku.id == id_baru:
                return False
        return True

    def tambah_buku_baru(self): # void
        pass

    def tampilkan_koleksi(self): # void
        pass

    def urutkan_koleksi(self): # return void, bubble sort,,,, Robby
        if self.terurut:
            print("Koleksi sudah terurut.")
            return
        n = len(self.koleksi)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.koleksi[j].id > self.koleksi[j+1].id:
                    self.koleksi[j], self.koleksi[j+1] = self.koleksi[j+1], self.koleksi[j]
        self.terurut = True
        print("Koleksi berhasil diurutkan berdasarkan ID.")

    def cari_buku(self, id_target): # return object dari class Buku / None, binary search
        return 