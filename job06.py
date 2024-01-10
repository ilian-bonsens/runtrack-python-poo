class Commande:
    def __init__(self, numero):
        self.__numero = numero
        self.__plats = {}
        self.__statut = "en cours"

    def ajouter_plat(self, nom, prix):
        self.__plats[nom] = prix

    def annuler(self):
        self.__statut = "annulée"
        print(f"Commande n°{self.__numero} annulée.")

    def __calculer_total(self):
        return sum(self.__plats.values())

    def afficher_commande(self):
        print(f"Commande n°{self.__numero} :")
        for nom, prix in self.__plats.items():
            print(f"- {nom} : {prix}€")
        print(f"Total à payer : {self.__calculer_total()}€")

    def calculer_tva(self, taux):
        return self.__calculer_total() * taux / 100

commande1 = Commande(1)
commande1.ajouter_plat("Pizza", 10)
commande1.ajouter_plat("Salade", 5)
commande1.afficher_commande()
print(f"TVA : {commande1.calculer_tva(20)}€")
commande1.annuler()
