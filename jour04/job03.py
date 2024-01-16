class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    def surface(self):
        return self.__longueur * self.__largeur

    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def set_largeur(self, largeur):
        self.__largeur = largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    def volume(self):
        return self.get_longueur() * self.get_largeur() * self.__hauteur

rectangle = Rectangle(8, 13)
parallelepipede = Parallelepipede(5, 4, 9)
print(f"Périmètre du rectangle : {rectangle.perimetre()}m")
print(f"Surface du rectangle : {rectangle.surface()}m²")
print(f"Volume du parallélépipède : {parallelepipede.volume()}m³")
