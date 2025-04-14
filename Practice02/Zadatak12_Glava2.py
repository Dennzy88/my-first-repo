"""
Zadatak 12:
Napisati program koji koristi `math.sin()` da izračuna
sinus uglova od 0° do 90° u koracima od 15 stepeni.
Rezultat prikazati sa 4 decimale.
"""
import math
# Definišemo uglove u stepenima
uglove = [0, 15, 30, 45, 60, 75, 90]
# Inicijalizujemo praznu listu za rezultate
sinus = []
# Koristimo petlju da izračunamo sinus za svaki ugao
for ugao in uglove:
    # Konvertujemo stepeni u radijane
    radijan = math.radians(ugao)
    # Izračunavamo sinus
    sinus.append(math.sin(radijan))
# Prikazujemo rezultate sa 4 decimale
for i in range(len(uglove)):
    print(f"Sinus {uglove[i]}° = {sinus[i]:.4f}")
    