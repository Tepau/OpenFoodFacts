from constants import CATEGORIES

def final_structure(recovered_product_list):
    """ Returns a format suitable for insertion into the database

    only the names of the searched categories are kept
    
    """

    sorted_categories = []                
    for product in recovered_product_list:
        list_product = list(product) 
        list_categories = list_product[5].split(",") 
        clean_categories_no_space = [] 
        final_categories = [] 
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
    """ Returns true if all the desired keys are in the dictionary  """

    for key in keys:
        if key not in all_products:
            return False
    return True