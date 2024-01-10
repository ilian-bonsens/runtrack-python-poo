class Student:
    def __init__(self, nom, prenom, numero, credits=0):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero = numero
        self.__credits = credits
        self.__level = self.__studentEval()

    def add_credits(self, credits):
        if isinstance(credits, int) and credits > 0:
            self.__credits += credits
            self.__level = self.__studentEval()
        else:
            print("Erreur: le nombre de crédits doit être un entier positif.")

    def __studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def studentInfo(self):
        print("Nom: ", self.__nom)
        print("Prénom: ", self.__prenom)
        print("Numéro d'étudiant: ", self.__numero)
        print("Niveau: ", self.__level)

etudiant1 = Student("John", "Doe", 145)
etudiant1.add_credits(10)
etudiant1.add_credits(10)
etudiant1.add_credits(10)
etudiant1.studentInfo()
