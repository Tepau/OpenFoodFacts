def gerer_erreur_saisie(variable, nb1, nb2):

    try :
        variable = int(variable)
    except ValueError:
        print('Vous devez choisir un nombre compris entre ', nb1, ' et ', nb2)
        variable = 0
    finally:
        return variable


