class Category(object):
    _unic = 0

    def __init__(self, name: str, description: str):
        self._name = name
        self._description = description
        self._product = []
        Category._unic += 1
        self._count_products = 0

    def add(self, product):
        self._product.append(product)

    def products(self):
        return self._product

    def name(self):
        return self._name

    def description(self):
        return self._description


class Product(object):
    _unic = 0

    def __init__(self, name: str, description: str, price: float, amount: int):
        self._name = name
        self._description = description
        self._price = price
        self._amount = amount
        Product._unic += 1

    def my_unic(self):
        return Product._unic

    def name(self):
        return self._name

    def description(self):
        return self._description

    def price(self):
        return self._price

    def amount(self):
        return self._amount
