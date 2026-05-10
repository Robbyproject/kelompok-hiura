from .ItemPerpustakaan import ItemPerpustakaan
from .Penulis import Penulis

class Buku(ItemPerpustakaan):

    def __init__(self, id_item, judul, penulis: Penulis):
        super().__init__(id_item, judul)
        self.penulis = penulis

    def deskripsi(self):
        return f"[{self.get_id :<7}] Buku: {self.get_judul :<30} | Penulis: {self.penulis.nama} ({self.penulis.kewarganegaraan})"