import mysql.connector

db_config = {
    'host': 'localhost',         # Adresse du serveur MySQL
    'user': 'root',              # Nom d'utilisateur
    'password': '',   # Mot de passe
    'database': 'ecole'    # Nom de la base de données
}

try:
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
# récuperer un id existant
    strSQL = "SELECT id_professeur from ex1_professeur WHERE nom = 'Tchana'"
    cursor.execute(strSQL)
    id_titulaire = cursor.fetchall()[0][0]

    print(id_titulaire)
# créer un professeur avec un nouvel ID
    strSQL = "INSERT INTO ex1_professeur (nom, prenom, DDN) VALUES (%s, %s, %s)"
    cursor.execute(strSQL, ["Moins", "Guy", "2000-03-01"])
# on ne spécifie pas le id_professeur parce que c'est un champs auto increment et que donc la DB va aller chercher
# automatiquement le prochain id. (le plus grand +1)
    id_prof = cursor.lastrowid
    print(id_prof)

# Mr Moins donne cours au 6tt4. il va donc falloir créer la classe
    strSQL = "INSERT INTO ex1_classe (OptionCl, nom, promotion, annee, id_professeur) VALUES (%s, %s, %s,%s, %s)"
    # On ne spécifie pas l'id_classe car il est auto increment mais IL FAUT préciser l'id_prof parce que c'est une clé étrangère.
    cursor.execute(strSQL, ["Informatique", "6TT4", "2024", "6", id_titulaire])
    id_classe = cursor.lastrowid
    print(id_classe)


# On va créer un cours d'informatique pour la 6TT4.
    strSQL = "INSERT INTO ex1_cours (Intitule, nb_heure, id_classe) VALUES (%s, %s, %s)"
    cursor.execute(strSQL, ["Informatique", "8", id_classe])
    id_cours = cursor.lastrowid
    print(id_cours)

# On assigne 2 heures à Mr Moins pour le cours d'info des 6TT4
    strSQL = "INSERT INTO ex1_tr_pro_cou (id_cours, id_professeur, nbHeure) VALUES (%s, %s, %s)"
    cursor.execute(strSQL, [id_cours, id_prof, 2])

    connection.commit()
except Exception as e:
    connection.rollback()
    print(e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
