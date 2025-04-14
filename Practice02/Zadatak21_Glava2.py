"""
Zadatak 21:
Napisati program koji:
- traži od korisnika da unese rečenicu
- računa:
    - broj slova (zanemari razmake i interpunkciju)
    - broj samoglasnika (A, E, I, O, U)
    - broj suglasnika
"""

# Unos rečenice
recenica = input("Unesite rečenicu: ")

# Pretvaramo sve u mala slova radi lakše provere
recenica = recenica.lower()

# Definišemo skup samoglasnika
samoglasnici = "aeiou"

# Inicijalizujemo brojače
broj_slova = 0
broj_samoglasnika = 0
broj_suglasnika = 0

# Prolazimo kroz svaki karakter u rečenici
for znak in recenica:
    if znak.isalpha():  # Uzimamo u obzir samo slova
        broj_slova += 1
        if znak in samoglasnici:
            broj_samoglasnika += 1
        else:
            broj_suglasnika += 1

# Ispis rezultata
print(f"Broj slova: {broj_slova}")
print(f"Broj samoglasnika: {broj_samoglasnika}")
print(f"Broj suglasnika: {broj_suglasnika}")
print("Završeno!")