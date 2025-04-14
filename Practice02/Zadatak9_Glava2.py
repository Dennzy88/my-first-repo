"""
Zadatak 9:
Napisati lambda funkciju koja proverava da li je broj paran.

Zatim primeniti `filter()` funkciju na listu brojeva kako bi se izdvojili samo parni brojevi.
"""
# Definišemo lambda funkciju koja proverava da li je broj paran

Brojevi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

proveri_paran = list(map(lambda x: x % 2 == 0, Brojevi))
print(f" Provera dali su parni brojevi iz liste: {Brojevi} : {proveri_paran}")

# Koristimo filter funkciju da izdvojimo samo parne brojeve
parni_brojevi = list(filter(lambda x: x % 2 == 0, Brojevi))
print(f"{parni_brojevi} su parni brojevi iz liste {Brojevi}")
