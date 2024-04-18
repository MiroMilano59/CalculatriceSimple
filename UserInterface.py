from re import match
from dotenv import load_dotenv, dotenv_values
from addition import additionner_nombre as sum_numbers
from soustraction import soustraire_nombre as substract
from division import division as divide
from multiplication import multiplication as multiply
from getpass import getpass

# GLOBAL VARIABLES MANAGEMENT
# 1. Retrieval of secured access data
load_dotenv()
PASSWORD = {**dotenv_values(".env")}['PASSWORD']

# 2. Other global variables to manage in beforehand
options = {'+': ('sum', sum_numbers),
           '-': ('diff', substract),
           '*': ('mult', multiply),
           '/': ('div', divide),
           #'r': ('reset', False),
           'Q': ('Quit', True)}

#choices_list = list(options.keys()
choices_list = list(options)
maximum_length = max([len(key) for key in choices_list])


# IMPLEMENTATION OF ACCESS MANAGER FUNCTION
def check_access(i=3):
    """
        Asks and wait for the user to input password.

    argument(s):
        i (int): Number of false user entry before definitely returning False.
                 Default value for `i` is 3.
    
    Retuns:
        A boolean indicating wether acces shall be granted to the user or not.
    """

    # INITIALIZATION & BASIC SETTINGS
    n, isPasswdOk = 0, False

    # ASKS FOR PASSWORD
    while n < i and not isPasswdOk:
        n += 1
        passwd = getpass("Veuillez saisir le mode de passe: ")
        isPasswdOk = passwd == PASSWORD
    
    # DISPLAYS REJECTED MESSAGE
    __ = print('Désolé, accès refusé car mot de passe erroné') if not isPasswdOk else None

    # FUNCTION OUTPUT
    return isPasswdOk


# IMPLEMENTATION OF CALCULATOR'S USER INTERFACE FUNCTIONS
def enumerate_options():
    """
        Shows the user the available options (no arguments required)
    """

    # INITIALIZATION & BASIC SETTINGS
    x = 1 + maximum_length

    # DISPLAYS AVAILABLE CHOICES
    for key, (action, function) in options.items():
        print(f'{key.ljust(x)}: {action}')


def match_numeric(string):
    """
        Checks wether a string is numerical or not.

    Argument(s):
        string (str): String to be checked

    Returns:
        A boolean (True or False) whether the input is numerical or not.
    """

    # PATTERNS
    regx1 = '\d+\.{0,1}\d*'
    regx2 = '\d*\.{0,1}\d+'

    # OUTPUT
    return bool(match(regx1, string)) or bool(match(regx2, string))


def ask_user_for_numeric(i=''):
    """
        Asks and wait for the user to input a numerical value.

    Arguments(s):
        i (int|str): Whether to add a suffix or anything else to the input text 

    Returns:
        Either an int or a float depending on the user entry
    """

    # INITIALIZATION & BASIC SETTINGS
    number = ''
    input_message = 'Veuillez saisir la valeur {}: '.format

    # INPUT REQUEST ROUTINE
    while not match_numeric(number):
        number = input(input_message(str(i)))

    # FUCNTION OUTPUT
    return eval(number)


def ask_user_for_choice():
    """
        Asks user to make choice(s) (no arguments required).

        Returns:
            shows result of required computation and returns `Quit mode` status
    """

    # PARAMETERS INITIALIZATION & BASIC SETTINGS
    #choice, reset, quit, a, b = (None)*5
    choice, quit = None, True
    
    # LIST ALL AVAILABLE CHOICES TO LET THE USER MAKE THEIR CHOICE
    enumerate_options()

    # ASK AND WAITH FOR THE USER TO MAKE THEIR CHOICE THEN COMPUTE
    while choice not in choices_list:
        choice = input('Merci de saisir votre choix: ')
        choice = choice.lower() if choice != 'Q' else choice

    # WHEN RELEVANT: ASK AND WAIT FOR THE USER'S VALUES AND RETURN RESULT
    if choice in choices_list[:-1]:
        # Retriev values
        print('\n')
        a, b = [ask_user_for_numeric(i+1) for i in range(2)]

        # Displays result
        print(f'\nRésultat: {options[choice][-1](a, b)}')

        # Set `Quit mode` status
        quit = False

    # FUNCTION OUTPUT
    return quit