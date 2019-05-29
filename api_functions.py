from constants import CATEGORIES

def final_structure(recovered_product_list):

    sorted_categories =[]                
    for product in recovered_product_list:
        list_product = list(product) #transformation du tuple d'un produit en liste
        list_categories = list_product[5].split(",") #transformation des categories sous forme de liste
        clean_categories_no_space =[] # Variables vide qui va contenir la liste des categories sans espaces
        final_categories =[] #Variable vide qui va contenir les categories que l'on veut et qui sont présentes
        for categorie in list_categories:
            no_space = categorie.strip()
            clean_categories_no_space.append(no_space)
            for name in clean_categories_no_space:
                if name in CATEGORIES:
                    if name not in final_categories:
                        final_categories.append(name)
            list_product[5] = final_categories
        sorted_categories.append(list_product)

    final_format = []

    for product in sorted_categories:
        product[5] = ", ".join(product[5])
        product_format_ok = tuple(product)
        final_format.append(product_format_ok)

    return final_format

def valid_product(keys, all_products):
    for key in keys:
        if key not in all_products:
            return False
    return True