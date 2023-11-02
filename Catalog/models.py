from datetime import datetime

from django.db import models


# Create your models here.
class Category(models.Model):
    label = models.CharField(max_length=50)
    parent = models.ForeignKey('self', related_name='subcategories', on_delete=models.CASCADE, null=True)
    icon = models.ImageField(upload_to="images/", null=True)

    class Meta:
        db_table = "catalog_category"
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.label


class Discount(models.Model):
    start_date = models.DateTimeField(default=datetime.today())
    end_date = models.DateTimeField(default=datetime.today())
    percentage = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    class Meta:
        db_table = "catalog_discount"

    @property
    def is_valid(self):
        if self.percentage is not None and self.percentage != 0:
            now = datetime.today().date()
            if self.start_date.date() <= now < self.end_date.date():
                return True
            else:
                return False
        else:
            return False

    def __str__(self):
        return f'{self.start_date} {self.end_date} {self.percentage}'


class Product(models.Model):
    label = models.CharField(max_length=50)
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="assets/images/")
    category = models.ManyToManyField(Category, related_name='products')
    discount = models.ForeignKey(Discount, models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = "catalog_product"

    @property
    def has_valid_discount(self):
        if self.discount.is_valid:
            return True
        else:
            return False

    @property
    def discounted_price(self):
        if self.discount.is_valid:
            return round((self.price * (1-(self.discount.percentage/100))), 2)
        else:
            return None

    def __str__(self):
        return self.label




