from fonctions_bdd import afficher_substitut, afficher_pdt_sauvegarde, sauvegarder_pdt
from fonctions import gerer_erreur_saisie
from constantes import QUESTION, QUESTION_CAT, QUESTION_FIN_RECHERCHE, QUESTION_APRES_ENREGISTREMENT

nom = input("Entrez votre pseudo: ")
nom_good_format = nom.lower()

boucle_principale = True

while boucle_principale:
    liste_sauvegarde = []
 
    choix_1 = gerer_erreur_saisie(1, 3, QUESTION)

    if choix_1 == 1:

        choix_categorie = gerer_erreur_saisie(1, 5, QUESTION_CAT)

        if choix_categorie == 1:
            afficher_substitut('Sandwichs', liste_sauvegarde)
        if choix_categorie == 2:
            afficher_substitut('Conserves', liste_sauvegarde) 
        if choix_categorie == 3:
            afficher_substitut('Viandes', liste_sauvegarde)
        if choix_categorie == 4:
            afficher_substitut('Poissons', liste_sauvegarde)
        if choix_categorie == 5:
            afficher_substitut('Snacks', liste_sauvegarde)

        choix_fin_de_recherche = gerer_erreur_saisie (1, 3, QUESTION_FIN_RECHERCHE)

        if choix_fin_de_recherche == 1:
            boucle_principale == True

        if choix_fin_de_recherche == 2:
            sauvegarder_pdt(liste_sauvegarde, nom_good_format)
            choix_final = gerer_erreur_saisie(1, 2, QUESTION_APRES_ENREGISTREMENT)

            if choix_final == 1:
                boucle_principale = True
            elif choix_final == 2:
                print("Au revoir ! ")
                boucle_principale = False

        if choix_fin_de_recherche == 3:
            print('Bye Bye')
            boucle_principale = False

    if choix_1 == 2:
        afficher_pdt_sauvegarde(nom_good_format)

        choix_final = gerer_erreur_saisie(1, 2, QUESTION_APRES_ENREGISTREMENT)
        if choix_final == 1:
            boucle_principale = True
        elif choix_final == 2:
            print("Bye Bye")
            boucle_principale = False

    if choix_1 == 3:
            print('Bye bye')
            boucle_principale = False

