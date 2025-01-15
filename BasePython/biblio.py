
def menu():
    print("Ajouter un livre: 1")
    print("Louer un livre: 2")
    print("Rendre un livre: 3")
    print("Affichez les livres disponibles: 4")
    print("Quitter: q")
    return input("Veuillez entrer un choix:")

def trouverLivre(id):
    for livre in livres:
        if id == livre["id"]:
            return livre

livres = []
reponse = menu()
lastId = 1

while reponse != "q":
    if reponse == "1":
        titre = input("Entrez le titre")
        auteur = input("Entrez le nom de l'auteur")
        annee = input("Entrez l'année")
        livres.append({"id": lastId, "titre": titre, "auteur": auteur, "annee": annee, "louable": True})
        lastId += 1

    elif reponse == "2":
        livreId = int(input("entrez l'id d'un livre à louer"))
        livre = trouverLivre(livreId)
        if livre["louable"]:
            livre["louable"] = False
            print(f"Le livre {livre["titre"]} vient d'être loué")
        else:
            print("livre non louable")

    elif reponse == "3":
        livreId = int(input("entrez l'id d'un livre à louer"))
        livre = trouverLivre(livreId)
        if not livre["louable"]:
            livre["louable"] = True
            titre = livre["titre"]
            print(f"Le livre {titre} vient d'être rendu")
        else:
            print("livre non loué")
    else:
        for livre in livres:
            if livre["louable"]:
                print(f"ID : {livre["id"]}, titre : {livre["titre"]}")

    reponse = menu()

print("Bonne journée")
