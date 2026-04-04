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
        invoice = f"=== INVOICE POS ===\n"
        invoice += f"Pelanggan : {self.pelanggan}\n"
        invoice += f"Meja      : {self.meja}\n"
        invoice += "-------------------\n"
        invoice += "Daftar Pesanan:\n"
        for pesanan in self.daftar_pesanan:
            invoice += f"- {pesanan['item']:<15} : Rp {pesanan['harga']}\n"
        invoice += "-------------------\n"
        invoice += f"Total Tagihan     : Rp {self.total_tagihan}\n"
        invoice += "==================="
        return invoice
    def proses_pembayaran(self, jumlah_bayar):
        if jumlah_bayar >= self.total_tagihan:
            return True
        else:
            return False