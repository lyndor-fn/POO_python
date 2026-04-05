class Produit :
    def __init__(self,nom,prix,description) :
        self.nom = nom
        self.prix = prix
        self.description = description

    def afficher(self) :
        print(self.nom)
        print(self.prix)
        print(self.description)

    def modifierPrix(self,nprix) :
        self.prix = nprix

    def modifierDescription(self,ndescription) :
        self.description = ndescription

    #objet :

produit1 = Produit("telephone",200000,"iphone")
produit1.afficher()
produit1.modifierPrix(150000)
produit1.modifierDescription("ipad")
produit1.afficher()