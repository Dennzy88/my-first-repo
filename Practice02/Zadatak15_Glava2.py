"""
Zadatak 15:
Koristeći modul `random`, napisati program koji:
- traži od korisnika da unese dve granice (donju i gornju)
- generiše i prikazuje jedan nasumičan broj između njih
"""
import random

lower = int(input("Unesite donju granicu: "))
upper = int(input("Unesite gornju granicu: "))
while True:
    if lower < upper:
        break
    print("Donja granica mora biti manja od gornje granice.")
    lower = int(input("Unesite donju granicu ponovo: "))
    upper = int(input("Unesite gornju granicu ponovo: "))
if lower < upper:
    random_number = random.randint(lower, upper)
    print(f"Nasumičan broj između {lower} i {upper} je: {random_number}")
else:
    print("Donja granica mora biti manja od gornje granice.")