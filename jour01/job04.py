class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        print(f"Je suis {self.prenom} {self.nom}")

personne1 = Personne("Doe", "John")
personne1.SePresenter()
personne2 = Personne("Dupont", "Jean")
personne2.SePresenter()