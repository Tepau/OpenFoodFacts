import random
import mysql
import mysql.connector
from datetime import datetime
now = datetime.now()

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="***",
  database="appli"
)
mycursor = mydb.cursor()

def afficher_substitut(categorie, liste_de_sauvegarde):

    mycursor.execute("""SELECT product_name_fr, code \
        FROM Product \
        INNER JOIN Category_product ON Product.code = Category_product.product_id \
        INNER JOIN Category ON Category.id = Category_product.category_id \
        WHERE category_name = %s AND nutrition_grade_fr = 'e' """, (categorie,))
    myresult = mycursor.fetchall()
    x = 1
    print("Voici la sélection de produits : ")
    for result in myresult:
        print(x, ':', result[0])
        x += 1
    choix_final_2 = 0
    while choix_final_2 < 1 or choix_final_2 >= x:
        choix_final_2 = input("Tapez le numéro associé au produit que vous voulez substituer : ")

        try:
            choix_final_2 = int(choix_final_2)
        except ValueError:
            print('Vous devez saisir un chiffre')
            choix_final_2 = 0
            continue
        if choix_final_2 < 1 or choix_final_2 >= x:
            print('Vous devez saisir un chiffre en 1 et ', x)
            continue

        code_pdt_substitue = myresult[choix_final_2 - 1][1]
        liste_de_sauvegarde.append(code_pdt_substitue)
        if choix_final_2 < x:
            mycursor.execute("""SELECT product_name_fr, url, generic_name_fr, store_name, code \
            FROM Product \
            INNER JOIN Category_product ON Product.code = Category_product.product_id \
            INNER JOIN Category ON Category.id = Category_product.category_id \
            INNER JOIN Store_product ON Product.code = Store_product.product_id \
            INNER JOIN Store ON Store.id = Store_product.store_id \
            WHERE category_name = %s AND nutrition_grade_fr = 'a' """, (categorie,))
            myresult = mycursor.fetchall() 
            aleatoire = random.choice(myresult)
            code_pdt_de_substitution = aleatoire[4]
            liste_de_sauvegarde.append(code_pdt_de_substitution)
            print('Pour remplacer ce produit, nous vous proposons : ', aleatoire[0], '\n',
                'La description de ce produit est : ', aleatoire[2], '\n',
                'Il est disponible dans le(s) magasin(s) suivant(s) : ', aleatoire[3], '\n',
                'Son url est la suivante : ', aleatoire[1])


def sauvegarder_pdt(liste_de_sauvegarde, name_user):
    sql_insert_query = """ INSERT INTO Favorite (product_id, substitute_id, date_heure, pseudo) VALUES (%s, %s, %s, %s) ON DUPLICATE KEY UPDATE product_id = %s, substitute_id = %s, date_heure = %s, pseudo = %s"""
    mycursor.execute(sql_insert_query, (liste_de_sauvegarde[0], liste_de_sauvegarde[1], now, name_user, liste_de_sauvegarde[0], liste_de_sauvegarde[1], now, name_user))
    print('Votre recherche est bien enregistrée')
    mydb.commit()
    liste_de_sauvegarde = []

def afficher_pdt_sauvegarde(name_user):
    mycursor.execute(""" SELECT product_id, substitute_id FROM Favorite WHERE pseudo = %s""", (name_user,))
    result = mycursor.fetchall()
    for x in result:
        good_pdt = []
        bad_pdt = []
        y = x[0]    
        z = x[1]
        good_pdt.append(y)
        bad_pdt.append(z)
        mycursor.execute(""" SELECT product_name_fr FROM Product WHERE code = %s """, (good_pdt[0],))
        result = mycursor.fetchall()
        mycursor.execute(""" SELECT product_name_fr FROM Product WHERE code = %s """, (bad_pdt[0],))
        result2 = mycursor.fetchall()
        print('Le produit : ', result[0][0], 'a été remplacé par le produit : ', result2[0][0])
