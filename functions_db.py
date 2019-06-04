import mysql
import mysql.connector
import random
from datetime import datetime
from functions import manage_typing_error
from constants import QUESTION_CHOICE_PRODUCT

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="tEPAU1992",
  database="appli",
  charset='utf8'
)
mycursor = mydb.cursor()

now = datetime.now()


def insert_product(liste_products):
    """Inserts the recovered products into the database"""

    for product in liste_products:
        code = product[0]
        name = product[2]
        grade = product[4]
        url = product[3]
        description = product[6]
        sql_insert_query = """INSERT INTO Product (code, product_name_fr, nutrition_grade_fr, url, generic_name_fr) VALUES (%s, %s, %s, %s, %s)"""
        mycursor.execute(sql_insert_query, (code, name, grade, url, description))


def insert_category_and_store_product(liste_products, category_index, store_index):
    """ Fill tables category_product and store_product"""

    for product in liste_products:
        code = product[0]
        cat = product[category_index].split(",")
        categories = valid_format(cat)
        sto = product[store_index].split(",")
        stores = valid_format(sto)
        for category in categories:
            sql_insert_query3 = """SELECT id FROM Category WHERE category_name =%s """
            mycursor.execute(sql_insert_query3, (category,))
            nb_categories = mycursor.fetchall()
            result = nb_categories[0][0]
            sql_insert_query2 = """INSERT INTO Category_product (product_id, category_id) VALUES (%s, %s)"""
            mycursor.execute(sql_insert_query2, (code, result))
            for store in stores:
                sql_insert_query3 = """SELECT id FROM Store WHERE store_name =%s """
                mycursor.execute(sql_insert_query3, (store,))
                nb_stores = mycursor.fetchall()
                result = nb_stores[0][0]
                sql_insert_query2 = """INSERT INTO Store_product (product_id, store_id) VALUES (%s, %s)"""
                mycursor.execute(sql_insert_query2, (code, result))


def insert_store(stores_list):
    """Inserts the recovered stores into the database"""

    for store in stores_list:
        sql_insert_query = """ INSERT INTO Store (store_name) VALUES (%s)"""
        mycursor.execute(sql_insert_query, (store,))


def insert_category(categories_list):
    """Inserts the recovered categories into the database"""

    for category in categories_list:
        sql_insert_query = """INSERT INTO Category (category_name) VALUES (%s)"""
        mycursor.execute(sql_insert_query, (category,))


def display_substitut(category, saved_list):

    mycursor.execute("""SELECT product_name_fr, code \
        FROM Product \
        INNER JOIN Category_product ON Product.code = Category_product.product_id \
        INNER JOIN Category ON Category.id = Category_product.category_id \
        WHERE category_name = %s AND nutrition_grade_fr = 'e' """, (category,))
    myresult = mycursor.fetchall()
    x = 1
    print("Voici la sélection de produits : ")
    for result in myresult:
        print(x, ':', result[0])
        x += 1
    final_choice = manage_typing_error(1, x-1, QUESTION_CHOICE_PRODUCT)

    if final_choice > 0 and final_choice < x:
        substituted_product_code = myresult[final_choice - 1][1]
        saved_list.append(substituted_product_code)

        if final_choice < x:
            mycursor.execute("""SELECT product_name_fr, url, generic_name_fr, store_name, code \
            FROM Product \
            INNER JOIN Category_product ON Product.code = Category_product.product_id \
            INNER JOIN Category ON Category.id = Category_product.category_id \
            INNER JOIN Store_product ON Product.code = Store_product.product_id \
            INNER JOIN Store ON Store.id = Store_product.store_id \
            WHERE category_name = %s AND nutrition_grade_fr = 'a' """, (category,))
            myresult = mycursor.fetchall()
            random_product = random.choice(myresult)
            substitution_product_code = random_product[4]
            saved_list.append(substitution_product_code)
            print('Pour remplacer ce produit, nous vous proposons : ', random_product[0], '\n',
                  'La description de ce produit est : ', random_product[2], '\n',
                  'Il est disponible dans le(s) magasin(s) suivant(s) : ', random_product[3], '\n',
                  'Son url est la suivante : ', random_product[1])


def save_product(saved_list, name_user):
    """ Save a research """

    sql_insert_query = """ INSERT INTO Favorite (product_id, substitute_id, date_heure, pseudo) VALUES (%s, %s, %s, %s) ON DUPLICATE KEY UPDATE product_id = %s, substitute_id = %s, date_heure = %s, pseudo = %s"""
    mycursor.execute(sql_insert_query, (saved_list[0], saved_list[1], now, name_user, saved_list[0], saved_list[1], now, name_user))
    print('Votre recherche est bien enregistrée')
    mydb.commit()
    saved_list = []


def display_saved_product(name_user):
    """Display a saved research """

    mycursor.execute(""" SELECT product_id, substitute_id FROM Favorite WHERE pseudo = %s""", (name_user,))
    result = mycursor.fetchall()
    for x in result:
        good_product = []
        bad_product = []
        y = x[0]
        z = x[1]
        good_product.append(y)
        bad_product.append(z)
        mycursor.execute(""" SELECT product_name_fr FROM Product WHERE code = %s """, (good_product[0],))
        result = mycursor.fetchall()
        mycursor.execute(""" SELECT product_name_fr FROM Product WHERE code = %s """, (bad_product[0],))
        result2 = mycursor.fetchall()
        print('Le produit : ', result[0][0], 'a été remplacé par le produit : ', result2[0][0])


def no_duplicates_good_format(selection_list, products_list, index):
    """Read a list that has several times the same data and creating a new list without duplicates """

    for product in products_list:
        selection = product[index]
        valid_format = selection.split(",")
        for name in valid_format:
            valid_name = name.lower().strip()
            if valid_name not in selection_list and valid_name != '':
                selection_list.append(valid_name)
    return selection_list


def valid_format(list_to_convert):
    """ Retrun a clean list, without spaces and empty names"""

    valid_list = []
    for name in list_to_convert:
        valid_name = name.strip()
        if valid_name != '':
            valid_list.append(valid_name)
    return valid_list
