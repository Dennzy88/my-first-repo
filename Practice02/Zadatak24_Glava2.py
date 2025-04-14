"""
Zadatak 24:
Napisati program koji:
- postavlja korisniku tri pitanja (po želji)
- čuva tačne odgovore
- upoređuje korisničke odgovore sa tačnim
- na kraju prikazuje broj tačnih odgovora
"""

# Lista pitanja i tačnih odgovora
pitanja = [
    "1. Koji je glavni grad Srbije? ",
    "2. Koliko je 5 + 3? ",
    "3. Kako se zove osnivač Microsofta? "
]

tacni_odgovori = [
    "beograd",
    "8",
    "bill gates"
]

# Brojač tačnih odgovora
poeni = 0

# Prolazimo kroz svako pitanje
for i in range(len(pitanja)):
    odgovor = input(pitanja[i]).strip().lower()
    if odgovor == tacni_odgovori[i]:
        print("✅ Tačno!\n")
        poeni += 1
    else:
        print(f"❌ Netačno! Tačan odgovor je: {tacni_odgovori[i].title()}\n")

# Rezultat
print(f"Ukupan broj tačnih odgovora: {poeni} od {len(pitanja)}")
print("Završeno!")
# Objašnjenje:
# - `strip()` uklanja razmake oko odgovora
# - `lower()` konvertuje odgovor u mala slova radi lakšeg poređenja
# - `title()` konvertuje prvi karakter u veliko slovo radi lepšeg ispisa
# - `len(pitanja)` vraća ukupan broj pitanja
# - `poeni` broji tačne odgovore
# - `print()` ispisuje rezultate
