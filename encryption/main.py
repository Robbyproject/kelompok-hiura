from modules.CaesarCipher import CaesarCipher
from modules.ReverseCipher import ReverseCipher

while True:
    reverse_cipher = ReverseCipher()
    caesar_cipher = CaesarCipher()

    text = input("Masukkan Kalimat: ")
    shift = input("(caesar) Ingin geser berapa (Enter if empty): ")

    reverse_cipher.plain_text = text
    caesar_cipher.plain_text = text

    print(f"{text} dibalik: {reverse_cipher.encrypt()}")
    if shift == "":
        print(f"{text} di enkripsi: {caesar_cipher.encrypt()}")
    else:
        try:
            shift = int(shift)
        except:
            print("Input geser harus berupa angka. Menggunakan nilai default (3)")
            shift = 3
        print(f"{text} di enkripsi: {caesar_cipher.encrypt(shift)}")


    print("---------------------")
    lanjut = input("Input lagi (y/n)? ")
    if lanjut == "n":
        break