# Classe Employe
class Employe:
    def __init__(self, nom):
        self.nom = nom

    def travailler(self):
        print(f"{self.nom} travaille.")

# Classe Instructeur
class Instructeur:
    def __init__(self, nom):
        self.nom = nom

    def enseigner(self):
        print(f"{self.nom} enseigne.")

# Classe Formateur qui hérite des deux
class Formateur(Employe, Instructeur):
    def __init__(self, nom):
        # On appelle le constructeur de Employe
        super().__init__(nom)

# Instanciation
samba = Formateur("Samba")

# Appels des méthodes
samba.travailler()
samba.enseigner()
