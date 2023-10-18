from django.contrib import admin
from Catalog.models import Category, Product, Discount

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Discount)
