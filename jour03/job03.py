class Tache:
    def __init__(self, titre, description, statut="à faire"):
        self.__titre = titre
        self.__description = description
        self.__statut = statut

    def get_titre(self):
        return self.__titre

    def get_statut(self):
        return self.__statut

    def set_statut(self, statut):
        self.__statut = statut

    def get_description(self):
        return self.__description


class ListeDeTaches:
    def __init__(self):
        self.__taches = []

    def ajouterTache(self, tache):
        self.__taches.append(tache)

    def supprimerTache(self, tache):
        self.__taches.remove(tache)

    def marquerCommeFinie(self, tache):
        tache.set_statut("terminé")

    def afficherListe(self):
        for tache in self.__taches:
            print(f"Titre : {tache.get_titre()}, Statut : {tache.get_statut()}")

    def filterListe(self, statut):
        return [tache for tache in self.__taches if tache.get_statut() == statut]

    def afficherListe(self):
        for tache in self.__taches:
            print(f"Titre : {tache.get_titre()}, Statut : {tache.get_statut()}")


# Créer des instances de Tache
tache1 = Tache("Vaisselle", "Ne pas oublier de faire la vaisselle du matin en arrivant le soir.")
tache2 = Tache("Rdv coiffeur", "Appeler le coiffeur pour prendre rendez-vous demain matin.")

# Créer une instance de ListeDeTaches
liste = ListeDeTaches()

# Ajouter les tâches à la liste
liste.ajouterTache(tache1)
liste.ajouterTache(tache2)

# Marquer la première tâche comme terminée
liste.marquerCommeFinie(tache1)

# Afficher toutes les tâches
liste.afficherListe()

# Afficher les tâches à faire
print("Tâches à faire :")
for tache in liste.filterListe("à faire"):
    print(tache.get_description())
