from datetime import datetime
from django.db import models


# Create your models here.
class Category(models.Model):
    label = models.CharField(max_length=50)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.label


class Discount(models.Model):
    start_date = models.DateTimeField(default=datetime.today)
    end_date = models.DateTimeField(default=datetime.today)
    percentage = models.FloatField(default=0)

    def __str__(self):
        return f'{self.start_date} {self.end_date} {self.percentage}'


class Product(models.Model):
    label = models.CharField(max_length=50)
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="images/")
    category = models.ManyToManyField(Category)
    discount = models.ForeignKey(Discount, models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.label


