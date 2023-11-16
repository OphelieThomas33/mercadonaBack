from datetime import date

from django.contrib import admin
from django.db import models
from django.utils.safestring import mark_safe


# send product image in assets/images folder
def file_location(instance, filename):
    file_path = f"assets/images/{instance.label}-{filename} "
    return file_path


# category table with parent categories and subcategories
class Category(models.Model):
    label = models.CharField(max_length=50, verbose_name="Libellé")
    parent = models.ForeignKey('self', related_name='subcategories', on_delete=models.CASCADE, blank=True, null=True, verbose_name="Catégorie parente")
    icon = models.ImageField(upload_to=file_location, blank=True, null=True)

    class Meta:
        db_table = "catalog_category"
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"

    def __str__(self):
        return self.label


# discount table
class Discount(models.Model):
    start_date = models.DateField(verbose_name="Date de début")
    end_date = models.DateField(verbose_name="Date de fin")
    percentage = models.DecimalField(max_digits=6, decimal_places=2, default=0, verbose_name="Remise")

    class Meta:
        db_table = "catalog_discount"
        verbose_name = "Promotion"
        verbose_name_plural = "Promotions"

    # calculate if the discount is valid
    # based on dates
    @property
    @admin.display(description="Validité", boolean=True)
    def is_valid(self):
        if self.percentage is not None and self.percentage != 0:
            now = date.today()
            if self.start_date <= now < self.end_date:
                return True
            else:
                return False
        else:
            return False

    def __str__(self):
        return f'{self.start_date} {self.end_date} {self.percentage}'


# product table
# one product can have only one promotion
# one product can have many categories (parent category and subcategory)
class Product(models.Model):
    label = models.CharField(max_length=50, verbose_name="Libellé")
    description = models.TextField(default='', verbose_name="Description")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix de base")
    image = models.ImageField(upload_to=file_location, blank=True, null=True)
    category = models.ManyToManyField(Category, related_name='products', verbose_name="Catégories")
    discount = models.ForeignKey(Discount, models.SET_NULL, blank=True, null=True, verbose_name="Promotion")

    class Meta:
        db_table = "catalog_product"
        verbose_name = "Produit"
        verbose_name_plural = "Produits"

    # indicates if the product is currently being promoted
    @property
    @admin.display(description="Promotion en cours")
    def has_valid_discount(self):
        if self.discount.is_valid:
            return True
        else:
            return False

    # returns discounted price if the product is currently being promoted
    @property
    @admin.display(description="Prix remisé")
    def discounted_price(self):
        if self.discount.is_valid:
            return round((self.price * (1-(self.discount.percentage/100))), 2)
        else:
            return None

    @admin.display(description="Image")
    def image_tag(self):
        return mark_safe('<img src="/../../../../%s" width="150" height="150" />' % self.image)

    def __str__(self):
        return self.label


