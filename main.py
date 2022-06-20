from pracownik import pracownik
from urlop import urlop
from zabieg import zabieg
from wlasciciel import wlasciciel
from towar import towar
from platnosc import platnosc
from klient import klient

temp = []
terminy = []
terminyGodziny = []
terminyUrlopyData = []
terminyUrlopyZak = []
# zabieg.status = "Termin zarezerwowany"
zabieg.status = "Termin wolny"

def rezerwacja():
    while True:
        print("Wybierz opcje:")
        print("1. Rezerwacja")
        print("2. Wypisanie z terminu")
        print("3. Wyjscie")
        opcja = input("Wybierz opcje: ")
        if opcja == "1":

            klient.email = input("Podaj email: ")
            zabieg.data = input("Podaj termin:")
            zabieg.godzina = int(input("Podaj godzine między od 10 do 19:"))

            if (zabieg.godzina < 10 or zabieg.godzina > 19):
                print("Godzina nie jest w zakresie")
                continue
            else:
                if (zabieg.data in terminy) and (zabieg.godzina in terminyGodziny):
                    print("Termin jest zarezerwowany, w tym czasie nie ma wolnego terminu")
                    return 0
                else:
                    zabieg.status = ("Termin zarezerwowany")
                    print("Termin zarezerwowany")
                    terminyGodziny.append(zabieg.godzina)
                    terminy.append(zabieg.data)
                    print(terminy+terminyGodziny)
                    continue

        if opcja == "2":
            zabieg.data = input("Podaj termin:")
            zabieg.godzina = int(input("Podaj godzine między od 10 do 19:"))

            terminy.remove(zabieg.data)
            terminyGodziny.remove(zabieg.godzina)
            print("Wypisales sie z terminu")
            print(terminy+terminyGodziny)
            continue
        if opcja == "3":
            return 0


def wybierz_decyzje():
    urlop.data_rozp = input("Podaj date rozpoczecia urlopu: ")
    urlop.data_zak = input("Podaj date zakonczenia urlopu: ")
    print("Wybierz decyzje:")
    print("1. Dostan urlop")
    print("2. Nie dostan urlopu")
    print("3. Wyjscie")
    decyzja = input("Wybierz decyzje: ")
    if decyzja == "1":
        wlasciciel.decyzja = "Dostan urlop"
        print("Własciciel zgodził się na urlop")
        terminyUrlopyData.append(urlop.data_rozp)
        terminyUrlopyZak.append(urlop.data_zak)
    if decyzja == "2":
        print("Własciciel nie zgodził się na urlop")
        wlasciciel.decyzja = "Nie dostan urlopu"
    if decyzja == "3":
        return 0

zamowione = []

def zeszyt_potrzeb():
    while True:
        print("Zeszyt")
        print("1. Pasta do zębów")
        print("2. Szczoteczki firmy Colgate")
        print("3. Znieczulenie w żelu (kartonik 125ml)")
        print("4. Znieczulenie w płynie (butelka 250ml)")
        print("5. Usun ostatnie zamowienie")
        print("6. Powrót")
        zeszyt = input()

        if zeszyt == "1":
            ilosc = int(input("Ilość: "))
            zamowione.append("Pasta do zębów " + str(ilosc))
        elif zeszyt == "2":
            ilosc = int(input("Ilość: "))
            zamowione.append("Szczoteczki firmy Colgate " + str(ilosc))
        elif zeszyt == "3":
            ilosc = int(input("Ilość: "))
            zamowione.append("Znieczulenie w żelu (kartonik 125ml) " + str(ilosc))
        elif zeszyt == "4":
            ilosc = int(input("Ilość: "))
            zamowione.append("Znieczulenie w płynie (butelka 250ml) " + str(ilosc))
        elif zeszyt == "5":
            zamowione.pop()
        else:
            return 0
        print("Zamówione: " + str(zamowione))



# rezerwacja()
# wybierz_decyzje()
# zeszyt_potrzeb()

klient.imie = ["Krystian", "Kamil"]
klient.nazwisko = ["Kowalski", "Nowak"]
klient.email = ["krystian124@fmail.com", "kamil124@fmail.com"]
klient.telefon = ["123456789", "987654321"]
klient.adres = ["ul. Krakowska", "ul. Nowa"]
klient.miasto = ["Krakow", "Warszawa"]


def wybierz_klienta():
    while True:
        print("Aktualnie zarejestrowani klienci:")
        for i in range(len(klient.imie)):
            print(str(i+1) + ". " + klient.imie[i] + " " + klient.nazwisko[i])
        print("a Dodaj klienta")
        print("b Powrót")
        klient_wybor = input("Wybierz klienta: ")
        print("Dane")
        if klient_wybor == "1":
            print("Imie: " + klient.imie[0])
            print("Nazwisko: " + klient.nazwisko[0])
            print("Email: " + klient.email[0])
            print("Telefon: " + klient.telefon[0])
            print("Adres: " + klient.adres[0])
            print("Miasto: " + klient.miasto[0])
        elif klient_wybor == "2":
            print("Imie: " + klient.imie[1])
            print("Nazwisko: " + klient.nazwisko[1])
            print("Email: " + klient.email[1])
            print("Telefon: " + klient.telefon[1])
            print("Adres: " + klient.adres[1])
            print("Miasto: " + klient.miasto[1])
        elif klient_wybor == "a":
            klient.imie.append(input("Imie: "))
            klient.nazwisko.append(input("Nazwisko: "))
            klient.email.append(input("Email: "))
            klient.telefon.append(input("Telefon: "))
            klient.adres.append(input("Adres: "))
            klient.miasto.append(input("Miasto: "))
        elif klient_wybor == "b":
            return 0
        else:
            print("Nie ma takiego klienta")
            return 0

