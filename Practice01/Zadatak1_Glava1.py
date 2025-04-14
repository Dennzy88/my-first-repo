class Car:
    def __init__(self, marka, model, godina_proizvodnje):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje

    def prikazi_info(self):
        print("Informacije o automobilu:")
        print(f"Marka: {self.marka}")
        print(f"Model: {self.model}")
        print(f"Godina proizvodnje: {self.godina_proizvodnje}")

# Test primer
podaci = ["Toyota", "Corolla", 2020]
car = Car(*podaci)
car.prikazi_info()
