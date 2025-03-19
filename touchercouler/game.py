bateaux = {"Porte avions": 5,
           "Cuirassé": 4,
           "Sous-marin": 3,
           "Torpilleur": 3,
           "": 2}

print("coucocu")
def creerGrille():
        return [["  ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
            [" 1", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
            [" 2", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
            [" 3", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
            [" 4", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
            [" 5", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
            [" 6", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
            [" 7", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
            [" 8", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
            [" 9", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~"],
            ["10", "~", "~", "~", "~", "~", "~", "~", "~", "~", "~"]
            ]

def afficherGrille(grille):
        for ligne in grille:
                display = ""
                for col in ligne:
                        display += col + " "
                print(display)


def creerJoueur():
        grille = creerGrille()
        for nom, longueur in bateaux:
                libre = False
                while not libre:
                        colonne = input("Colonne: ")
                        ligne = input("Ligne: ")
                        orientation = input("Orientation (h ou v): ")
                        try:
                                ligne = int(ligne)
                                if colonne in grille[0]:
                                        colonne = grille[ligne].index(colonne)
                                        if orientation == "h":

                                        elif orientation == "v":


                        finally:
                                if not libre:
                                        print("valeur invalide ou chevauchement")



def creerJeu():
