
#Napraviti klasu `Zivotinja` koja sadrži:
#- naziv
#- vrsta
#- starost

#Dodati metodu `prikazi()` koja prikazuje informacije o životinji.

#Dodati metodu `da_li_je_mlada()` koja vraća True ako je životinja mlađa od 5 godina, inače False.


class Zivotinja:
    def __init__(self, naziv, vrsta, starost):
        self.naziv = naziv
        self.vrsta = vrsta
        self.starost = starost
        
    def prikazi(self):
        print(f"Zivotinja: {self.naziv}, Vrsta: {self.vrsta}, Starost: {self.starost} godina")
    
    def da_li_je_mlada(self):
        return self.starost < 5
    
Zivotinja1 = Zivotinja("Miki", "Pas", 3)
Zivotinja2 = Zivotinja("Maca", "Macka", 6)
Zivotinja3 = Zivotinja("Cica", "Papagaj", 2)
Zivotinja4 = Zivotinja("Roki", "Zec", 4)

Prikazi = [Zivotinja1, Zivotinja2, Zivotinja3, Zivotinja4]
for zivotinja in Prikazi:
    zivotinja.prikazi()
    if zivotinja.da_li_je_mlada():
        print(f"{zivotinja.naziv} je mlada životinja.")
    else:
        print(f"{zivotinja.naziv} nije mlada životinja.")
    print()