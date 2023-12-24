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
