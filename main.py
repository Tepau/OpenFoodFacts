import mysql
import mysql.connector
import random
from datetime import datetime
now = datetime.now()

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="tEPAU1992",
  database="appli"
)
mycursor = mydb.cursor()

liste_sauvegarde = []

def afficher_substitut(categorie):

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
    choix_2 = int(input("Tapez le numéro associé au produit que vous voulez substituer : "))
    code_pdt_substitue = myresult[choix_2 - 1][1]
    liste_sauvegarde.append(code_pdt_substitue)
    if choix_2 < x:
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
        liste_sauvegarde.append(code_pdt_de_substitution)
        print('Pour remplacer ce produit, nous vous proposons : ', aleatoire[0], '\n',
            'La description de ce produit est : ', aleatoire[2], '\n',
            'Il est disponible dans le(s) magasin(s) suivant(s) : ', aleatoire[3], '\n',
            'Son url est la suivante : ', aleatoire[1])


choix_utilisateur = True

while choix_utilisateur == True : 
    choix = int(input("Coisir une catégorie : " '\n'
                 "1 = Fromages" '\n'
                 "2 = Conserves" '\n'
                 "3 = Viandes" '\n'
                 "4 = Produits à tartiner" '\n'
                 "5 = Desserts" '\n'
                 "ici  : " ))

    if choix == 1:
        afficher_substitut('Fromages')
    elif choix == 2:
        afficher_substitut('Conserves')  
    elif choix == 3:
        afficher_substitut('Viandes')
    elif choix == 4:
        afficher_substitut('Produits à tartiner')
    elif choix == 5:
        afficher_substitut('Desserts')

    choix_utilisateur2 = int(input("Voulez pouvez désormais :" '\n'
     "Effectuer une nouvelle recheche : 1" '\n'
     "Sauvegarder votre recherche : 2" '\n'
     "Quitter l'application : 3" '\n'
     "A vous de choisir :  "))

    if choix_utilisateur2 == 1:
        choix_utilisateur = True

    if choix_utilisateur2 == 2:
        sql_insert_query = """ INSERT INTO Favorite (product_id, substitute_id, date_heure) VALUES (%s, %s, %s)"""
        mycursor.execute(sql_insert_query, (liste_sauvegarde[0], liste_sauvegarde[1], now))
        mydb.commit()
        liste_sauvegarde = []
        choix_final = int(input("Vous souhaitez : " '\n'
                                "Effectuer une nouvelle recherche : 1" '\n'
                                "Quitter le programme : 2" '\n'
                                "ici  : "))
        if choix_final == 1:
            choix_utilisateur = True
        elif choix_final == 2:
            choix_utilisateur = False

    if choix_utilisateur2 == 3:
        choix_utilisateur = False
        print("Au revoir ! ")
