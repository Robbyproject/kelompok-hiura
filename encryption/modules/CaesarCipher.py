from modules.Cipher import Cipher
from multipledispatch import dispatch

class CaesarCipher(Cipher):

    def __encrypt(self, shift):
        result = ""

        for i in range(len(self.plain_text)):
            char = self.plain_text[i]

            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65) 
            elif char.islower():
                result += chr((ord(char) + shift - 97) % 26 + 97) 
            else:
                result += char

        return result

    @dispatch()
    def encrypt(self):
        return self.__encrypt(3)

    @dispatch(int)
    def encrypt(self, shift):
        return self.__encrypt(shift)
    