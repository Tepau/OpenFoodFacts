import requests
from api_functions import *
from constants import CATEGORIES, GRADES

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

final_format = final_structure(selected_products)