"""
Zadatak 3:
Napraviti klasu `Zaposleni` sa sledećim atributima:
- ime
- pozicija
- plata

Dodati metodu `povecaj_platu(iznos)` koja povećava platu za dati iznos.

Dodati metodu `prikazi_info()` koja ispisuje podatke o zaposlenom.
"""
class Zaposleni:
    def __init__(self, ime, pozicija, plata):
        self.ime = ime
        self.pozicija = pozicija
        self.plata = plata
        
    def povecaj_platu(self, iznos):
        self.plata += iznos
        
    def prikazi_info(self):
        print(f"Ime: {self.ime}, Pozicija: {self.pozicija}, Plata: {self.plata} RSD")
        
Zaposleni1 = Zaposleni("Marko Marković", "Programer", 80000)
Zaposleni2 = Zaposleni("Ana Anić", "Menadžer", 90000)
Zaposleni3 = Zaposleni("Petar Petrović", "Analitičar", 70000)

print("Pre povećanja plata:")
Zaposleni1.prikazi_info()
Zaposleni2.prikazi_info()
Zaposleni3.prikazi_info()
print("\nNakon povećanja plata:")
Zaposleni1.povecaj_platu(10000)
Zaposleni2.povecaj_platu(15000)
Zaposleni3.povecaj_platu(5000)
Zaposleni1.prikazi_info()
Zaposleni2.prikazi_info()
Zaposleni3.prikazi_info()