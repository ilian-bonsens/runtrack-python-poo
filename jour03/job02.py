class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print(f"Numéro de compte : {self.__numero_compte}, Nom : {self.__nom}, Prénom : {self.__prenom}, Solde : {self.__solde}")

    def afficherSolde(self):
        print(f"Le solde du compte est de {self.__solde} euros.")

    def versement(self, montant):
        self.__solde += montant
        print(f"Versement de {montant} euros effectué. Nouveau solde : {self.__solde} euros.")

    def retrait(self, montant):
        if self.__solde - montant < 0 and not self.__decouvert:
            print("Erreur : solde insuffisant et aucun découvert autorisé.")
        else:
            self.__solde -= montant
            print(f"Retrait de {montant} euros effectué. Nouveau solde : {self.__solde} euros.")

    def agios(self):
        if self.__solde < 0:
            self.__solde *= 1.05  # Appliquer des agios de 5%
            print(f"Agios appliqués. Nouveau solde : {self.__solde} euros.")

    def virement(self, compte_destinataire, montant):
        if self.__solde - montant < 0 and not self.__decouvert:
            print("Erreur : solde insuffisant et aucun découvert autorisé.")
        else:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print(f"Virement de {montant} euros vers le compte {compte_destinataire.__numero_compte} effectué.")

# Créer des objets CompteBancaire
compte1 = CompteBancaire("123456", "Dupont", "Jean", 700, False)
compte2 = CompteBancaire("789101", "Durand", "Marie", -500, True)

# Faire un versement du premier compte vers le deuxième pour le remettre à zéro
compte1.virement(compte2, 600)