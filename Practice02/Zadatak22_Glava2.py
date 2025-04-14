"""
Zadatak 22:
Napisati program koji:
- prikazuje tabelu brojeva od 1 do 10
- za svaki broj prikazuje i njegov kvadrat
- formatirati ispis u dve kolone:
    Broj     Kvadrat
"""

# Naslov tabele
print("Broj\tKvadrat")
print("-" * 20)

# Petlja kroz brojeve od 1 do 10
for broj in range(1, 11):
    kvadrat = broj ** 2
    print(f"{broj}\t{kvadrat}")
print("Završeno!")

"""
Objašnjenje:
\t pravi tabulator, pa brojevi i kvadrati lepo stoje u koloni

range(1, 11) pravi brojeve od 1 do 10

broj ** 2 računa kvadrat
"""