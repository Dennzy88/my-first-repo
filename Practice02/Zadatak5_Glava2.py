class Kupac:
    def __init__(self, ime, email):
        self.ime = ime
        self.email = email
        self.lista_proizvoda = []

    def dodaj_proizvod(self, proizvod):
        self.lista_proizvoda.append(proizvod)
        
    def prikazi_kupovine(self):
        if not self.lista_proizvoda:
            print(f"{self.ime} nije kupio nijedan proizvod.")
        else:
            print(f"{self.ime} je kupio sledeće proizvode:")
            for proizvod in self.lista_proizvoda:
                print(f"- {proizvod}")

# Kreiramo kupce
kupac1 = Kupac("Marko", "marko@example.com")
kupac2 = Kupac("Ana", "ana@example.com")

# Dodajemo proizvode
kupac1.dodaj_proizvod("Laptop")
kupac1.dodaj_proizvod("Telefon")
kupac1.dodaj_proizvod("Tablet")

kupac2.dodaj_proizvod("Monitor")
kupac2.dodaj_proizvod("Tastatura")

# Prikazujemo kupovine
kupac1.prikazi_kupovine()
kupac2.prikazi_kupovine()
