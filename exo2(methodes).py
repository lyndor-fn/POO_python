class Rectangle:
    # Attributs de classe
    Nrect = 0
    MaxSurface = float('-inf')

    def __init__(self, largeur, hauteur):
        # Attributs d'instance privés
        self.__largeur = largeur
        self.__hauteur = hauteur

        # Mise à jour du compteur
        Rectangle.Nrect += 1

        # Calcul de la surface
        surface = self.surface()

        # Mise à jour de la plus grande surface
        if surface > Rectangle.MaxSurface:
            Rectangle.MaxSurface = surface

    # Méthodes d'accès
    def getLargeur(self):
        return self.__largeur

    def getHauteur(self):
        return self.__hauteur

    def surface(self):
        return self.__largeur * self.__hauteur

    # Méthodes de classe
    @classmethod
    def getNrect(cls):
        return cls.Nrect

    @classmethod
    def getMaxSurface(cls):
        return cls.MaxSurface

    # Méthodes spéciales
    def __repr__(self):
        return f"Rectangle({self.__largeur}, {self.__hauteur})"

    def __str__(self):
        return f"Rectangle: largeur={self.__largeur}, hauteur={self.__hauteur}, surface={self.surface()}"

    # Méthode statique
    @staticmethod
    def plusGrand(r1, r2):
        return r1 if r1.surface() >= r2.surface() else r2
