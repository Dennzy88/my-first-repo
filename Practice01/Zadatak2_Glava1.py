
class Student:
    def __init__(self, ime, prezime, broj_indeksa):
        self.ime = ime
        self.prezime = prezime
        self.broj_indeksa = broj_indeksa

    def prikazi_podatke(self):
        print(f"{self.ime} {self.prezime} - Indeks: {self.broj_indeksa}")
        

podaci = ["Marko", "Marković", 12345]
student = Student(*podaci)
student.prikazi_podatke()
