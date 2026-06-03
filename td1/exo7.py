for i in range(1, 101):
    if i % 2 == 0:
        continue
    if i % 7 == 0:
        continue
    somme = 0
    for j in str(i):
        somme +=int(j)
    if somme % 2 == 0:
        continue
    print (i)
