class Category(object):
    """Класс Category предназначен для хранения информации о категории товаров.
    Каждый экземпляр класса содержит название категории, описание и список продуктов.

    Атрибуты:
        _name (str): Название категории.
        _description (str): Описание категории.
        _product (list): Список продуктов в данной категории.
        _unic (int): Классовая переменная, отслеживающая количество созданных экземпляров.
        _count_products (int): Количество продуктов в категории."""
    _unic = 0

    def __init__(self, name: str, description: str, product_list=None):
        """Инициализирует экземпляр категории с заданным названием, описанием и списком продуктов."""
        if product_list is None:
            product_list = []
        self._name = name
        self._description = description
        self._product = product_list
        Category._unic += 1
        self._count_products = 0

    def add(self, product):
        """Добавляет объект product в список продуктов категории."""
        self._product.append(product)

    def products(self):
        """Выводит информацию о всех продуктах в категории и возвращает список продуктов."""
        for product in self._product:
            print(f"{product.name}, {product.price} руб. Остаток: {product.amount} шт.")
        return self._product

    @property
    def name(self):
        """Возвращает название категории."""
        return self._name

    @property
    def description(self):
        """Возвращает описание категории."""
        return self._description


class Product(object):
    """
    Класс Product предназначен для создания и хранения данных о товаре.

    Атрибуты:
        _name (str): Название продукта.
        _description (str): Описание продукта.
        _price (float): Цена продукта.
        _amount (int): Количество единиц продукта.
        _unic (int): Классовая переменная, отслеживающая количество созданных экземпляров.
        """
    _unic = 0

    def __init__(self, name: str, description: str, price: float, amount: int):
        """Инициализирует экземпляр продукта с заданными характеристиками."""
        self._name = name
        self._description = description
        self._price = price
        self._amount = amount
        Product._unic += 1

    @staticmethod
    def create_product(name: str, description: str, price: float, amount: int):
        """Создает и возвращает экземпляр класса Product."""
        return Product(name, description, price, amount)

    @property
    def price(self):
        """Возвращает цену продукта."""
        return self._price

    @price.setter
    def price(self, new_price):
        """
        Устанавливает новую цену продукта.

        Если новая цена ниже текущей, запрашивает подтверждение для изменения цены.
        """
        if self._price > new_price:
            answer = input("Ввёная цена ниже текущей. Подтвердить? (y/n)")
            if answer == "y":
                self._price = new_price
            else:
                print("Действие отменено")

    @price.deleter
    def price(self):
        """Удаляет информацию о цене продукта."""
        del self._price

    @property
    def name(self):
        """Возвращает название продукта."""
        return self._name

    @property
    def description(self):
        """Возвращает описание продукта."""
        return self._description

    @property
    def amount(self):
        """Возвращает количество единиц продукта на складе."""
        return self._amount

