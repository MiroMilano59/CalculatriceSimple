from dotenv import load_dotenv, dotenv_values
from unittest.mock import patch
from User_interface.UserInterface import check_access

# GLOBAL VARIABLES MANAGEMENT
# 1. Retrieval of secured access data
load_dotenv()
PASSWORD = {**dotenv_values(".env")}['PASSWORD']

# FUNCTION TESTING
def test_secured_access():
    """
        Test whether the behavior of `check_access` is as expected.

        Should return only False or True depending on entry is correct.
        All of this combined with a variable number of allowed wrong entries.
    """

    # BASIC SETTINGS & INITIALIZATION
    path = 'User_interface.UserInterface.getpass'

    # TEST FOUR WRONG ENTRIES
    n = 4
    with patch(path, side_effect=['wrong_password'] * n):
        assert check_access(n) is False

    # TEST CONFIGURATION WITH FOUR ALLOWED ENTRIS WHILE
    sideEffect = ['bad', 'very_bad', PASSWORD, 'wrong_password']
    with patch(path, side_effect=sideEffect):
        assert check_access(n) is True