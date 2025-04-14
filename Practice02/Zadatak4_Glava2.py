"""
Zadatak 4:
Kreirati klasu `Film` sa sledećim atributima:
- naslov
- zanr
- ocena (ocena filma)

Dodati metodu `prikazi_film()` koja ispisuje podatke o filmu.

Dodati metodu `je_dobar()` koja vraća `True` ako je ocena veća ili jednaka 8, inače `False`.
"""
class Film:
    def __init__(self, naslov, zanr, ocena):
        self.naslov = naslov
        self.zanr = zanr
        self.ocena = ocena
        
    def prikazi_film(self):
        print(f"Film: {self.naslov}, Zanr: {self.zanr}, Ocena: {self.ocena}")
        
    def je_dobar(self):
        return self.ocena >= 8
    
# Primer korišćenja klase Film
film1 = Film("Inception", "Sci-Fi", 8.8)
film2 = Film("Titanic", "Romance", 7.8)
film1.prikazi_film()
print(f"Da li je film dobar? {'Da' if film1.je_dobar() else 'Ne'}")
film2.prikazi_film()
print(f"Da li je film dobar? {'Da' if film2.je_dobar() else 'Ne'}")