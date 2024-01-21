import pytest

from src.main import Product, Category, Smartphone, Grass


@pytest.fixture
def check_product_data():
    """Фикстура pytest для предоставления тестовых данных продукта."""
    return ["appel", "green", 100, 20]


def test_product_initialization(check_product_data):
    """
    Тестирование создания экземпляра класса Product.
    Используя фикстуру check_product_data, тест проверяет,
    что все атрибуты продукта инициализированы корректно.
    """
    product_data = check_product_data
    prod = Product(*product_data)
    assert prod.name == product_data[0]
    assert prod.description == product_data[1]
    assert prod.price == product_data[2]
    assert prod.amount == product_data[3]


def test_category_initialization_and_add_product():
    """
    Тестирование инициализации категории и добавления продукта в категорию.

    Создает экземпляр Category и экземпляр Product, затем добавляет продукт в категорию.
    Проверяет корректность названия и описания категории, корректное отображение
    уникального идентификатора и список продуктов после добавления в категорию.
    """
    category_name = "fruits"
    category_description = "sweet and sour"
    product_name = "apple"
    product_description = "green apple"
    product_price = 100
    product_amount = 20
    # Инициализация категории
    categ = Category(category_name, category_description)
    # Создание и добавление продукта в категорию
    prod = Product(product_name, product_description, product_price, product_amount)
    categ.add(prod)
    # Проверки
    assert categ.name == category_name
    assert categ.description == category_description
    assert categ._unic == 1
    assert prod in categ.products()


def test_product_str(check_product_data):
    """
        Тестирует строковое представление продукта.

        Функция проверяет, что строковое представление объекта продукта, созданного с помощью
        данных из check_product_data, соответствует ожидаемому формату.

        :param check_product_data: кортеж данных продукта
        """
    product_data = check_product_data
    prod = Product(*product_data)
    true_output = f"{product_data[0]}, {product_data[2]} руб. Остаток: {product_data[3]} шт."
    assert str(prod) == true_output


def test_product_add(check_product_data):
    """
        Тестирует функционал сложения двух продуктов.

        Функция создает два объекта продукта с одинаковыми данными из check_product_data
        и проверяет, что результат их сложения соответствует ожидаемому значению,
        предполагая, что сложение продуктов складывает их стоимость умноженную на кол-во.

        :param check_product_data: кортеж данных продукта
        """
    product_data = check_product_data
    prod_1 = Product(*product_data)
    prod_2 = Product(*product_data)
    true_output = product_data[2] * product_data[3] * 2
    sum_product = prod_1 + prod_2
    assert sum_product == true_output


def test_category_str():
    """
        Тестирует строковое представление категории.

        Функция создает объект категории и добавляет в нее продукт. Проверяется,
        что строковое представление категории соответствует ожидаемому формату,
        включая количество добавленных продуктов.
        """
    category_name = "fruits"
    category_description = "sweet and sour"
    product_name = "apple"
    product_description = "green apple"
    product_price = 100
    product_amount = 20
    # Инициализация категории
    categ = Category(category_name, category_description)
    # Создание и добавление продукта в категорию
    prod = Product(product_name, product_description, product_price, product_amount)
    categ.add(prod)
    true_output = f"{category_name}, количество продуктов: {product_amount} шт."
    real_output = str(categ)
    assert true_output == real_output


def test_category_len():
    """
        Тестирует функционал получения количества продуктов в категории.

        Функция создает объект категории, добавляет в нее два продукта и проверяет,
        что результат вызова встроенной функции len() для категории возвращает
        корректное общее количество продуктов.

        Предполагается, что метод __len__ категории возвращает общее количество
        единиц всех продуктов в категории, что позволяет использовать функцию len().
        В этом примере проверяется, что общее количество (product_amount * 2) яблок
        после добавления двух одинаковых продуктов с корректным количеством совпадает
        с ожидаемым результатом.
        """
    category_name = "fruits"
    category_description = "sweet and sour"
    product_name = "apple"
    product_description = "green apple"
    product_price = 100
    product_amount = 20
    # Инициализация категории
    categ = Category(category_name, category_description)
    # Создание и добавление продукта в категорию
    prod_1 = Product(product_name, product_description, product_price, product_amount)
    prod_2 = Product(product_name, product_description, product_price, product_amount)
    categ.add(prod_1)
    categ.add(prod_2)
    true_output = product_amount * 2
    real_output = len(categ)
    assert true_output == real_output


