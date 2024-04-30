from Functions.addition import additionner_nombre
from Functions.division import division
from Functions.soustraction import soustraire_nombre
from Functions.multiplication import multiplication


# TEST ADDITION FEATURE
def test_addition():
    assert additionner_nombre(1,2) == 3
    assert additionner_nombre(-1,-2) == -3
    assert additionner_nombre(-1,2) == 1
    assert additionner_nombre(0,2) == 2


# TEST DIVISION FEATURE
def test_division():
    assert division(4,2) == 2
    assert division(4,0) == 4


# TEST MULTIPLY FEATURE
def test_multiplication():
    assert multiplication(2,2) == 4
    assert multiplication(-2,2) == -4
    assert multiplication(-2,-2) == 4


# TEST SUBTRACT FEATURE
def test_soustraction():
    assert soustraire_nombre(5,2) == 3
    assert soustraire_nombre(-5,2) == -7