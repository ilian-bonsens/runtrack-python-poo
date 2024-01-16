class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        return f"Marque : {self.marque}\nModèle : {self.modele}\nAnnée : {self.annee}\nPrix : {self.prix}€"

    def demarrer(self):
        return "Attention, je roule"


class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, portes=4):
        super().__init__(marque, modele, annee, prix)
        self.portes = portes

    def informationsVehicule(self):
        return super().informationsVehicule() + f", Portes : {self.portes}"

    def demarrer(self):
        return "Vroom, la voiture démarre"


class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roues=2):
        super().__init__(marque, modele, annee, prix)
        self.roues = roues

    def informationsVehicule(self):
        return super().informationsVehicule() + f"\nRoues : {self.roues}"

    def demarrer(self):
        return "Vroom, la moto démarre"

voiture = Voiture("Peugeot", "208", 2020, 15000)
print(voiture.informationsVehicule())
print(voiture.demarrer())

moto = Moto("Yamaha", "MT-07", 2021, 7500)
print(moto.informationsVehicule())
print(moto.demarrer())
