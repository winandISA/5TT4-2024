def calculAire(val1, val2):
    return val1 * val2

def printResultat(resultat):
    print(f"l'aire est égale à {resultat}")

continuer = True
while continuer:
    aireACalculer = input("Quelle aire voulez vous calculer? Carré(c), Rectangle (r), Parallélogramme (p), Triangle (t) ou quitter (q): ").lower()

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
    elif aireACalculer == "q":
        print("Fin de programme")
        continuer = False
    else:
        print("Valeur non acceptée")
