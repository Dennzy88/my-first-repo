"""
Zadatak 11:
Koristeći `math` modul, napisati program koji:
- traži od korisnika da unese poluprečnik kruga
- izračunava i prikazuje:
  - obim kruga (2 * π * r)
  - površinu kruga (π * r^2)
"""
import math

# Tražimo od korisnika da unese poluprečnik kruga

poluprecnik = float(input("Unesite poluprečnik kruga: "))

obim = 2 * math.pi * poluprecnik
povrsina = math.pi * poluprecnik ** 2

print(f"Obim kruga je: {obim:.2f}")
print(f"Površina kruga je: {povrsina:.2f}")

