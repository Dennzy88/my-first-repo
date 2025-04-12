class Calculator:
    def __init__(self, number1):
        self.result = number1  # početna vrednost
    
    def add(self, b):
        self.result += b
        return self.result
    
    def sub(self, b):
        self.result -= b
        return self.result
    
    def mul(self, b):
        self.result *= b
        return self.result
    
    def div(self, b):
        if b == 0:
            return "Greška: Deljenje sa nulom!"
        self.result /= b
        return self.result

# --- Početak rada ---
print("Pametni kalkulator (sa pamćenjem rezultata)")
print("Unesi 'exit' da izađeš iz programa.\n")

# Prvi broj mora da se unese
while True:
    try:
        start = float(input("Unesi početni broj: "))
        break
    except ValueError:
        print("Greška: Unesi ispravan broj!")

calc = Calculator(start)

# Glavna petlja
while True:
    print(f"\nTrenutni rezultat: {calc.result}")
    operacija = input("Unesi operaciju (+, -, *, /) ili 'exit': ")

    if operacija == "exit":
        print("Izlazak iz kalkulatora. Završni rezultat:", calc.result)
        break

    try:
        broj = float(input("Unesi sledeći broj: "))
    except ValueError:
        print("Greška: Unos mora biti broj!")
        continue

    # Izvršavanje operacije
    if operacija == "+":
        print("Rezultat:", calc.add(broj))
    elif operacija == "-":
        print("Rezultat:", calc.sub(broj))
    elif operacija == "*":
        print("Rezultat:", calc.mul(broj))
    elif operacija == "/":
        rezultat = calc.div(broj)
        print("Rezultat:", rezultat)
        if rezultat == "Greška: Deljenje sa nulom!":
            break  # možeš i da nastaviš umesto break
    else:
        print("Nepoznata operacija!")
