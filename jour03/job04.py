class Joueur:
    def __init__(self, nom, numero, position):
        self.__nom = nom
        self.__numero = numero
        self.__position = position
        self.__buts = 0
        self.__passes = 0
        self.__cartons_jaunes = 0
        self.__cartons_rouges = 0

    def marquerUnBut(self):
        self.__buts += 1

    def effectuerUnePasseDecisive(self):
        self.__passes += 1

    def recevoirUnCartonJaune(self):
        self.__cartons_jaunes += 1

    def recevoirUnCartonRouge(self):
        self.__cartons_rouges += 1

    def afficherStatistiques(self):
        print(f"Nom : {self.__nom}, Numéro : {self.__numero}, Position : {self.__position}, Buts : {self.__buts}, Passes : {self.__passes}, Cartons jaunes : {self.__cartons_jaunes}, Cartons rouges : {self.__cartons_rouges}")


class Equipe:
    def __init__(self, nom):
        self.__nom = nom
        self.__joueurs = []

    def ajouterJoueur(self, joueur):
        self.__joueurs.append(joueur)

    def afficherStatistiquesJoueurs(self):
        for joueur in self.__joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, nom, buts, passes, cartons_jaunes, cartons_rouges):
        for joueur in self.__joueurs:
            if joueur.get_nom() == nom:
                joueur.set_buts(buts)
                joueur.set_passes(passes)
                joueur.set_cartons_jaunes(cartons_jaunes)
                joueur.set_cartons_rouges(cartons_rouges)
                break

# Créer des instances de Joueur
joueur1 = Joueur("Mbappé", 7, "Attaquant")
joueur2 = Joueur("Tchouameni", 6, "Milieu")
joueur3 = Joueur("Konate", 4, "Défenseur")

# Créer une instance de Equipe
equipe = Equipe("France")

# Ajouter les joueurs à l'équipe
equipe.ajouterJoueur(joueur1)
equipe.ajouterJoueur(joueur2)
equipe.ajouterJoueur(joueur3)

# Afficher les statistiques des joueurs
equipe.afficherStatistiquesJoueurs()

# Simuler un match
joueur1.marquerUnBut()
joueur2.effectuerUnePasseDecisive()
joueur1.marquerUnBut()
joueur2.recevoirUnCartonJaune()
joueur3.recevoirUnCartonRouge()

# Afficher à nouveau les statistiques des joueurs
equipe.afficherStatistiquesJoueurs()
