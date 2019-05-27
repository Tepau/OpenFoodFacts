from constantes import CATEGORIES

def final_structure(liste_pdt_recuperes):

    sorted_categories =[]                
    for produit in liste_pdt_recuperes:
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
        sorted_categories.append(liste)

    final_format = []

    for produit in sorted_categories:
        produit[5] = ", ".join(produit[5])
        produit_bon_format = tuple(produit)
        final_format.append(produit_bon_format)

    return final_format

def valid_product(keys, all_products):
    for key in keys:
        if key not in all_products:
            return False
    return True