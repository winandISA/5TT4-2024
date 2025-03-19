from display import regleGlobal, menu

continuer = True
while continuer:
    choix = menu()
    if choix == 1:
        print()
    elif choix == 2:
        print()
    elif choix == 3:
        regleGlobal()
    elif choix == 4:
        if input("Etes vous sur de vouloir quitter (o/n)? ").lower() == "o":
            continuer = False
    else:
        print("Choix invalide")
