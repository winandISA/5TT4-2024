import random

def isDead(niveau):
    if niveau == 0:
        print("Vous êtes mort dans la honte.")
        return False
    else:
        return True


def isWin(niveau):
    if niveau >= 10:
        print("VICTOIRE !!!!")
        return False
    else:
        return True


niveauJoueur = 3
argent = 0
potion = 1
fuite = 0
continuer = True
while continuer:
    print(f"Votre niveau est {niveauJoueur}, vous avez {argent} pieces d'or et {potion} potions")
    niveauMonstre = random.randint(1, 10)
    if input(f"Vous entrez dans la pièce suivante, un monstre de niveau {niveauMonstre} se dresse devant vous. Voulez-vous le combattre? o/n: ") == "o":
#Gestion des potions
        potionW = True
        forceJoueur = niveauJoueur
        while potionW:
            if potion > 0:
                if input(f"Voulez-vous utiliser une potion? il vous en reste {potion}. o/n: ") == "o":
                    potion -= 1
                    gain = random.randint(1, 3)
                    forceJoueur += gain
                    print(f"Vous gagnez {gain}, votre puissance actuelle est {forceJoueur}")
                else:
                    potionW = False
            else:
                potionW = False
#Gestion du combat
        if forceJoueur >= niveauMonstre:
            print("Vous passez le monstre par le fil de votre épée")
            argent += random.randint(10, 100)
            if random.randint(1, 3) == 1:
                potion += 1
            if niveauJoueur < niveauMonstre:
                niveauJoueur += 2
            else:
                niveauJoueur += 1
            continuer = isWin(niveauJoueur)
        else:
            print("Le monstre vous piétine sauvagement")
            niveauJoueur -= 1
            continuer = isDead(niveauJoueur)
    else:
#Gestion de la fuite
        print("Vous fuyez!!!")
        fuite += 1
#Punition si trop de fuites
        if fuite == 3:
            print("Vous avez fuis trop souvent, vous perdez 1 niveau pour votre couardise.")
            niveauJoueur -= 1
            continuer = isDead(niveauJoueur)
            fuite = 0
    print(" ")