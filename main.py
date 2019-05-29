from fonctions_bdd import display_substitut, display_saved_product, save_product
from fonctions import manage_typing_error
from constantes import MAIN_QUESTION, QUESTION_CATEGORY, QUESTION_END_RESEARCH, QUESTION_AFTER_RECORDING

name = input("Entrez votre pseudo: ")
name_good_format = name.lower()

main_loop = True

while main_loop:
    saved_list = []
 
    choice_1 = manage_typing_error(1, 3, MAIN_QUESTION)

    if choice_1 == 1:

        category_choice = manage_typing_error(1, 5, QUESTION_CATEGORY)

        if category_choice == 1:
            display_substitut('Sandwichs', saved_list)
        if category_choice == 2:
            display_substitut('Conserves', saved_list) 
        if category_choice == 3:
            display_substitut('Viandes', saved_list)
        if category_choice == 4:
            display_substitut('Poissons', saved_list)
        if category_choice == 5:
            display_substitut('Snacks', saved_list)

        end_research_choice = manage_typing_error (1, 3, QUESTION_END_RESEARCH)

        if end_research_choice == 1:
            main_loop == True

        if end_research_choice == 2:
            save_product(saved_list, nom_good_format)
            final_choice = manage_typing_error(1, 2, QUESTION_AFTER_RECORDING)

            if final_choice == 1:
                main_loop = True
            elif final_choice == 2:
                print("Au revoir ! ")
                main_loop = False

        if end_research_choice == 3:
            print('Bye Bye')
            main_loop = False

    if choice_1 == 2:
        display_saved_product(nom_good_format)

        final_choice = manage_typing_error(1, 2, QUESTION_AFTER_RECORDING)
        if final_choice == 1:
            main_loop = True
        elif final_choice == 2:
            print("Bye Bye")
            main_loop = False

    if choice_1 == 3:
            print('Bye bye')
            main_loop = False

