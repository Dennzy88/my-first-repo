"""
Zadatak 8:
Kreirati klasu `Proizvod` sa sledećim atributima:
- naziv
- cena
- kolicina

Dodati metode:
- `ukupna_vrednost()` – vraća ukupnu vrednost zaliha (cena * kolicina)
- `prikazi()` – prikazuje sve informacije o proizvodu
"""
class Proizvod:
    def __init__(self, naziv, cena, kolicina):
        self.naziv = naziv
        self.cena = cena
        self.kolicina = kolicina
        
    def ukupna_vrednost(self):
        return self.cena * self.kolicina
    
    def prikazi(self):
        print(f"Proizvod: {self.naziv}, Cena: {self.cena}, Kolicina: {self.kolicina}, Ukupna vrednost: {self.ukupna_vrednost()}")

# Kreiranje proizvoda
Proizvodi = [
    Proizvod("Laptop", 1000, 5),
    Proizvod("Telefon", 500, 10),
    Proizvod("Monitor", 300, 7),
    Proizvod("Tastatura", 50, 20),
    Proizvod("Mis", 25, 15),
    Proizvod("Zvučnici", 150, 8),
    Proizvod("Mikrofon", 100, 12),
    Proizvod("Web kamera", 200, 6),
]

# Prikaz informacija o proizvodima i ukupne vrednosti svih proizvoda
ukupna_vrednost_svih_proizvoda = 0
for proizvod in Proizvodi:
    proizvod.prikazi()
    ukupna_vrednost_svih_proizvoda += proizvod.ukupna_vrednost()

print(f"Ukupna vrednost svih proizvoda: {ukupna_vrednost_svih_proizvoda}")