pracownik.imie = ["Paweł", "Karolina", "Julia", "Piotr"]
pracownik.nazwisko = ["Madry", "Kowalska", "Nowak", "Zajaczkowski"]
pracownik.stanowsiko = ["Informatyk", "Dentysta", "Dentysta", "Dentysta"]
pracownik.kontakt = ["pracownik1@wp.pl", "pracownik2@wp.pl", "pracownik3@wp.pl", "pracownik4@wp.pl"]

def wybierzPracownika():
    while True:
        print("Aktualnie zarejestrowani pracownicy:")
        for i in range(len(pracownik.imie)):
            print(str(i+1) + ". " + pracownik.imie[i] + " " + pracownik.nazwisko[i])
        print("5. Powrót")
        wybor = input("Wybierz pracownika: ")

        if wybor == "1":
            print("Kontakt: " + pracownik.kontakt[0] + " Stanowisko: " + pracownik.stanowsiko[0])
        elif wybor == "2":
            print("Kontakt: " + pracownik.kontakt[1] + " Stanowisko: " + pracownik.stanowsiko[1])
        elif wybor == "3":
            print("Kontakt: " + pracownik.kontakt[2] + " Stanowisko: " + pracownik.stanowsiko[2])
        elif wybor == "4":
            print("Kontakt: " + pracownik.kontakt[3] + " Stanowisko: " + pracownik.stanowsiko[3])
        elif wybor == "5":
            return 0
        else:
            print("Nie ma takiego pracownika")
            return 0

# wybierzPracownika()


def menuGlowne():
    while True:
        print("Wybierz Menu:")
        print("1. Menu Pracownika")
        print("2. Menu Klienta")
        print("3. Wyjście")
        wybor = input("Wybierz menu: ")
        if wybor == "1":
            menuPracownika()
        elif wybor == "2":
            menuKlienta()
        else:
            return 0


opisZabiegu = []


def opis_zabiegu():
    while True:
        print("1.Opis")
        print("2.Powrót")
        if input("") == "1":
            print("Opisz zabieg:")
            opis = input("")
            opisZabiegu.append(opis)
        else:
            return 0
        print(opisZabiegu)

kwotaRachunku = []

def wystaw_rachunek():
    while True:
        print("1.Wystaw rachunek")
        print("2.Powrót")
        if input("") == "1":
            print("Kwota:")
            kwota = input("")
            kwotaRachunku.append(kwota)
        else:
            return 0
        print(kwotaRachunku)


def menuPracownika():
    while True:
        print("Menu Pracownika")
        print("1.Opis zabiegu")
        print("2.Wystaw Rachunek")
        print("3.Urlop")
        print("4.Zeszyt potrzeb")
        print("5.Kontakt z klientem")
        print("6.Wyloguj się")
        wybor = input("Opcja: ")
        if wybor == "1":
            opis_zabiegu()
        elif wybor == "2":
            wystaw_rachunek()
        elif wybor == "3":
            wybierz_decyzje()
        elif wybor == "4":
            zeszyt_potrzeb()
        elif wybor == "5":
            wybierz_klienta()
        elif wybor == "6":
            return 0

produkty = []

def kupProdukt():
    while True:
        print("1.Kup produkt")
        print("2.Zwroc produkt")
        print("3.Powrót")
        wyb = input("Wybierz opcję: ")
        if wyb == "1":
            print("1. Pasta do zębów")
            print("2. Szczoteczki firmy Colgate")
            print("3. Znieczulenie w żelu (kartonik 125ml)")
            print("4. Znieczulenie w płynie (butelka 250ml)")
            print("5. Powrót")
            wybor = input("Wybierz produkt: ")
            if wybor == "1":
                print("Produkt: Pasta do zębów")
                print("Cena: 10zł")
                ilosc = input("Ilość: ")
                produkty.append("Pasta do zębów" + " " + ilosc)
            elif wybor == "2":
                print("Produkt: Szczoteczki firmy Colgate")
                print("Cena: 15zł")
                ilosc = input("Ilość: ")
                produkty.append("Szczoteczki firmy Colgate" + " " + ilosc)
            elif wybor == "3":
                print("Produkt: Znieczulenie w żelu (kartonik 125ml)")
                print("Cena: 20zł")
                ilosc = input("Ilość: ")
                produkty.append("Znieczulenie w żelu (kartonik 125ml)" + " " + ilosc)
            elif wybor == "4":
                print("Produkt: Znieczulenie w płynie (butelka 250ml)")
                print("Cena: 25zł")
                ilosc = input("Ilość: ")
                produkty.append("Znieczulenie w płynie (butelka 250ml)" + " " + ilosc)
            elif wybor == "5":
                return 0
            else:
                print("Nie ma takiego produktu")
                return 0
            print(produkty)
        elif wyb == "2":
            print("Aktualne produkty:")
            print(produkty)
            produkty.pop()
            print("Produkty po usunięciu:")
            print(produkty)
        else:
            return 0


def menuKlienta():
    while True:
        print("Menu Klienta")
        print("1.Zapisz się na zabieg")
        print("2.Zrezygnuj z zabiegu")
        print("3.Kup produkt")
        print("4.Kontakt z pracownikiem")
        print("5.Zwroc Towar")
        print("6.Wyloguj się")
        wybor = input("Opcja: ")
        if wybor == "1" or wybor == "2":
            rezerwacja()
        elif wybor == "3" or wybor == "5":
            kupProdukt()
        elif wybor == "4":
            wybierzPracownika()
        else:
            return 0

# menuKlienta()
menuGlowne()