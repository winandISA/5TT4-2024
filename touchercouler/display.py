def menu():
    print("""Sélectionnez une option:
    1. Nouveau jeu
    2. Charger jeu
    3. Règles du jeu
    4. Quitter""")
    return input("Votre choix? ")

def regleGlobal():
    print("Le jeu est en 2 parties")
    reglePosition()
    regleTir()

def reglePosition():
    print("On place des bateaux")

def regleTir():
    print("On tire sur des bateaux")