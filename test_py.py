import pytest
from app import calculer_puissance

def test_puissance_entier_positif():
    assert calculer_puissance(2, 3) == 8

def test_puissance_entier_negatif():
    assert calculer_puissance(-2, 3) == -8

def test_puissance_flottant():
    assert pytest.approx(calculer_puissance(2.5, 2), 0.01) == 6.25
