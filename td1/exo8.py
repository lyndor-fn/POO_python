somme = 0
nb_valides = 0

for i in range(10):
    n = int(input("Saisissez un nombre positif : "))

    if n <= 0:
        break
    if n > 100:
        continue

    somme += n
    nb_valides += 1

if nb_valides == 10:
    print("Somme =", somme)
else:
    print(f"echec : seulement {nb_valides} nombres valides")