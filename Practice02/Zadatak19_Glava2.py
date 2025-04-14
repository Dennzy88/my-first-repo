"""
Zadatak 19:
Napisati program koji:
- ima listu brojeva
- ispisuje:
    - najveći broj
    - najmanji broj
    - zbir svih brojeva
    - prosečnu vrednost
"""
# Funkcije koje koristiš:
# Funkcija	Značenje
# max(lista)	Najveći broj
# min(lista)	Najmanji broj
# sum(lista)	Zbir
# len(lista)	Broj elemenata
# sum(lista) / len(lista)	Prosek

brojevi = [10, 20, 5, 7, 12]

najveci_broj = max(brojevi)
najmanji_broj = min(brojevi)
zbir_brojeva = sum(brojevi)
prosecna_vrednost = sum(brojevi) / len(brojevi)


results = [najveci_broj, najmanji_broj, zbir_brojeva, prosecna_vrednost]
for r in results:
    print(r)
    
print(f"Najveći broj je: {najveci_broj}")
print(f"Najmanji broj je: {najmanji_broj}")
print(f"Zbir svih brojeva je: {zbir_brojeva}")
print(f"Prosečna vrednost je: {prosecna_vrednost}")
print("Završeno!")