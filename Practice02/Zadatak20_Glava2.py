"""
Zadatak 20:
Napisati program koji:
- traži od korisnika da unese rečenicu
- računa:
    - broj reči
    - prosečnu dužinu reči
    - najdužu reč

Saveti:
Korak	Šta radiš	Primer
1.	input() za unos	"Unesi rečenicu: "
2.	split() da podeliš rečenicu	"Python je sjajan".split() → ['Python', 'je', 'sjajan']
3.	len(lista) da prebrojiš reči	
4.	sum(len(r) for r in lista) za ukupnu dužinu svih reči	
5.	max(lista, key=len) za najdužu reč
"""

# Unos rečenice od korisnika
recenica = input("Unesite rečenicu: ")

recenica = recenica.split()

# Računanje broja reči
broj_reci = len(recenica)

# Računanje prosečne dužine reči
duzina_recenice = sum(len(r) for r in recenica)
prosecna_duzina_reci = duzina_recenice / broj_reci

# Računanje najduže reči
najduza_rec = max(recenica, key=len)

# Ispis rezultata
print(f"Lista reči je: {recenica}")
print(f"Broj reči: {broj_reci}")
print(f"Prosečna dužina reči: {round(prosecna_duzina_reci, 2)}")
print(f"Najduža reč: {najduza_rec}")
print("Završeno!")
