from PajakPPN import PajakPPN

class TransaksiPOS(PajakPPN):#haris hama
    def __init__(self, pelanggan, meja):
        super().__init__(0)
        self.pelanggan = pelanggan
        self.meja = meja
        self.daftar_pesanan = []
    def tambah_item(self, nama_makanan, jumlah, harga_satuan):
        pesanan_baru = {
            "nama_makanan": nama_makanan, 
            "jumlah": jumlah,
            "harga_satuan": harga_satuan
        }
        self.daftar_pesanan.append(pesanan_baru)
        self.subtotal += (jumlah * harga_satuan)
        self.hitung_pajak()
        return f"Item '{nama_makanan}' sejumlah {jumlah} telah ditambahkan."
    def cetak_struk(self):
        lebar = 46 # Haris Hama
        invoice = "\n" + "=" * lebar + "\n"
        invoice += f"STRUK PEMBAYARAN - MEJAK {int(self.meja):02d}".center(lebar) + "\n"
        invoice += "=" * lebar + "\n"
        invoice += f"Pelanggan: {self.pelanggan}\n"
        invoice += "-" * lebar + "\n"
        for pesanan in self.daftar_pesanan:
            subtotal_item = pesanan['jumlah'] * pesanan['harga_satuan']
            invoice += f"{pesanan['nama_makanan']:<20} x {pesanan['jumlah']:<2} Rp {subtotal_item:>10,}\n"
        invoice += "-" * lebar + "\n"
        invoice += f"{'Subtotal':<19} : Rp {self.subtotal:>10,}\n"
        invoice += f"{'PPN (10%)':<19} : Rp {self.nilai_pajak:>10,}\n"
        invoice += f"{'TOTAL AKHIR':<19} : Rp {self.total_akhir:>10,}\n"
        invoice += "=" * lebar
        return invoice
    def proses_pembayaran(self, jumlah_bayar):
        if jumlah_bayar >= self.total_tagihan:
            return True
        else:
            return False