import math
class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self):
        self.rayon = input("Entrez le nouveau rayon : ")

    def circonférence(self):
        return (2 * math.pi * self.rayon) 
    def aire(self):
        return (3.14 * self.rayon * self.rayon)
    def diametere(self):
        return (2 * self.rayon)
    
    def afficherInfos(self):
        print(f"Rayon : {self.rayon}\nCirconférence : {self.circonférence()}\nAire : {self.aire()}\nDiamètre : {self.diametere()}")

cercle1 = Cercle(4)
cercle1.afficherInfos()
cercle2 = Cercle(7)
cercle2.afficherInfos()