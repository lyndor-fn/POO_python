print("Triangle simple :")
for i in range(1, 6):
    print('*' * i)

print("\nTriangle gauche (aligné à droite) :")
for i in range(1, 6):
    print(' ' * (5 - i) + '*' * i)

print("\nTriangle inversé :")
for i in range(5, 0, -1):
    print('*' * i)

print("\nPyramide fixe (5 lignes) :")
for i in range(1, 6):
    print(' ' * (5 - i) + '*' * (2 * i - 1))
print("\nPyramide personnalisée :")
N = int(input("Entrez le nombre de lignes de la pyramide : "))
for i in range(1, N + 1):
    print(' ' * (N - i) + '*' * (2 * i - 1))
