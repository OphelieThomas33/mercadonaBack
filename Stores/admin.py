from django.contrib import admin
from Stores.models import Store, Company, Country

# models to display in django admin panel
admin.site.register(Store)
admin.site.register(Company)
admin.site.register(Country)
