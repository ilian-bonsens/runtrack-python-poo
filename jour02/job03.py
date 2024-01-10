class Livre:
    def __init__(self, titre, auteur, pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages
        self.__disponible = True

    def get_titre(self):
        return self.__titre
    def get_auteur(self):
        return self.__auteur
    def get_pages(self):
        return self.__pages
    
    def set_titre(self, titre):
        self.__titre = titre
    def set_auteur(self, auteur):
        self.__auteur = auteur
    def set_pages(self, pages):
        if isinstance(pages, int) and pages > 0:
            self.__pages = pages
        else:
            print("Erreur: le nombre de pages doit être un entier positif.")

    def verification(self):
        return self.__disponible

    def emprunter(self):
        if self.verification():
            self.__disponible = False
        else:
            print("Erreur: le livre n'est pas disponible.")

    def rendre(self):
        if not self.verification():
            self.__disponible = True
        else:
            print("Erreur: le livre n'a pas été emprunté.")
