def calcul_conso(puissance, total):
    duree = float(input("Combien de temps l'appareil a- t'il fonctionné?"))
    resultat = puissance * duree / 1000
    total += resultat
    print(f"votre appareil a consommé {resultat} KW/H. pour le moment le total de consommation est {total} KW/H")
    return total


total = 0

continuer = True

while continuer:
    reponse = input("Veuillez choisir un appareil ou quitter: PC = 1, TV = 2, Grille-pain = 3, Quitter = q").lower()
    if reponse == "1":
        total = calcul_conso(450, total)
    elif reponse == "2":
        total = calcul_conso(150, total)
    elif reponse == "2":
        total = calcul_conso(150, total)
    elif reponse == "q":
        continuer = False
    else:
        print("Appareil non répertorié")

print(f"Le total des consommations est {total} KW/H")
