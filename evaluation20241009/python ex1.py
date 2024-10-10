def calculAire(val1, val2):
    return val1 * val2

def printResultat(resultat):
    print(f"l'aire est égale à {resultat}")

aireACalculer = input("Quelle aire voulez vous calculer? Carré(c), Rectangle (r), Parallélogramme (p) ou Triangle (t): ").lower()

if aireACalculer == "c":
    cote = int(input("Veuillez entrer la valeur d'un coté: "))
    resultat = calculAire(cote, cote)
    printResultat(resultat)
elif aireACalculer == "r":
    largeur = int(input("Veuillez entrer la valeur de la largeur: "))
    longueur = int(input("Veuillez entrer la valeur de la longueur: "))
    resultat = calculAire(longueur, largeur)
    printResultat(resultat)
elif aireACalculer == "p" or aireACalculer == "t":
    base = int(input("Veuillez entrer la valeur de la base: "))
    hauteur = int(input("Veuillez entrer la valeur de la hauteur: "))
    resultat = calculAire(base, hauteur)
    if aireACalculer == "t":
        resultat /= 2
    printResultat(resultat)
else:
    print("Valeur non acceptée")
