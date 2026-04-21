class Cipher:
    def __init__(self):
        self.__plain_text = ""

    @property
    def plain_text(self):
        return self.__plain_text
    
    @plain_text.setter
    def plain_text(self, text):
        if text != "":
            self.__plain_text = text
        else:
            raise ValueError("Text cannot be empty")
        
    
