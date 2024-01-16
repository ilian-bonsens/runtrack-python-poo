class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print(self.age)

    def bonjour(self):
        print('Hello')

    def modifierAge(self, age):
        self.age = age


class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print(f"J'ai {self.age} ans")


class Professeur(Personne):
    def __init__(self, age, matiereEnseignee):
        super().__init__(age)
        self.__matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")

eleve = Eleve()


eleve.modifierAge(15)
professeur = Professeur(40, 'Mathématiques')

eleve.bonjour()
eleve.allerEnCours()
professeur.bonjour()
professeur.enseigner()
