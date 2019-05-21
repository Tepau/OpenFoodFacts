import mysql
import mysql.connector
import random
from datetime import datetime
now = datetime.now()

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="********",
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
    choix_2 = 0
    while choix_2 < 1 or choix_2 >= x:
        choix_2 = input("Tapez le numéro associé au produit que vous voulez substituer : ")

        try:
            choix_2 = int(choix_2)
        except ValueError:
            print('Vous devez saisir un chiffre')
            choix_2 = 0
            continue
        if choix_2 < 1 or choix_2 >= x:
            print('Vous devez saisir un chiffre en 1 et ', x)
            continue

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

nom = input("Entrez votre pseudo: ")
nom_good_format = nom.lower()

boucle_principale = True

while boucle_principale:

        choix_1 = 0
        while choix_1 < 1 or choix_1 > 3:
            choix_1 = input("Que souhaitez vous faire?" '\n'
                            "1 : Rechercher un produit" '\n'
                            "2 : Consulter votre historique" '\n'
                            "3 : Quitter l'application" '\n'
                            " :  ")
            try:
                choix_1 = int(choix_1) 
            except ValueError:
                print('Vous devez saisir un chiffre')
                choix_1 = 0
                continue
            if choix_1 < 1 or choix_1 > 3:
                print('Le chiffre doit être compris en 1 et 3')

            if choix_1 == 1:

                choix_categorie = 0
                while choix_categorie < 1 or choix_categorie > 5:
                    choix_categorie = input("Choisir une catégorie : " '\n'
                                "1 = Sandwichs" '\n'
                                "2 = Conserves" '\n'
                                "3 = Viandes" '\n'
                                "4 = Poissons" '\n'
                                "5 = Snacks" '\n'
                                "ici  : ")

                    try:
                       choix_categorie = int(choix_categorie)
                    except ValueError:
                        print('Vous devez saisir un chiffre')
                        choix_categorie = 0
                        continue
                    if choix_categorie < 1 or choix_categorie > 5:
                        print('Le chiffre doit être compris entre 1 et 5')
                        continue


                    if choix_categorie == 1:
                        afficher_substitut('Sandwichs')
                    elif choix_categorie == 2:
                        afficher_substitut('Conserves')  
                    elif choix_categorie == 3:
                        afficher_substitut('Viandes')
                    elif choix_categorie == 4:
                        afficher_substitut('Poissons')
                    elif choix_categorie == 5:
                        afficher_substitut('Snacks')

                    choix_fin_de_recherche = 0
                    while choix_fin_de_recherche < 1 or choix_fin_de_recherche > 3:
                        choix_fin_de_recherche = input("Voulez pouvez désormais :" '\n'
                        "Revenir au Menu Principal : 1" '\n'
                        "Sauvegarder votre recherche : 2" '\n'
                        "Quitter l'application : 3" '\n'
                        "A vous de choisir :  ")

                        try:
                            choix_fin_de_recherche = int(choix_fin_de_recherche)
                        except ValueError:
                            print('Vous devez saisir un chiffre')
                            choix_fin_de_recherche = 0
                            continue
                        if choix_fin_de_recherche < 1 or choix_fin_de_recherche > 3:
                            print('Vous devez saisir un chiffre entre 1 et 3')
                            continue

                        if choix_fin_de_recherche == 1:
                            boucle_principale == True

                        if choix_fin_de_recherche == 2:
                            sql_insert_query = """ INSERT INTO Favorite (product_id, substitute_id, date_heure, pseudo) VALUES (%s, %s, %s, %s)"""
                            mycursor.execute(sql_insert_query, (liste_sauvegarde[0], liste_sauvegarde[1], now, nom_good_format))
                            print('Votre recherche est bien enregistrée')
                            mydb.commit()
                            liste_sauvegarde = []
                            choix_final = 0
                            while choix_final < 1 or choix_final > 2:
                                choix_final = input("Vous souhaitez : " '\n'
                                                        "Revenir au Menu Principal : 1" '\n'
                                                        "Quitter le programme : 2" '\n'
                                                        "ici  : ")
                                try:
                                    choix_final = int(choix_final)
                                except ValueError:
                                    print('Vous devez saisir un chiffre')
                                    choix_final = 0
                                    continue
                                if choix_final < 1 or choix_final > 2:
                                    print('Vous devez saisir un chiffre entre 1 et 2')
                                    continue


                                if choix_final == 1:
                                    boucle_principale = True
                                elif choix_final == 2:
                                    print("Au revoir ! ")
                                    boucle_principale = False

                        if choix_fin_de_recherche == 3:
                            print('Bye Bye')
                            boucle_principale = False

            if choix_1 == 2:
                mycursor.execute(""" SELECT product_id, substitute_id FROM Favorite WHERE pseudo = %s""", (nom_good_format,))
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

                choix_final = 0
                while choix_final < 1 or choix_final > 2:
                    choix_final = input("Vous souhaitez : " '\n'
                                    "Revenir au Menu Principal : 1" '\n'
                                    "Quitter le programme : 2" '\n'
                                    "ici  : ")

                    try:
                        choix_final = int(choix_final)
                    except ValueError:
                        print('Vous devez saisir un chiffre')
                        choix_final = 0
                        continue
                    if choix_final < 1 or choix_final > 2:
                        print('Vous devez saisir un chiffre entre 1 et 2')

                    if choix_final == 1:
                        boucle_principale = True
                    elif choix_final == 2:
                        print("Bye Bye")
                        boucle_principale = False


            if choix_1 == 3:
                print('Bye bye')
                boucle_principale = False

