class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def afficherLesPoints(self):
        print(f"Coordonnées : {self.x}, {self.y}")

    def afficherX(self):
        print(f"Coordonnée X : {self.x}")
    def afficherY(self):
        print(f"Coordonnée Y : {self.y}")

    def changerX(self):
        self.x = input("Nouvelle coordonnée X : ")
    def changerY(self):
        self.y = input("Nouvelle coordonnée Y : ")

point = Point(34, 76)
point.afficherLesPoints()
point.changerX()
point.changerY()
point.afficherLesPoints()