class Ville:
    def __init__(self, nom, habitants):
        self.__nom = nom
        self.__habitants = habitants

    def get_nom(self):
        return self.__nom

    def get_habitants(self):
        return self.__habitants

    def ajouter_habitant(self):
        self.__habitants += 1


class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        self.__ville.ajouter_habitant()


# Créer des objets Ville
paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)

# Afficher le nombre d'habitants de chaque ville
print(f"Population de la ville de Paris : {paris.get_habitants()}.")
print(f"Population de la ville de Marseille : {marseille.get_habitants()}.")

# Créer des objets Personne
john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

# Afficher le nombre d'habitants de chaque ville après l'arrivée des nouvelles personnes
print(f"Mise à jour de la population de Paris : {paris.get_habitants()}.")
print(f"Mise à jour de la population de Marseille : {marseille.get_habitants()}.")
