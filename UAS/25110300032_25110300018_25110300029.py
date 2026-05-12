# INI MAIN BLM DI IMPLEMENTASI :)
from modules.ManajerPerpustakaan import ManajerPerpustakaan

perpus = ManajerPerpustakaan()

def main():
    while True:
        print("\n")
        print(f"=" * 50)
        print(f"     LIBSEARCH - DIGITAL ARCHIVE (ASSOCIATION)")
        print(f"=" * 50)
        print("1. Tambah Buku Baru")
        print("2. Tampilkan Semua Koleksi")
        print("3. Urutkan Koleksi (Bubble Sort)")
        print("4. Cari Buku (Binary Search)")
        print("5. Keluar")
        pilihan = input("\nPilih Menu (1-5): ")

        match pilihan:
            case "1":
                perpus.tambah_buku_baru()
            case "2":
                perpus.tampilkan_koleksi()
            case "3":
                perpus.urutkan_koleksi()
            case "4":
                try:
                    id_target = int(input("Masukkan ID Buku yang dicari: "))
                except:
                    print("\n[Peringatan] ID yang dimaksukan harus berupa angka!")
                    break
                
                buku = perpus.cari_buku(id_target)
                if buku:
                    print(f"\n[DITEMUKAN] Buku: {buku.get_judul :<30} | Penulis: {buku.penulis.nama}")
                    print(f"Detail Penulis: {buku.penulis.nama} ({buku.penulis.kewarganegaraan})")
                else:
                    print(f"[HASIL] ID {id_target} tidak ditemukan.")
            case "5":
                print("\n[SISTEM] Terimakasih sudah menggunakan program kami.")
                exit()
            case _:
                print("\n[SISTEM] Opsi tidak tersedia.")

main()