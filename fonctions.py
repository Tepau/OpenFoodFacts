def gerer_erreur_saisie(nb1, nb2, choix_user):
    choix = 0
    while choix < nb1 or choix > nb2:
        choix = input(choix_user)
        try :
            choix = int(choix)
        except ValueError:
            print('Vous devez choisir un nombre compris entre ', nb1, ' et ', nb2)
            choix = 0
    return choix
