class PajakPPN:
    def __init__(self, subtotal):
        super().__init__(subtotal)
        self.nilai_pajak = self.subtotal * 0.1
        self.total_akhir += self.nilai_pajak
    
