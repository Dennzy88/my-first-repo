"""
Zadatak 23:
Napisati program koji:
- omogućava korisniku da unese više brojeva (kroz `input()`)
- čuva ih u listi
- na kraju ispisuje:
    - sve unete brojeve
    - broj unetih brojeva
    - njihov zbir
    - prosečnu vrednost
"""

zadati_brojevi = input("Unesite brojeve odvojene zarezom: ")
brojevi = zadati_brojevi.split(",")  # Delimo string na osnovu zareza

brojevi = [int(broj.strip()) for broj in brojevi]  # Uklanjamo razmake i konvertujemo u int
broj_unetih_brojeva = len(brojevi)  # Broj unetih brojeva
zbir_brojeva = sum(brojevi)  # Zbir svih brojeva
prosecna_vrednost = zbir_brojeva / broj_unetih_brojeva  # Prosečna vrednost

resultati = [brojevi, broj_unetih_brojeva, zbir_brojeva, prosecna_vrednost]
for r in resultati:
    print(r)
    
print(f"Svi uneti brojevi su: {brojevi}")
print(f"Broj unetih brojeva je: {broj_unetih_brojeva}")
print(f"Zbir svih brojeva je: {zbir_brojeva}")
print(f"Prosečna vrednost je: {prosecna_vrednost}")
print("Završeno!")
# Objašnjenje:
# - `input()` uzima unos od korisnika kao string
# - `split(",")` deli string na osnovu zareza i vraća listu
# - `strip()` uklanja razmake oko brojeva
# - `int()` konvertuje string u int
# - `len()` vraća broj elemenata u listi
# - `sum()` vraća zbir svih elemenata u listi