@pytest.fixture
def check_product_smartphone():
    """
        Фикстура pytest для создания тестовых данных для смартфона.

        :return: Список значений, соответствующих параметрам инициализации экземпляра класса Smartphone.
        """
    return ["Nokia 3310", "smartphone", 10, 10, 11000, "3310", 32, "black"]


@pytest.fixture
def check_product_grass():
    """
        Фикстура pytest для создания тестовых данных для травы.

        :return: Список значений, соответствующих параметрам инициализации экземпляра класса Grass.
        """
    return ["green", "", 10, 10, "russia", 20, "green"]


def test_smartphone_init(check_product_smartphone):
    """
       Тест инициализации экземпляра класса Smartphone.

       Использует фикстуру check_product_smartphone для проверки корректности создания экземпляра.

       Проверяет, что атрибуты экземпляра совпадают с данными, предоставленными фикстурой.
       """
    product_data = check_product_smartphone
    prod = Smartphone(*product_data)
    assert prod.name == product_data[0]
    assert prod.description == product_data[1]
    assert prod.price == product_data[2]
    assert prod.amount == product_data[3]
    assert prod.power == product_data[4]
    assert prod.model == product_data[5]
    assert prod.storage == product_data[6]
    assert prod.color == product_data[7]


def test_grass_init(check_product_grass):
    """
        Тест инициализации экземпляра класса Grass.

        Использует фикстуру check_product_grass для проверки корректности создания экземпляра.

        Проверяет, что атрибуты экземпляра совпадают с данными, предоставленными фикстурой.
        """
    product_data = check_product_grass
    prod = Grass(*product_data)
    assert prod.name == product_data[0]
    assert prod.description == product_data[1]
    assert prod.price == product_data[2]
    assert prod.amount == product_data[3]
    assert prod.country == product_data[4]
    assert prod.term_rise == product_data[5]
    assert prod.color == product_data[6]


def test_add_product():
    """
        Тест добавления продукта в категорию.

        Создает экземпляр категории и экземпляр продукта (смартфон), затем проверяет,
        что продукт успешно добавляется в категорию и метод возвращает ожидаемое сообщение.
        """
    category_name = "gadget"
    category_description = ""
    product_name = "apple"
    product_description = "smartphone"
    product_price = 100
    product_amount = 20
    product_power = 100
    product_model = "11"
    product_storage = 128
    product_color = "black"
    categ = Category(category_name, category_description)
    prod = Smartphone(product_name, product_description, product_price, product_amount,
                      product_power, product_model, product_storage, product_color)
    real_output = categ.add(prod)
    true_output = "Товар добавлен"
    assert true_output == real_output


def test_repr_grass(check_product_grass):
    """Проверяет правильность реализации метода repr для класса Grass."""
    product_data = check_product_grass
    prod = Grass(*product_data)
    true_output = "Grass, green, 10 руб. Остаток: 10 шт., russia, 20, green"
    real_output = repr(prod)
    assert true_output == real_output


def test_repr_smartphone(check_product_smartphone):
    """Проверяет правильность реализации метода repr для класса Smartphone."""
    product_data = check_product_smartphone
    prod = Smartphone(*product_data)
    true_output = "Smartphone, Nokia 3310, 10 руб. Остаток: 10 шт., 11000, 3310, 32, black"
    real_output = repr(prod)
    assert true_output == real_output


def test_repr_product(check_product_data):
    """Проверяет правильность реализации метода repr для класса Product"""
    product_data = check_product_data
    prod = Product(*product_data)
    true_output = "Product, appel, 100 руб. Остаток: 20 шт."
    real_output = repr(prod)
    assert true_output == real_output


def test_category_mean_price(check_product_smartphone):
    """
        Тестирование метода mean_price() класса Category для непустой категории.
        """
    category_name = "fruits"
    category_description = "sweet and sour"
    # Инициализация категории
    categ = Category(category_name, category_description)
    # Создание и добавление продукта в категорию
    prod = Smartphone(*check_product_smartphone)
    categ.add(prod)
    true_output = 10.0
    real_output = categ.mean_price()
    assert true_output == real_output


def test_category_mean_price_empty(check_product_smartphone):
    """
       Тестирование метода mean_price() класса Category для пустой категории.
        """
    category_name = "fruits"
    category_description = "sweet and sour"
    # Инициализация категории
    categ = Category(category_name, category_description)
    # Создание и добавление продукта в категорию
    true_output = 0
    real_output = categ.mean_price()
    assert true_output == real_output
