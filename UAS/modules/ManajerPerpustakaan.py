from .Buku import Buku

class ManajerPerpustakaan:

    def __init__(self):
        self.koleksi = []
        self.terurut = False

    def validasi_id_unik(self, id_baru): # return bool
        pass

    def tambah_buku_baru(self): # void
        pass

    def tampilkan_koleksi(self): # void
        pass

    def urutkan_koleksi(self): # return void, bubble sort
        pass

    def cari_buku(self, id_target): # return object dari class Buku / None, binary search
        pass