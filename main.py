from fonctions import *
from fonctions_bdd import afficher_substitut, afficher_pdt_sauvegarde, sauvegarder_pdt

nom = input("Entrez votre pseudo: ")
nom_good_format = nom.lower()

boucle_principale = True

while boucle_principale:
        liste_sauvegarde = []

        choix_1 = 0
        while choix_1 < 1 or choix_1 > 3:
            choix_1 = input("Que souhaitez vous faire?" '\n'
                            "1 : Rechercher un produit" '\n'
                            "2 : Consulter votre historique" '\n'
                            "3 : Quitter l'application" '\n'
                            " :  ")
            choix_1 = gerer_erreur_saisie(choix_1, 1, 3)

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
                    choix_categorie = gerer_erreur_saisie(choix_categorie, 1, 5)

                if choix_categorie == 1:
                    afficher_substitut('Sandwichs', liste_sauvegarde)
                    choix_fin_de_recherche = 0
                if choix_categorie == 2:
                    afficher_substitut('Conserves', liste_sauvegarde) 
                    choix_fin_de_recherche = 0
                if choix_categorie == 3:
                    afficher_substitut('Viandes', liste_sauvegarde)
                    choix_fin_de_recherche = 0
                if choix_categorie == 4:
                    afficher_substitut('Poissons', liste_sauvegarde)
                    choix_fin_de_recherche = 0
                if choix_categorie == 5:
                    afficher_substitut('Snacks', liste_sauvegarde)
                    choix_fin_de_recherche = 0

                while choix_fin_de_recherche < 1 or choix_fin_de_recherche > 3:
                    choix_fin_de_recherche = input("Voulez pouvez désormais :" '\n'
                    "Revenir au Menu Principal : 1" '\n'
                    "Sauvegarder votre recherche : 2" '\n'
                    "Quitter l'application : 3" '\n'
                    "A vous de choisir :  ")

                    choix_fin_de_recherche = gerer_erreur_saisie(choix_fin_de_recherche, 1, 3)

                    if choix_fin_de_recherche == 1:
                        boucle_principale == True

                    if choix_fin_de_recherche == 2:
                        sauvegarder_pdt(liste_sauvegarde, nom_good_format)
                        choix_final = 0
                        while choix_final < 1 or choix_final > 2:
                            choix_final = input("Vous souhaitez : " '\n'
                                                    "Revenir au Menu Principal : 1" '\n'
                                                    "Quitter le programme : 2" '\n'
                                                    "ici  : ")
                            choix_final = gerer_erreur_saisie(choix_final, 1, 2)

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

                choix_final = 0
                while choix_final < 1 or choix_final > 2:
                    choix_final = input("Vous souhaitez : " '\n'
                                    "Revenir au Menu Principal : 1" '\n'
                                    "Quitter le programme : 2" '\n'
                                    "ici  : ")

                    choix_final = gerer_erreur_saisie(choix_final, 1, 2)

                    if choix_final == 1:
                        boucle_principale = True
                    elif choix_final == 2:
                        print("Bye Bye")
                        boucle_principale = False

            if choix_1 == 3:
                print('Bye bye')
                boucle_principale = False

