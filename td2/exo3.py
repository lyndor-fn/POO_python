#Q11
def sous_liste_somme(liste, cible):
    for i in range(len(liste)):
        s = 0
        for j in range(i, len(liste)):
            s += liste[j]
            if s == cible:
                return liste[i:j+1]
    return []
#Q12
def evaluer_expression_sans_eval():
    return 3.5 + 4 * 2 - 6.5
#Q13
def groupes_anagrammes(liste_mots):
    groupes = {}
    for mot in liste_mots:
        cle = ''.join(sorted(mot))
        if cle not in groupes:
            groupes[cle] = []
        groupes[cle].append(mot)
    return list(groupes.values())
#Q14
import datetime

def prochain_anniversaire(liste_dates):
    aujourd = datetime.date.today()
    min_jours = 9999
    nom_proche = ""

    for nom, date in liste_dates:
        j, m = map(int, date.split("/"))
        anniv = datetime.date(aujourd.year, m, j)
        if anniv < aujourd:
            anniv = datetime.date(aujourd.year + 1, m, j)

        jours = (anniv - aujourd).days
        if jours < min_jours:
            min_jours = jours
            nom_proche = nom

    return nom_proche, min_jours
#Q15
def mega_soiree(invites_depart, nouveaux_arrivants, notes, seuil=10, max_personnes=15, taille_table=4):
    presents = []
    for x in invites_depart + nouveaux_arrivants:
        if x not in presents:
            presents.append(x)

    refuses = []
    acceptes = []

    for i in range(len(presents)):
        if notes[i] < seuil:
            refuses.append(presents[i])
        else:
            acceptes.append(presents[i])

    print("Invités présents (sans doublons) :", presents)
    print("Invités refusés (note trop basse) :", refuses)
    print("Liste triée alphabétique :", sorted(acceptes))
    print("Liste triée par niveau de fête :", sorted(acceptes, key=lambda x: notes[presents.index(x)], reverse=True))

    print("Tables :")
    for i in range(0, len(acceptes), taille_table):
        print("Table :", ", ".join(acceptes[i:i+taille_table]))

    print("Nombre total accepté :", len(acceptes))

    s = 0
    for x in acceptes:
        s += notes[presents.index(x)]
    print("Moyenne des notes acceptées :", round(s / len(acceptes), 2))

    meilleur = acceptes[0]
    for x in acceptes:
        if notes[presents.index(x)] > notes[presents.index(meilleur)]:
            meilleur = x

    print("Meilleur fêtard :", meilleur)

    if len(acceptes) >= max_personnes:
        print("Trop de monde ! La soirée est complète.")
    else:
        print("Il reste de la place.")
