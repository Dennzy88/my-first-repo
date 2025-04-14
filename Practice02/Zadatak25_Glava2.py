"""
Napisati program koji:
- omogućava korisniku da unese više kontakata (ime, telefon, email)
- čuva ih u listi (svaki kontakt kao rečnik)
- prikazuje sve kontakte u tabeli

Deo koda	Značenje
imenik = []	Lista u koju čuvaš sve kontakte
kontakt = {}	Svaki kontakt je rečnik sa imenom, telefonom i emailom
kontakt.append()	Dodaješ svaki novi kontakt u listu
while True	Unos više kontakata dok korisnik ne unese "kraj"
f"{'Ime':<15}"	Formatiraš kolone za prikaz u tabeli
"""
# Inicijalizacija praznog imenika
imenik = []

print("Dobrodošli u digitalni imenik!")
print("Unosite kontakte, unesite 'kraj' za ime kada želite da završite.\n")

while True:
    ime = input("Unesite ime kontakta: ")
    if ime.lower() == "kraj":
        break
    telefon = input("Unesite broj telefona: ")
    email = input("Unesite email adresu: ")
    
    # Dodavanje kontakta kao rečnik u listu
    kontakt = {
        "Ime": ime.title(),
        "Telefon": telefon,
        "Email": email.lower()
    }
    imenik.append(kontakt)
    print("Kontakt sačuvan!\n")

# Prikaz svih kontakata
print("\n IMENIK KONTAKATA")
print("-" * 40)
print(f"{'Ime':<15}{'Telefon':<15}{'Email'}")
print("-" * 40)

for k in imenik:
    print(f"{k['Ime']:<15}{k['Telefon']:<15}{k['Email']}")
