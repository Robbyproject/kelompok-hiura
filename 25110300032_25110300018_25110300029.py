pass # :)

def inputPesanan():
    list_pesanan = []
    while True:
        print("\n--- Input Pesanan ---")
        nama_makanan = input("Nama Makanan (atau ketik 'selesai'): ")
        if nama_makanan == "selesai":
            return list_pesanan
        harga_satuan = int(input(f"Harga Satuan {nama_makanan}: "))
        jumlah = int(input(f"Jumlah {nama_makanan}: "))

        list_pesanan.append({
            "nama_makanan": nama_makanan,
            "harga_satuan": harga_satuan,
            "jumlah"      : jumlah
        })

def printStrukPembayaran(nama_pelanggan, nomor_meja, list_pesanan):
    print("\n" + "=" * 40)
    print(f"       STRUK PEMBAYARAN - MEJA {nomor_meja}")
    print("=" * 40)
    print(f"Pelanggan: {nama_pelanggan}")
    print("-" * 40)
    for pesanan in list_pesanan:
        print(f"{pesanan['nama_makanan']:<20}x{pesanan['jumlah']:>2}  Rp{pesanan['jumlah'] * pesanan['harga_satuan'] :>11,}")
    print("-" * 40)
    # logic from classes
    print("=" * 40)

def main():
    print("=" * 40)
    print("       SISTEM KASIR RESTORAN OOP")
    print("=" * 40)
    nama_pelanggan = input("Nama Pelanggan : ")
    nomor_meja     = input("Nomor Meja     : ")

    pesanan = inputPesanan()
    printStrukPembayaran(nama_pelanggan, nomor_meja, pesanan)




main()