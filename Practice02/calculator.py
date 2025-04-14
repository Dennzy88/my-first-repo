# Deo zadatka 13

# calculator.py
class Calculator:
    def saberi(self, a, b):
        return a + b

    def oduzmi(self, a, b):
        return a - b

    def pomnozi(self, a, b):
        return a * b

    def podeli(self, a, b):
        if b == 0:
            raise ValueError("Deljenje nulom nije dozvoljeno.")
        return a / b