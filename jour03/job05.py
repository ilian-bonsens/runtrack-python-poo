class Personnage:
    def __init__(self, nom, vie):
        self.__nom = nom
        self.__vie = vie

    def attaquer(self, adversaire, niveau):
        adversaire.__vie -= niveau
        print(f"{self.__nom} attaque et inflige {niveau} points de dégâts à {adversaire.get_nom()}.")

    def defendre(self, niveau):
        self.__vie += niveau
        print(f"{self.__nom} se défend et récupère {niveau} points de vie.")

    def est_vivant(self):
        return self.__vie > 0

    def get_nom(self):
        return self.__nom

    def get_vie(self):
        return self.__vie


class Jeu:
    def __init__(self):
        self.__niveau = 0
        self.__joueur = None
        self.__ennemi = None

    def choisirNiveau(self):
        self.__niveau = int(input("Choisissez le niveau de difficulté (1-3) : "))

    def lancerJeu(self):
        vie_joueur = 10 * (4 - self.__niveau)
        vie_ennemi = 5 * self.__niveau
        self.__joueur = Personnage("Joueur", vie_joueur)
        self.__ennemi = Personnage("Ennemi", vie_ennemi)

    def jouer(self):
        while self.__joueur.est_vivant() and self.__ennemi.est_vivant():
            choix = input("Voulez-vous attaquer ou défendre ? (a/d) : ")
            if choix == 'a':
                self.__joueur.attaquer(self.__ennemi, self.__niveau)
            elif choix == 'd':
                self.__joueur.defendre(self.__niveau)
            print(f"{self.__joueur.get_nom()} a {self.__joueur.get_vie()} points de vie.")
            print(f"{self.__ennemi.get_nom()} a {self.__ennemi.get_vie()} points de vie.")
            if self.__ennemi.est_vivant():
                self.__ennemi.attaquer(self.__joueur, self.__niveau)

        if self.__joueur.est_vivant():
            print(f"{self.__joueur.get_nom()} a gagné !")
        else:
            print(f"{self.__ennemi.get_nom()} a gagné !")


# Créer une instance de Jeu
jeu = Jeu()

# Choisir le niveau de difficulté
jeu.choisirNiveau()

# Lancer le jeu
jeu.lancerJeu()

# Jouer le jeu
jeu.jouer()

