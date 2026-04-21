from modules.Cipher import Cipher

class ReverseCipher(Cipher):

    def encrypt(self):
        return self.plain_text[::-1]