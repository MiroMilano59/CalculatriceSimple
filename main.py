from UserInterface import check_access, ask_user_for_choice

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


# RUN CALCULATOR APPLICATION
if __name__ == '__main__':
    calculator()