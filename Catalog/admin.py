from django.contrib import admin
from Catalog.models import Category, Product, Discount

# models to display in django admin panel
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Discount)
