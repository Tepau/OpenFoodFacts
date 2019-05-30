def manage_typing_error(nb1, nb2, user_choice):
    """Check that the user enters an integer corresponding to one of the expected number"""

    choice = 0
    while choice < nb1 or choice > nb2:
        choice = input(user_choice)
        try:
            choice = int(choice)
        except ValueError:
            print('Vous devez choisir un nombre compris entre ', nb1, ' et ', nb2)
            choice = 0
    return choice
