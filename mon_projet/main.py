from maths.operations import *
from maths.statistiques import *
from utils.string_utils import *
import requests

#operations
print(addition(7,9))
print(soustraction(7,9))
print(multiplication(7,9))

#statistiques
liste = [10,20,30,40,50]
print(moyenne(liste))
print(maximum(liste))
print(minimum(liste))

#chaine
chaine = "Bonjour tout le monde"
print(inverser_chaine(chaine))
print(compter_mots(chaine))

def tester_requete(url: str):
    """Teste une requête HTTP GET simple avec requests."""
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print("Requête réussie !")
            print("Contenu (premiers 300 caractères) :")
            print(response.text[:300])
        else:
            print(f"Erreur HTTP : {response.status_code}")
    except Exception as e:
        print(f"Erreur de connexion : {e}")

