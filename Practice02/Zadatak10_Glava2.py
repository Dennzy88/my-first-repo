"""
Zadatak 10:
Napisati program koji koristi `map()` i `lambda` funkciju
da pretvori sva imena u listi u velika slova (uppercase).
"""

lista_imena = ["ana", "marko", "jelena", "nikola"]

imena_veliko_slovo = list(map(lambda x: x.upper(), lista_imena))
print(f"Lista imena velika slova: {imena_veliko_slovo}")