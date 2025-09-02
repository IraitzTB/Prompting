import unittest
from main import suma, resta, saluda
import pytest


def test_saluda(capsys):
    """
    Teste la fonction saluda pour vérifier l'affichage correct sans argument et avec argument, y compris l'emoji.
    """
    saluda()
    captured = capsys.readouterr()
    assert "👋 Hello world!" in captured.out
    saluda("Marie")
    captured = capsys.readouterr()
    assert "👋 Hello Marie!" in captured.out


def test_suma_typique():
    """
    Teste la fonction suma avec des entiers typiques.
    Exemple : suma(2, 3) == 5
    """
    assert suma(2, 3) == 5


def test_suma_extreme():
    """
    Teste suma avec des valeurs extrêmes (grands nombres).
    Exemple : suma(1e10, 1e10) == 2e10
    Voir : https://stackoverflow.com/questions/11264684/python-large-integer
    """
    assert suma(10**10, 10**10) == 2 * 10**10


def test_suma_type_error():
    """
    Teste suma avec des types non supportés (chaîne).
    Exemple : suma('a', 1) doit lever une exception.
    Voir : https://stackoverflow.com/questions/2052390/python-typeerror
    """
    with pytest.raises(TypeError):
        suma('a', 1)


def test_resta_typique():
    """
    Teste la fonction resta avec des entiers typiques.
    Exemple : resta(5, 3) == 2
    """
    assert resta(5, 3) == 2


def test_resta_extreme():
    """
    Teste resta avec des valeurs extrêmes (négatives et grandes).
    Exemple : resta(-1e10, 1e10) == -2e10
    Voir : https://stackoverflow.com/questions/11264684/python-large-integer
    """
    assert resta(-10**10, 10**10) == -2 * 10**10


def test_resta_type_error():
    """
    Teste resta avec des types non supportés (None).
    Exemple : resta(None, 1) doit lever une exception.
    Voir : https://stackoverflow.com/questions/2052390/python-typeerror
    """
    with pytest.raises(TypeError):
        resta(None, 1)


if __name__ == "__main__":
    unittest.main()
