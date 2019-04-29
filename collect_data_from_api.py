import requests
from constantes import *

class CollectDataFromApi:

    def __init__(self):
      pass

    def select_products(self):
            
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
                    'page_size': 4,
                    'json': 1
                         }
                response = requests.get(api, params=config)
                results = response.json()
                all_products.extend(results['products'])

        return all_products



    def select_data(self, products):

      final_format = []
      keys = ('code', 'product_name', 'stores',
            'categories', 'url', 'nutrition_grade_fr')
      for product in products:
          if self.valid_product(keys, product):
              num_id = product['code']
              nom = product['product_name']
              store = product['stores']
              url = product['url']
              nutrition_grade = product['nutrition_grade_fr']
              key = (num_id, nom, store, url, nutrition_grade)
              final_format.append(key)

              print('Nom : ', nom, 'id :', num_id,
                    'Note nutritionelle: ', nutrition_grade, '.', '\n',
                    'Il est disponible dans', [len(store.split(None))], 'magasins : ', store, '\n',
                    'Url : ', url, '\n',
                    'Nous avons désormais récupéré', [len(final_format)], 'produits.')


    def valid_product(self, keys, all_products):

        for key in keys:
            if key not in all_products:
              return False
        return True

def main():
  downloader = CollectDataFromApi()
  connect = downloader.select_products()
  downloader.select_data(connect)

if __name__ == '__main__':
      main()
