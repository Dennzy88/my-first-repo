"""
Zadatak 3:
Kreirati klasu `Pravougaonik` koja sadrži:
- a (dužina)
- b (širina)

Dodati metodu `povrsina()` koja vraća površinu pravougaonika,
i metodu `obim()` koja vraća obim.
"""
class Pravougaonik:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def povrsina(self):
        return self.a * self.b
    def obim(self):
        return 2 * (self.a + self.b)
    
# Test primer
podaci = [5, 10]
pravougaonik = Pravougaonik(*podaci)
print(f"Površina pravougaonika: {pravougaonik.povrsina()}")
print(f"Obim pravougaonika: {pravougaonik.obim()}")