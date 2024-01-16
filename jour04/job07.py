import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu:
    def __init__(self):
        self.paquet = [Carte(valeur, couleur) for valeur in range(1, 14) for couleur in ['Coeur', 'Carreau', 'Trefle', 'Pique']]

    def valeur_carte(self, carte):
        if carte.valeur > 10:
            return 10
        elif carte.valeur == 1:
            return 11
        else:
            return carte.valeur

    def jouer(self):
        main_joueur = random.sample(self.paquet, 2)
        print(f"Vos cartes sont {main_joueur[0].valeur} de {main_joueur[0].couleur} et {main_joueur[1].valeur} de {main_joueur[1].couleur}.")
        main_croupier = random.sample(self.paquet, 2)
        print(f"La première carte du croupier est {main_croupier[0].valeur} de {main_croupier[0].couleur}.")

        score_joueur = sum(self.valeur_carte(carte) for carte in main_joueur)
        score_croupier = sum(self.valeur_carte(carte) for carte in main_croupier)

        while score_joueur < 21:
            choix = input("Voulez-vous prendre une autre carte ? (Oui/Non) ")
            if choix.lower() == "oui":
                carte = random.choice(self.paquet)
                score_joueur += self.valeur_carte(carte)
                print(f"Votre nouvelle carte est {carte.valeur} de {carte.couleur}. Votre score est maintenant {score_joueur}.")
            else:
                break

        while score_croupier < 17:
            carte = random.choice(self.paquet)
            score_croupier += self.valeur_carte(carte)
            print(f"La nouvelle carte du croupier est {carte.valeur} de {carte.couleur}. Son score est maintenant {score_croupier}.")

        if score_joueur > 21:
            return "Vous avez dépassé 21. Vous avez perdu."
        elif score_croupier > 21:
            return "Le croupier a dépassé 21. Vous avez gagné."
        elif score_joueur > score_croupier:
            return "Vous avez gagné."
        else:
            return "Le croupier a gagné."

jeu = Jeu()
print(jeu.jouer())
