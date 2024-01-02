class Personnage:
    def  __init__(self, x, y):
        self.x = x
        self.y = y

    def gauche(self):
        self.x -= 1
        print("Déplacement à gauche")
    def droite(self):
        self.x += 1
        print("Déplacement à droite")
    def haut(self):
        self.y += 1
        print("Déplacement en haut")
    def bas(self):
        print("Déplacement en bas")
        self.y -= 1

    def position(self):
        print(f"Position : ({self.x}, {self.y})")

perso = Personnage(10, 10)
perso.position()
perso.gauche()
perso.haut()
perso.position()