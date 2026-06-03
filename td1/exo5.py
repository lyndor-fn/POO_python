mot = input("Saisissez un mot : ")

mot_min = mot.lower()

contient_a = "a" in mot_min
contient_python = "python" in mot_min

if contient_a:
    print("Contient un 'a' (insensible à la casse)")

if contient_python:
    print("Python détecté !")

if not contient_a and not contient_python:
    print("Rien de spécial")
