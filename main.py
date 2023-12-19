class Category(object):
    _unic = 0

    def __init__(self, name: str, description: str):
        self._name = name
        self._description = description
        self._product = []
        Category._unic += 1
        self._count_products = 0

    @property
    def name(self):
        return self._name

    @property
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

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def price(self):
        return self._price

    @property
    def amount(self):
        return self._amount
