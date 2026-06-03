#Q6
def est_premier(liste):
    premier = []
    for entier in liste:
        cpt = 0
        for k in range(1, entier + 1):
            if entier % k == 0:
                cpt += 1
        if cpt == 2:
            premier.append(entier)
    return premier

def filtrer_premiers(liste):
    res = []
    for x in liste:
        if est_premier(x):
            res.append(x)
    return res
#Q7
import datetime

def prochain_lundi():
    d = datetime.date.today()
    while d.weekday() != 0:
        d += datetime.timedelta(days=1)
    return d.strftime("%d/%m/%Y")
#Q7-2
import datetime

def prochain_lundi():
    aujourd = datetime.date.today()
    jour = aujourd.weekday()

    if jour == 0:
        return aujourd.strftime("%d/%m/%Y")
    else:
        prochain = aujourd + datetime.timedelta(days=7 - jour)
        return str(prochain.day) + "/" + str(prochain.month) + "/" + str(prochain.year)


#Q8
import string

def est_palindrome_phrase(phrase):
    p = ""
    for c in phrase.lower():
        if c.isalpha():
            p += c
    return p == p[::-1]
#Q9
def cesar_rotatif(texte,decalage_initial):
    rest=""
    decalage = decalage_initial
    for c in texte:
        if'a' <= c <= 'z':
            pos=ord(c) - ord('a')
            nouvelle_pos=(pos+decalage) % 26
            resultat += chr(nouvelle_pos + ord('a'))' '
            decalage += 1
        elif 'A' <= c <= 'Z':
            pos=ord(c) - ord('A')
            nouvelle_pos=(pos+decalage) % 26
            rest += chr(nouvelle_pos + ord('A'))
            decalage += 1
        else:
            resultat += c
    return resultat
#Q9-2
def cesar_rotatif(texte, decalage_initial):
    alphabet_min = "abcdefghijklmnopqrstuvwxyz"
    alphabet_maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    resultat = ""
    decalage = decalage_initial

    for c in texte:
        if c in alphabet_min:
            i = 0
            while alphabet_min[i] != c:
                i += 1
            resultat += alphabet_min[(i + decalage) % 26]
            decalage += 1

        elif c in alphabet_maj:
            i = 0
            while alphabet_maj[i] != c:
                i += 1
            resultat += alphabet_maj[(i + decalage) % 26]
            decalage += 1

        else:
            resultat += c

    return resultat
#Q10
def moyenne_glissante(liste, fenetre):
    res = []
    for i in range(len(liste)):
        debut = max(0, i - fenetre + 1)
        s = 0
        for j in range(debut, i + 1):
            s += liste[j]
        res.append(s / (i - debut + 1))
    return res
