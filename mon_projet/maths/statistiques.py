from .operations import addition

def moyenne (liste):
    return sum(liste)/len(liste)
def maximum (liste):
    return max(liste)
def minimum (liste):
    return min(liste)

def somme_des_carres (liste):
    total = 0
    for x in liste:
        """Calcule la somme des carrés des éléments d'une liste en utilisant addition."""
        total = addition(total,x ** 2)
    return total


