#Q1
def somme_pairs(liste):
    s = 0
    for x in liste:
        if x % 2 == 0:
            s += x
    return s
#Q2
def plus_long_mot(phrase):
    mots = phrase.split()
    long = mots[0]
    for m in mots:
        if len(m) > len(long):
            long = m
    return long
#Q3
def celsius_fahrenheit(temp):
    return temp * 9/5 + 32
#Q4
def compte_voyelles(texte):
    voyelles = "aeiouyAEIOUY"
    c = 0
    for ch in texte:
        if ch in voyelles:
            c += 1
    return c
#Q5
import datetime

def age_en_jours(annee, mois, jour):
    naissance = datetime.date(annee, mois, jour)
    aujourd_hui = datetime.date.today()
    return (aujourd_hui - naissance).days
