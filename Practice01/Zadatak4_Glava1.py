"""
Zadatak 4:
Napraviti klasu `Racun` koja sadrži:
- broj_racuna
- vlasnik
- stanje (početno stanje na računu)

Dodati metode:
- `uplata(iznos)` – povećava stanje za dati iznos
- `isplata(iznos)` – smanjuje stanje ako ima dovoljno sredstava
- `prikazi_stanje()` – ispisuje trenutno stanje i vlasnika
"""
class Racun:
    def __init__(self, broj_racuna, vlasnik, stanje=0):
        self.broj_racuna = broj_racuna
        self.vlasnik = vlasnik
        self.stanje = stanje
        
    def uplata(self, iznos):
        if iznos > 0:
            self.stanje += iznos
            print(f"Uplata od {iznos} dinara uspešna.")
        else:
            print("Uplata nije uspešna. Iznos mora biti pozitivan.")
            
    def isplata(self, iznos):
        if iznos > 0 and iznos <= self.stanje:
            self.stanje -= iznos
            print(f"Isplata od {iznos} dinara uspešna.")
        elif iznos > self.stanje:
            print("Isplata nije uspešna. Nedovoljno sredstava.")
            
    def prikazi_stanje(self):
        print(f"Vlasnik: {self.vlasnik}, Broj računa: {self.broj_racuna}, Stanje: {self.stanje} dinara")
        
# Test primer
podaci = ["123456789", "Marko Marković", 10000]
racun = Racun(*podaci)
racun.prikazi_stanje()
racun.uplata(5000)
racun.prikazi_stanje()
racun.isplata(3000)
racun.prikazi_stanje()
racun.isplata(20000)  # Pokušaj isplate više od stanja
racun.prikazi_stanje()
racun.isplata(2000)  # Pokušaj isplate više od stanja
racun.prikazi_stanje()
racun.uplata(-1000)  # Pokušaj uplate negativnog iznosa
racun.prikazi_stanje()
racun.uplata(0)  # Pokušaj uplate nula
racun.prikazi_stanje()
racun.isplata(0)  # Pokušaj isplate nula
racun.prikazi_stanje()
        
        