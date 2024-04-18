from UserInterface import check_access, ask_user_for_choice
from UserInterface import historique

def calculator():
    """
        Runs calculator application (no arguments required)
    """

    # CALCULATOR APPLICATION
    if check_access():
    #if True:
        # Welcome message
        print('HELLO, BIENVENUE DANS CALCULIX, VOTRE APPLICATION DE CALCUL\n')

        # computation mode
        quit = False
        while not quit:
            print()
            quit = ask_user_for_choice()

        # Leaving message
        print('\nAU REVOIR ET BONNE JOURNEE.')
        afficher_historique()
        


def afficher_historique():
    print("\nHistorique des Calculs:")
    for operation in historique:
        if operation[0] == '+':
            print(f"{operation[1]} + {operation[2]} = {operation[3]}")
        elif operation[0] == '-':
            print(f"{operation[1]} - {operation[2]} = {operation[3]}")
        elif operation[0] == '*':
            print(f"{operation[1]} * {operation[2]} = {operation[3]}")
        elif operation[0] == '/':
            print(f"{operation[1]} / {operation[2]} = {operation[3]}")


# RUN CALCULATOR APPLICATION
if __name__ == '__main__':
    calculator()