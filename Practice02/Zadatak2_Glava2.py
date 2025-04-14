"""
Zadatak 2:
Napraviti klasu `Knjiga` sa sledećim atributima:
- naslov
- autor
- godina_izdanja

Dodati metodu `prikazi_podatke()` koja ispisuje sve informacije o knjizi.
"""
class Knjiga:
    def __init__(self, naslov, autor, godina_izdanja):
        self.naslov = naslov
        self.autor = autor
        self.godina_izdanja = godina_izdanja
        
    def prikazi_podatke(self):
        print(f"Naslov: {self.naslov}, Autor: {self.autor}, Godina izdanja: {self.godina_izdanja}")
        
   
        
Knjiga1 = Knjiga("1984", "George Orwell", 1949)
Knjiga2 = Knjiga("Ponos i predrasude", "Jane Austen", 1813)
Knjiga3 = Knjiga("Mali princ", "Antoine de Saint-Exupéry", 1943)
Knjiga4 = Knjiga("Ubiti pticu rugalicu", "Harper Lee", 1960)
Knjiga5 = Knjiga("Gospodar muva", "William Golding", 1954)

for knjiga in [Knjiga1, Knjiga2, Knjiga3, Knjiga4, Knjiga5]:
    if knjiga.godina_izdanja < 1950:
        print(f"{knjiga.naslov} je izdat pre 1950. godine.")
    else:
        print(f"{knjiga.naslov} je izdat posle 1950. godine.")


Knjiga1.prikazi_podatke()
Knjiga2.prikazi_podatke()
Knjiga3.prikazi_podatke()
Knjiga4.prikazi_podatke()
Knjiga5.prikazi_podatke()


