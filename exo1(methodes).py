class Point3D:
    # Attributs de classe
    Npts = 0
    Mx = 0
    My = 0
    Mz = 0

    def __init__(self, x, y, z):
        # Attributs d'instance privés
        self.__x = x
        self.__y = y
        self.__z = z

        # Mise à jour du compteur d'objets
        Point3D.Npts += 1

        # Mise à jour des maxima
        if x > Point3D.Mx:
            Point3D.Mx = x
        if y > Point3D.My:
            Point3D.My = y
        if z > Point3D.Mz:
            Point3D.Mz = z

    # Méthodes d'accès aux coordonnées
    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getZ(self):
        return self.__z

    # Méthodes de classe pour les statistiques
    @classmethod
    def getNpts(cls):
        return cls.Npts

    @classmethod
    def getMaxX(cls):
        return cls.Mx

    @classmethod
    def getMaxY(cls):
        return cls.My

    @classmethod
    def getMaxZ(cls):
        return cls.Mz

    # Représentation de l'objet
    def __repr__(self):
        return f"Point3D(x={self.__x}, y={self.__y}, z={self.__z})"
