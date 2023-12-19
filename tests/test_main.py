from src.main import *


def fuel_filling():
    prod = Product("appel", "green", 100, 20)
    assert prod.name == "appel"
    assert prod.description == "green"
    assert prod.price == 100
    assert prod.amount == 20


def test_category():
    prod = Category("appel", "green")
    assert prod._name == "appel"
    assert prod._description == "green"
