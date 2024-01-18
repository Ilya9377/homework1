from typing import Any
from abc import ABC, abstractmethod


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
        if product.__name__ in ["Smartphone", "Grass", "Product"]:
            self._product.append(product)
            return "Товар добавлен"
        else:
            return "Объект не является товаром"

    def products(self):
        """Выводит информацию о всех продуктах в категории и возвращает список продуктов."""
        for product in self._product:
            print(f"{product.name}, {product.price} руб. Остаток: {product.amount} шт.")
        return self._product

    def __str__(self):
        """Возвращает строковое представление объекта"""
        return f"{self.name}, количество продуктов: {len(self)} шт."

    def __len__(self):
        """Возвращает общее количество продуктов"""
        amount = 0
        for product in self._product:
            amount += len(product)
        return amount

    @property
    def name(self):
        """Возвращает название категории."""
        return self._name

    @property
    def description(self):
        """Возвращает описание категории."""
        return self._description

    def __repr__(self):
        return f"{self.__name__}, {str(self)}, Описание: {self.description}"


class AbstractProduct(ABC):
    def __init__(self, name: str, description: str, price: float, amount: int):
        """Инициализирует экземпляр продукта с заданными характеристиками."""
        self._name = name
        self._description = description
        self._price = price
        self._amount = amount

    def __add__(self, other: Any):
        """Определяет поведение операции сложения (+) для продуктов"""
        if other.__name__ == self.__name__:
            return self._price * self._amount + other.price * other.amount
        else:
            return f"Второй объект не является классом {self.__name__}"

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

    def __str__(self):
        """Возвращает строковое представление объекта Product."""
        return f"{self.name}, {self.price} руб. Остаток: {self.amount} шт."

    def __len__(self):
        """Возвращает квантитативное представление объекта Product, используемое функцией len()."""
        return self.amount

    @abstractmethod
    def __repr__(self):
        pass


class Product(AbstractProduct):
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
        super().__init__(name, description, price, amount)
        self.__name__ = "Product"
        Product._unic += 1

    @staticmethod
    def create_product(name: str, description: str, price: float, amount: int):
        """Создает и возвращает экземпляр класса Product."""
        return Product(name, description, price, amount)

    def __repr__(self):
        return f"{self.__name__}, {str(self)}"


class Smartphone(AbstractProduct):
    def __init__(self, name: str, description: str, price: float,
                 amount: int, power: int, model: str, storage: int, color: str):
        """
                    Инициализация объекта класса Smartphone, который наследуется от Product.

                    :param name: Название смартфона.
                    :param description: Описание смартфона.
                    :param price: Цена смартфона.
                    :param amount: Количество смартфонов на складе.
                    :param power: Производительность.
                    :param model: Модель смартфона.
                    :param storage: Объем встроенной памяти смартфона.
                    :param color: Цвет смартфона.
                    """
        super().__init__(name, description, price, amount)
        self._power = power
        self._model = model
        self._storage = storage
        self._color = color
        self.__name__ = "Smartphone"

    @property
    def power(self):
        """Возвращает производиттельность смартфона."""
        return self._power

    @property
    def model(self):
        """Возвращает модель смартфона."""
        return self._model

    @property
    def storage(self):
        """Возвращает объем встроенной памяти смартфона."""
        return self._storage

    @property
    def color(self):
        """Возвращает цвет смартфона."""
        return self._color

    def __repr__(self):
        return (f"{self.__name__}, {str(self)}, {self.power}, {self.model},"
                f" {self.storage}, {self.color}")


class Grass(AbstractProduct):
    def __init__(self, name: str, description: str, price: float, amount: int, country: str,
                 term_rise: int, color: str):
        """
               Инициализация объекта класса Grass, который наследуется от Product.

               :param name: Название травы.
               :param description: Описание травы.
               :param price: Цена травы.
               :param amount: Количество травы на складе.
               :param country: Страна происхождения.
               :param term_rise: Срок выращивания травы до урожая.
               :param color: Цвет травы.
               """
        super().__init__(name, description, price, amount)
        self._country = country
        self._term_rise = term_rise
        self._color = color
        self.__name__ = "Grass"

    @property
    def color(self):
        """Возвращает цвет травы."""
        return self._color

    @property
    def country(self):
        """Возвращает страну происхождения травы."""
        return self._country

    @property
    def term_rise(self):
        """Возвращает срок выращивания травы до урожая."""
        return self._term_rise

    def __repr__(self):
        return (f"{self.__name__}, {str(self)}, {self.country}, {self.term_rise},"
                f" {self.color}")


s = Grass("трава", "", 10, 10, "usa", 2, "green")
print(repr(s))
