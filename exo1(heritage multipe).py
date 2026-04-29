# Définition de la classe Animal
class Animal:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def se_deplacer(self):
        print(f"{self.nom} se déplace.")

# Définition de la classe Chien qui hérite de Animal
class Chien(Animal):
    def aboyer(self):
        print(f"{self.nom} aboie.")

# Instanciation d'un chien nommé Rex, âgné de 5 ans
rex = Chien("Rex", 5)

# Appel des méthodes
rex.se_deplacer()   # affiche "Rex se déplace."
rex.aboyer()        # affiche "Rex aboie."
