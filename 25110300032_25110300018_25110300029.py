from modules.KomponenHarga import KomponenHarga
from modules.PajakPPN import PajakPPN
from modules.TransaksiPOS import TransaksiPOS

def inputPesanan(transaksiPOS: TransaksiPOS):
    while True:
        print("\n--- Input Pesanan ---")
        nama_makanan = input("Nama Makanan (atau ketik 'selesai'): ")
        if nama_makanan == "selesai":
            return
        harga_satuan = int(input(f"Harga Satuan {nama_makanan}: "))
        jumlah = int(input(f"Jumlah {nama_makanan}: "))
        transaksiPOS.tambah_item(nama_makanan, harga_satuan, jumlah)

def bayarTagihan(transaksiPOS: TransaksiPOS):
    while True:
        uang_bayar = int(input("Masukkan Uang Bayar: Rp"))
        if transaksiPOS.proses_pembayaran(uang_bayar):
            print(f"BERHASIL: Kembalian Anda adalah Rp{uang_bayar - transaksiPOS.total_akhir :,}\n")
            return
        
        print(f"GAGAL: Uang Kurang! (Kurang Rp{transaksiPOS.total_akhir - uang_bayar :,})\n")


def main():
    print("=" * 40)
    print("       SISTEM KASIR RESTORAN OOP")
    print("=" * 40)
    nama_pelanggan = input("Nama Pelanggan : ")
    nomor_meja     = input("Nomor Meja     : ")
    transaksi_pos = TransaksiPOS(nama_pelanggan, nomor_meja)

    inputPesanan(transaksi_pos)
    transaksi_pos.cetak_struk()
    bayarTagihan(transaksi_pos)

main()