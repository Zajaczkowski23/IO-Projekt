class urlop:
    def __init__(self, data_rozp, data_zak, pracownik, stan):
        self.data_rozp = data_rozp
        self.data_zak = data_zak
        self.pracownik = pracownik
        self.stan = stan

    def terminUrlopu(self):
        return f"Data rozpoczecia: {self.data_rozp} Data zakonczenia: {self.data_zak}"

    def pracownik(self):
        return f"Pracownik: {self.pracownik} Stan: {self.stan}"