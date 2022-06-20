class zabieg:
    def __init__(self, rodzaj, opis, data, status, godzina):
        self.rodzaj = rodzaj
        self.opis = opis
        self.data = data
        self.status = status
        self.godzina = godzina

    def opisZabiegu(self):
        return f"Rodzaj: {self.rodzaj} Opis: {self.opis} Data: {self.data} Status: {self.status} Godzina: {self.godzina}"