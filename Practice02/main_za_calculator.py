# Deo zadatka 13

# main_za_calculator.py
# Import the Calculator class from the calculator module
from calculator import Calculator

# Create an instance of the Calculator class
calculator = Calculator()

# Define a function to perform calculations based on user input

def perform_calculation():
    print("Dobrodošli u kalkulator!")


a = float(input("Unesite prvi broj: "))
b = float(input("Unesite drugi broj: "))

sabiranje = calculator.saberi(a, b)
oduzimanje = calculator.oduzmi(a, b)
mnozenje = calculator.pomnozi(a, b)
deljenje = calculator.podeli(a, b)

formats = {
    "Sabiranje": sabiranje,
    "Oduzimanje": oduzimanje,
    "Množenje": mnozenje,
    "Deljenje": deljenje
}

print(f"Sabiranje: {sabiranje}")
print(f"Oduzimanje: {oduzimanje}")
print(f"Množenje: {mnozenje}")
print(f"Deljenje: {deljenje}")


