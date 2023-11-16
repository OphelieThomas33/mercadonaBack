import pytest
from Catalog.models import *


# test the str function of the category model
@pytest.mark.django_db
def test_category_model():
    category = Category.objects.create(
        label="Chats",
        parent_id='',
        icon="images/test-category.jpg"
    )
    expected_value = "Chats"
    assert str(category) == expected_value


# test is_valid() function of the discount model
@pytest.mark.django_db
def test_discount_is_valid():
    discount = Discount.objects.create(
        start_date=date(2023, 10, 30),
        end_date=date(2023, 11, 3),
        percentage=50
    )
    expected_value = False
    assert discount.is_valid == expected_value


# test has_valid_discount() and discounted_price functions of the product model
@pytest.mark.django_db
def test_discounted_price():
    discount = Discount.objects.create(
        start_date=date(2023, 10, 30),
        end_date=date(2024, 12, 3),
        percentage=50
    )
    product = Product.objects.create(
        label='Mascara',
        description='Noir',
        price=15.00,
        image='assets/images/mascara-noir.jpg',
        discount=discount,
    )
    expected_value_has_valid_discount = True
    expected_value_discounted_price = 7.50
    assert product.has_valid_discount == expected_value_has_valid_discount
    assert product.discounted_price == expected_value_discounted_price
