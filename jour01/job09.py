class Produit:
    def __init__(self, nom, prixHT, TVA=20):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)
    
    def afficher(self):
        return f"Produit : {self.nom}\nPrix HT : {self.prixHT}\nTVA : {self.TVA}%\nPrix TTC : {self.CalculerPrixTTC()}"

    def definirNom(self):
        self.nom = input("Nom du produit : ")
    def definirPrixHT(self):
        self.prixHT = float(input("Prix HT : "))

produit = Produit("Banane", 2)
print(produit.afficher())
produit.definirNom()
produit.definirPrixHT()
print(produit.afficher())
