class TransaksiPOS:
    def __init__(self, pelanggan, meja):
        super().__init__(0)
        self.pelanggan = pelanggan
        self.meja = meja
        self.daftar_pesanan = []
    def tambah_item(self, nama_item, harga):
        pesanan_baru = {"item": nama_item, "harga": harga}
        self.daftar_pesanan.append(pesanan_baru)
        self.total_tagihan += harga
        return f"Item '{nama_item}' dengan harga {harga} telah ditambahkan ke pesanan."
    def cetak_struk(self):
        invoice = "\n" + "=" * 40 + "\n"
        invoice += f"       STRUK PEMBAYARAN - MEJA {self.meja}\n"
        invoice += "=" * 40 + "\n"
        invoice += f"Pelanggan: {self.pelanggan}\n"
        invoice += "-" * 40 + "\n"
        for pesanan in self.daftar_pesanan:
            subtotal_item = pesanan['jumlah'] * pesanan['harga_satuan']
            invoice += f"{pesanan['nama_makanan']:<20}x{pesanan['jumlah']:>2}  Rp{subtotal_item:>11,}\n"
        invoice += "-" * 40 + "\n"
        invoice += f"{'TOTAL TAGIHAN':<23}  Rp{self.total_tagihan:>11,}\n"
        invoice += "=" * 40
        return invoice
    def proses_pembayaran(self, jumlah_bayar):
        if jumlah_bayar >= self.total_tagihan:
            return True
        else:
            return False