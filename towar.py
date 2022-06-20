class towar:
    def __init__(self, nazwa, rodzaj, cena, ilosc):
        self.nazwa = nazwa
        self.rodzaj = rodzaj
        self.cena = cena
        self.ilosc = ilosc

    def opisTowaru(self):
        return f"Nazwa: {self.nazwa} Rodzaj: {self.rodzaj} Cena za szutke: {self.cena} Ilosc: {self.ilosc}"