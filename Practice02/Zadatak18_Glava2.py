"""
Zadatak 18:
Napisati program koji:
- postavlja korisniku jednostavno pitanje (npr. 3 + 4)
- meri vreme od postavljanja pitanja do odgovora (koristi time.time())
- na kraju ispisuje koliko sekundi je korisniku trebalo
"""
import time


# Postavljamo pitanje korisniku
question = "Koliko je 3 + 4?"
correct_answer = 7
print(question)
print("Molimo vas da unesete vaš odgovor.")
print("Unesite 'q' za izlaz.")

for i in range(5, 0, -1):
    print(i)
    time.sleep(1)  # Pauza od 1 sekunde između brojeva
print("Kreni!")

start_time = time.time()  # Početno vreme
user_answer = input("Vaš odgovor: ")
end_time = time.time()  # Krajnje vreme

elapsed_time = end_time - start_time  # Izračunavamo vreme trajanja
while True:
    if user_answer == 'q':
        print("Izlaz iz programa.")
        break
    try:
        user_answer = int(user_answer)
        if user_answer == correct_answer:
            print("Tačno!")
            break
        else:
            print("Netačno! Pokušajte ponovo.")
            user_answer = input("Vaš odgovor: ")
    except ValueError:
        print("Molimo unesite validan broj ili 'q' za izlaz.")
        user_answer = input("Vaš odgovor: ")


print(f"Odgovorio si za {round(end_time - start_time, 2)} sekundi.")

    

