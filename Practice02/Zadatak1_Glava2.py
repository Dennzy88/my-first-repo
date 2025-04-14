class Trosak:
    def __init__(self, naziv, iznos, kategorija):
        self.naziv = naziv
        self.iznos = iznos
        self.kategorija = kategorija
        
    def prikazi(self):
        print(f"Naziv: {self.naziv}, Iznos: {self.iznos}RSD, Kategorija: {self.kategorija}")
    
    
trosak = Trosak("Struja", 3500, "Komunalije")
trosak.prikazi()