class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    # afficher les dimensions
    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur
    
    # modifier les dimensions
    def set_longueur(self, longueur):
        self.__longueur = longueur

    def set_largeur(self, largeur):
        self.__largeur = largeur

Rectangle1 = Rectangle(10, 5)

print(Rectangle1.get_longueur(), Rectangle1.get_largeur())

Rectangle1.set_longueur(20), Rectangle1.set_largeur(12)

print(Rectangle1.get_longueur(), Rectangle1.get_largeur())


