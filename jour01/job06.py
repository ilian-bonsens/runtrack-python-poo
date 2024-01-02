class Animal:
    def __init__(self, age=0, prenom=""):
        self.age = age
        self.prenom = prenom
    
    def vieillir(self):
        self.age += 1
        print(f"L'animal a : {self.age} ans.")

    def nommer(self, nom):
        self.prenom = nom
        print(f"L'animal se nomme {self.prenom}.")

animal = Animal()
print(f"L'animal a : {animal.age} ans.")
animal.nommer("Nibi")
animal.vieillir()
