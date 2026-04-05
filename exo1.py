from math import sqrt

class Point3d :
    def __init__(self,x,y,z) :
        self.x = x
        self.y = y
        self.z = z

    def afficher(self) :
        print(self.x,self.y,self.z)

    def deplacer(self,dx,dy,dz) :
        self.x += dx
        self.y += dy
        self.z += dz
        print(self.x,self.y,self.z)

    def distance(self,x,y,z):
        d = sqrt ((self.x - x) ** 2 + (self.y - y) ** 2 + (self.z - z) ** 2)
        return d

a3d = Point3d(1,2,3)
b3d = Point3d(4,5,6)
a3d.afficher()
b3d.afficher()
a3d.deplacer(1,2,3)
b3d.deplacer(4,5,6)
a3d.afficher()
b3d.afficher()
d = a3d.distance(b3d.x,b3d.y,b3d.z)
print(d)