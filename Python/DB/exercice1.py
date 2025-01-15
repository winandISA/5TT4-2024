import mysql.connector


db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'ecole'
}

try:
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    # version Beaucoup de SQL
    print("LISTE ELEVE SQL")
    strSQL = "SELECT e.* FROM Ex1_eleve e JOIN Ex1_tr_ele_cla tr ON e.id_eleve = tr.id_eleve JOIN Ex1_classe c ON tr.id_classe = c.id_classe WHERE c.nom = '5TT4'"
    cursor.execute(strSQL)
    eleves = cursor.fetchall()
    print(*(eleve for eleve in eleves), sep="\n")

    # version Beaucoup de Python
    print("LISTE ELEVE PYTHON")
    strSQL = "SELECT id_classe FROM Ex1_classe WHERE nom = '5TT4'"
    cursor.execute(strSQL)
    result = cursor.fetchall()

    strSQL = "SELECT id_eleve FROM Ex1_tr_ele_cla WHERE id_classe = %s"
    cursor.execute(strSQL, result[0])
    result = cursor.fetchall()

    for eleve in result:
        strSQL = "SELECT * FROM Ex1_eleve WHERE id_eleve = %s"
        cursor.execute(strSQL, eleve)
        result = cursor.fetchall()
        print(result)

    connection.commit()

except Exception as e:
    connection.rollback()
    print(e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()