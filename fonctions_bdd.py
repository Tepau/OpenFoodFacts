import mysql
import mysql.connector
import random
from datetime import datetime
now = datetime.now()
from fonctions import gerer_erreur_saisie
from constantes import QUESTION_CHOIX_PRODUIT

mydb = mysql.connector.connect(
  host="******",
  user="******",
  password="******",
  database="******"
)
mycursor = mydb.cursor()

def insert_product(liste_products):
    for product in liste_products:
        code = product[0]
        name = product[2]
        grade = product[4]
        url = product[3]
        description = product[6]
        sql_insert_query = """INSERT INTO Product (code, product_name_fr, nutrition_grade_fr, url, generic_name_fr) VALUES (%s, %s, %s, %s, %s)"""
        mycursor.execute(sql_insert_query, (code, name, grade, url, description))

def insert_category_and_store_product(liste_products, index_categorie, index_store):
    for product in liste_products:
        code = product[0]
        cat = product[index_categorie].split(",")
        categories = bon_format(cat)
        sto = product[index_store].split(",")
        stores = bon_format(sto)
        for categorie in categories:
            sql_insert_query3 =  """SELECT id FROM Category WHERE category_name =%s """
            mycursor.execute(sql_insert_query3, (categorie,))
            nb_categories = mycursor.fetchall()
            result = nb_categories[0][0]
            sql_insert_query2 = """INSERT INTO Category_product (product_id, category_id) VALUES (%s, %s)"""
            mycursor.execute(sql_insert_query2, (code, result))
            for store in stores:
                sql_insert_query3 =  """SELECT id FROM Store WHERE store_name =%s """
                mycursor.execute(sql_insert_query3, (store,))
                nb_stores = mycursor.fetchall()
                result = nb_stores[0][0]
                sql_insert_query2 = """INSERT INTO Store_product (product_id, store_id) VALUES (%s, %s)"""
                mycursor.execute(sql_insert_query2, (code, result))


def insert_store(liste_stores):
    for store in liste_stores:
        sql_insert_query = """ INSERT INTO Store (store_name) VALUES (%s)"""
        mycursor.execute(sql_insert_query, (store,))


def insert_category(liste_categories):
    for category in liste_categories:
        sql_insert_query = """INSERT INTO Category (category_name) VALUES (%s)"""
        mycursor.execute(sql_insert_query, (category,))

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
    choix_final_2 = gerer_erreur_saisie(1, x-1, QUESTION_CHOIX_PRODUIT)

    if choix_final_2 > 0 and choix_final_2 < x:
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

def no_doublons_good_format(liste_selection, liste_produits, index):
    for product in liste_produits:
        selection = product[index]
        bon_format = selection.split(",")
        for nom in bon_format:
            bon_nom = nom.lower().strip()
            if bon_nom not in liste_selection and bon_nom != '':
                liste_selection.append(bon_nom)
    return liste_selection

def bon_format(liste):
    toutes_cat = []
    for nom in liste:
        bon_nom = nom.strip()
        if bon_nom != '':
            toutes_cat.append(bon_nom)
    return toutes_cat
    ******