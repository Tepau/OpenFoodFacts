from fonctions import afficher_substitut, afficher_pdt_sauvegarde, sauvegarder_pdt


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
                        afficher_substitut('Sandwichs', liste_sauvegarde)
                    elif choix_categorie == 2:
                        afficher_substitut('Conserves', liste_sauvegarde)  
                    elif choix_categorie == 3:
                        afficher_substitut('Viandes', liste_sauvegarde)
                    elif choix_categorie == 4:
                        afficher_substitut('Poissons', liste_sauvegarde)
                    elif choix_categorie == 5:
                        afficher_substitut('Snacks', liste_sauvegarde)

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
                            sauvegarder_pdt(liste_sauvegarde, nom_good_format)
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
                afficher_pdt_sauvegarde(nom_good_format)

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

