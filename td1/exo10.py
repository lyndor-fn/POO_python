chaine = 'ABCDEFGHIJ'

for i in range(len(chaine)):
    if i < len(chaine) // 2:     # i < 5
        print(chaine[i : i + (i + 1)])
    else:
        print(chaine[i : len(chaine)])
