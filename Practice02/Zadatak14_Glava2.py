"""
Zadatak 14:
Napraviti program koji koristi `math` modul za:
- računanje apsolutne vrednosti broja (math.fabs)
- računanje kvadratnog korena (math.sqrt)
- stepenovanje broja (math.pow)
Korisnik unosi vrednosti.
"""
import math

# Funkcija za unos broja od strane korisnika
def unos_broja():
    while True:
        try:
            broj = float(input("Unesite broj: "))
            return broj
        except ValueError:
            print("Greška! Molimo unesite validan broj.")
            

# Funkcija za izračunavanje apsolutne vrednosti
def izracunaj_abs(broj):
    return math.fabs(broj)


# Funkcija za izračunavanje kvadratnog korena
def izracunaj_kvadratni_koren(broj):
    if broj < 0:
        raise ValueError("Negativan broj ne može imati kvadratni koren.")
    return math.sqrt(broj)


# Funkcija za izračunavanje stepena
def izracunaj_stepen(broj, stepen):
    return math.pow(broj, stepen)


# Glavna funkcija koja poziva ostale funkcije
def main():
    print("Dobrodošli u program za izračunavanje!")
    
    # Unos broja od strane korisnika
    broj = unos_broja()
    
    # Izračunavanje apsolutne vrednosti
    abs_broj = izracunaj_abs(broj)
    print(f"Apsolutna vrednost {broj} je: {abs_broj}")
    
    # Izračunavanje kvadratnog korena
    try:
        kvadratni_koren = izracunaj_kvadratni_koren(broj)
        print(f"Kvadratni koren {broj} je: {kvadratni_koren}")
    except ValueError as e:
        print(e)
    
    # Unos stepena od strane korisnika
    stepen = unos_broja()
    
    # Izračunavanje stepena
    rezultat_stepena = izracunaj_stepen(broj, stepen)
    print(f"{broj} na stepen {stepen} je: {rezultat_stepena}")

if __name__ == "__main__":
    main()
