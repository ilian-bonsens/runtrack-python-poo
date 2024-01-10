class Voiture:
    def __init__(self, marque, modele, annee, kilometrage, en_marche=False):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = en_marche
        self.__reservoir = 50

    def get_marque(self):
        return self.__marque
    def get_modele(self):
        return self.__modele
    def get_annee(self):
        return self.__annee
    def get_kilometrage(self):
        return self.__kilometrage
    def get_en_marche(self):
        return self.__en_marche
    
    def set_marque(self, marque):
        self.__marque = marque
    def set_modele(self, modele):
        self.__modele = modele
    def set_annee(self, annee):
        self.__annee = annee
    def set_kilometrage(self, kilometrage):
        if isinstance(kilometrage, int) and kilometrage >= 0:
            self.__kilometrage = kilometrage
        else:
            print("Erreur: le kilométrage doit être un entier positif.")

    def demarrer(self):
        if self.__verifier_plein() > 5:
            self.__en_marche = True
            print("La voiture démarre.")
        else:
            print("Erreur: le réservoir est presque vide.")
    def arreter(self):
        if not self.__en_marche:
            print("Erreur: la voiture est déjà à l'arrêt.")
        else:
            self.__en_marche = False
            print("La voiture s'arrête.")

    def __verifier_plein(self):
        return self.__reservoir
    
voiture = Voiture("Peugeot", "308", 2017, 10000)
voiture.demarrer()