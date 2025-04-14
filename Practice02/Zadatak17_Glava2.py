"""
Zadatak 17:
Koristeći `time` modul, napisati program koji:
- ispisuje odbrojavanje od 5 do 1
- između svakog broja napravi pauzu od 1 sekunde (time.sleep)
- na kraju ispiše: "Kreni!"
"""

import time
import random

# Odbrojavanje od 5 do 1
for i in range(5, 0, -1):
    print(i)
    time.sleep(1)  # Pauza od 1 sekunde između brojeva
print("Kreni!")

