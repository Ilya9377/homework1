import pytest

from src.main import Product, Category


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
