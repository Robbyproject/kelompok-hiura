from modules.PajakPPN import PajakPPN

class TransaksiPOS(PajakPPN): #haris hama
    def __init__(self, nama_pelanggan, nomor_meja):
        super().__init__(0)
        self.nama_pelanggan = nama_pelanggan
        self.nomor_meja = nomor_meja
        self.daftar_pesanan = []

    def tambah_item(self, nama_makanan, harga_satuan, jumlah):
        pesanan_baru = {
            "nama_makanan": nama_makanan, 
            "harga_satuan": harga_satuan,
            "jumlah": jumlah
        }
        self.daftar_pesanan.append(pesanan_baru)
        self.subtotal += (jumlah * harga_satuan)
        return f"Item '{nama_makanan}' sejumlah {jumlah} telah ditambahkan."
    
    def cetak_struk(self):
        super().__init__(self.subtotal)
        print("\n" + "=" * 40)
        print(f"       STRUK PEMBAYARAN - MEJA {self.nomor_meja}")
        print("=" * 40)
        print(f"Pelanggan: {self.nama_pelanggan}")
        print("-" * 40)
        for pesanan in self.daftar_pesanan:
            subtotal_item = pesanan['jumlah'] * pesanan['harga_satuan']
            print(f"{pesanan['nama_makanan']:<20} x {pesanan['jumlah']:<2} Rp {subtotal_item:>10,}")
        print("-" * 40)
        print(f"{'Subtotal':<17} : Rp {self.subtotal:>15,}")
        print(f"{'PPN (10%)':<17} : Rp {self.nilai_pajak:>15,}")
        print(f"{'TOTAL AKHIR':<17} : Rp {self.total_akhir:>15,}")
        print("=" * 40 + "\n")
    
    def proses_pembayaran(self, jumlah_bayar):
        if jumlah_bayar >= self.total_akhir:
            return True
        else:
            return False