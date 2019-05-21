import requests
import mysql
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="********",
  database="appli"
)
mycursor = mydb.cursor()

CATEGORIES = ['Sandwichs',
              'Conserves',
              'Viandes',
              'Poissons',
              'Snacks']

GRADES = ['a','e']

def valid_product(keys, all_products):
    for key in keys:
        if key not in all_products:
            return False
    return True

all_products = []
api = 'https://fr.openfoodfacts.org/cgi/search.pl'
for category in CATEGORIES:
    for grade in GRADES:
        config = {
            'action': 'process',
            'tagtype_0': 'categories',
            'tag_contains_0': 'contains',
            'tag_0': category,
            'tagtype_1': 'nutrition_grade_fr',
            'tag_contains_1': 'contains',
            'tag_1': grade,
            'sort_by': 'categories',
            'page_size': 3,
            'json': 1
                    }
        response = requests.get(api, params=config)
        results = response.json()
        all_products.extend(results['products'])


selected_products = []
keys = ('code', 'product_name',
        'categories', 'url', 'nutrition_grade_fr', 'stores', 'generic_name_fr')
for product in all_products:
    if valid_product(keys, product) == True:
        categorie = product['categories']
        stores = product['stores']
        barcode = product['code']
        nom = product['product_name']
        url = product['url']
        nutrition_grade = product['nutrition_grade_fr']  
        description = product['generic_name_fr']       
        key = (barcode, stores, nom, url, nutrition_grade, categorie, description)
        selected_products.append(key)

#print(selected_products)

#Pour trier les catégories et garder que les intitulés qui nous intéressent
sorted_date =[]                
for produit in selected_products:
    liste = list(produit) #transformation du tuple d'un produit en liste
    categories_sous_forme_de_liste = liste[5].split(",") #transformation des categories sous forme de liste
    categories_propre =[] # Variables vide qui va contenir la liste des categories sans espaces
    good_category =[] #Variable vide qui va contenir les categories que l'on veut et qui sont présentes
    for categorie in categories_sous_forme_de_liste:
        sans_espace = categorie.strip()
        categories_propre.append(sans_espace)
        for nom in categories_propre:
            if nom in CATEGORIES:
                if nom not in good_category:
                    good_category.append(nom)
        liste[5] = good_category
    sorted_date.append(liste)

final_format = []

for produit in sorted_date:
    produit[5] = ", ".join(produit[5])
    produit_bon_format = tuple(produit)
    final_format.append(produit_bon_format)

#Récupérer toutes les categories pour eviter les doublons
all_category = []
for product in final_format:
    categorie = product[5]
    bon_format = categorie.split(",")
    for nom in bon_format:
        bon_nom = nom.strip()
        if bon_nom not in all_category and bon_nom != '' :
            all_category.append(bon_nom)

# Pour remplir la table catégorie
for category in all_category:
    sql_insert_query = """INSERT INTO Category (category_name) VALUES (%s)"""
    mycursor.execute(sql_insert_query, (category,))

#Récupérer tous les magasins pour éviter les doublons
all_store = []
for product in final_format:
   store = product[1]
   bon_format = store.split(",")
   for magasin in bon_format:
      sans_espace_minuscule = magasin.lower().strip()
      if sans_espace_minuscule not in all_store and sans_espace_minuscule != '':
          all_store.append(sans_espace_minuscule)

# Pour remplir la table Store 
for store in all_store:
    sql_insert_query = """ INSERT INTO Store (store_name) VALUES (%s)"""
    mycursor.execute(sql_insert_query, (store,))

#Fonction pour enlever les espaces
def bon_format(liste):
    toutes_cat = []
    for nom in liste:
        bon_nom = nom.strip()
        if bon_nom != '':
            toutes_cat.append(bon_nom)
    return toutes_cat

#Test pour intégrer les produits et remplir la tbale 'category product'
# La table 'categorie' doit déja etre remplie
for product in final_format:
    code = product[0]
    name = product[2]
    grade = product[4]
    url = product[3]
    description = product[6]
    cat = product[5].split(",")
    categories = bon_format(cat)
    sto = product[1].split(",")
    stores = bon_format(sto)
    sql_insert_query = """INSERT INTO Product (code, product_name_fr, nutrition_grade_fr, url, generic_name_fr) VALUES (%s, %s, %s, %s, %s)"""
    mycursor.execute(sql_insert_query, (code, name, grade, url, description))
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

mydb.commit()
