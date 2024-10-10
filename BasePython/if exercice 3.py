import random

na = random.randint(0, 10)

continuer = True
while(continuer):
    nu = int(input("Faites un essai: "))
    if nu == na:
        print("vous avez gagné")
# O:-)
        continuer = False
    else:
        if nu > na:
            print("le chiffre est plus petit")
        else:
            print("le chiffre est plus grand")