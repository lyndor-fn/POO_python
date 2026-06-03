lsnote = []
for n in range(10):
    note = input('saisir la note : ')
    if note.isdigit():
        note = float(note)
        lsnote.append(note)

    else:
        print("veuillez saisir une valeur numerique")
print(lsnote)