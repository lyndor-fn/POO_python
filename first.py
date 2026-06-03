def bulletin_classe(resultats):
    eleve = {}
    for nom, matiere, note in resultats:
        if nom not in eleve:
            eleve[nom] = {}
        if matiere not in eleve[nom]:
            eleve[nom][matiere] = []
        eleve[nom][matiere].append(note)
    bulletin = {}
    for nom, matieres in eleve.items():
        moyennes_matieres = {matiere: sum(notes) / len(notes) for matiere, notes in matieres.items()}
        total_notes = sum(sum(notes) for notes in matieres.values())
        nombre_matieres = len(matieres)
        moyenne_generale = total_notes / nombre_matieres if nombre_matieres > 0 else 0
        bulletin[nom] = {
            "moyennes_matieres": moyennes_matieres,
            "moyenne_generale": moyenne_generale,
            "nombre_matieres": nombre_matieres
        }
    # Créer la liste triée avec rangs
    liste_triee = [(nom, bulletin[nom]["moyenne_generale"]) for nom in bulletin]
    liste_triee.sort(key=lambda x: x[1], reverse=True)
    liste_triee = [(nom, moy, rang) for rang, (nom, moy) in enumerate(liste_triee, 1)]
    return bulletin, liste_triee

# Test
resultats = [
    ("Awa", "Maths", 17),
    ("Moussa", "Français", 13),
    ("Awa", "Français", 16),
    ("Fatou", "Maths", 11),
    ("Moussa", "Maths", 14),
    ("Awa", "Histoire", 15),
    ("Fatou", "Français", 12),
    ("Moussa", "Histoire", 9),
]

bulletin, liste = bulletin_classe(resultats)
print(bulletin)
print(liste)