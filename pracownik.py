class pracownik:
    def __init__(self, imie, nawisko, kontakt, stanowisko):
        self.imie = imie
        self.nawisko = nawisko
        self.kontakt = kontakt
        self.stanowisko = stanowisko

    def opis(self):
        return f"Imie: {self.imie} Nazwisko: {self.nawisko} Kontakt: {self.kontakt} Stanowisko: {self.stanowisko}"

