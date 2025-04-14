"""
Zadatak 7:
Napraviti klasu `Student` sa sledećim atributima:
- ime
- broj_indeksa
- ocene (lista ocena)

Dodati metode:
- `dodaj_ocenu(ocena)` – dodaje ocenu u listu
- `prosek()` – vraća prosečnu ocenu studenta
"""
class Student:
    def __init__(self, ime, broj_indeksa):
        self.ime = ime
        self.broj_indeksa = broj_indeksa
        self.ocene = []

    def dodaj_ocenu(self, ocena):
        self.ocene.append(ocena)
        
    def prosek(self):
        if not self.ocene:
            return 0
        return sum(self.ocene) / len(self.ocene)

# Kreiramo studente
student1 = Student("Marko", "12345")
student2 = Student("Ana", "67890")
student3 = Student("Petar", "54321")
student4 = Student("Jelena", "09876")

Studenti = [student1, student2, student3, student4]
# Dodajemo ocene studentima
student1.dodaj_ocenu(8)
student1.dodaj_ocenu(9)
student1.dodaj_ocenu(10)
student2.dodaj_ocenu(7)
student2.dodaj_ocenu(8)
student2.dodaj_ocenu(9)
student3.dodaj_ocenu(6)
student3.dodaj_ocenu(7)
student3.dodaj_ocenu(8)
student4.dodaj_ocenu(9)
student4.dodaj_ocenu(10)
student4.dodaj_ocenu(9)

# Prikazujemo prosečne ocene studenata
for student in Studenti:
    print(f"Student: {student.ime}, Broj indeksa: {student.broj_indeksa}, Prosek: {student.prosek():.2f}")
# Output: