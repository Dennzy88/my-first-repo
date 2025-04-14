"""
Zadatak 16:
Napisati program koji:
- nasumično bira broj od 1 do 100 (koristi random.randint)
- traži od korisnika da pogodi broj
- daje poruke: "Manje!", "Veće!" ili "Pogodak!"
- broji broj pokušaja
"""
# Prosirio sam zadatak tako da dodam odbrojavanje i pauzu između brojeva
import time
import random

# Odbrojavanje od 5 do 1
for i in range(5, 0, -1):
    print(i)
    time.sleep(1)  # Pauza od 1 sekunde između brojeva
print("Kreni!")


# Generišemo nasumičan broj između 1 i 100
random_number = random.randint(1, 100)
attempts = 0
guessed = False

print("Pogodi broj između 1 i 100!")

if random_number == 1:
    print("Nasumičan broj je 1.")
elif random_number == 100:
    print("Nasumičan broj je 100.")
else:
    print("Nasumičan broj je između 2 i 99.")
    
while not guessed:
    try:
        user_guess = int(input("Unesite vaš pokušaj: "))
        attempts += 1

        if user_guess < random_number:
            print("Manje!")
        elif user_guess > random_number:
            print("Veće!")
        else:
            guessed = True
            print(f"Pogodili ste broj {random_number} u {attempts} pokušaja!")
    except ValueError:
        print("Molimo unesite validan broj.")