from src.main import *


def fuel_filling():
    prod = Product("appel", "green", 100, 20)
    assert prod.name() == "appel"
    assert prod.description() == "green"
    assert prod.price() == 100
    assert prod.amount() == 20


def test_category():
    categ = Category("appel", "green")
    prod = Product("appel", "green", 100, 20)
    categ.add(prod)
    assert categ.name() == "appel"
    assert categ.description() == "green"
    assert categ._unic == 1
    assert categ.products() == [prod]
