from django.contrib import admin
from Stores.models import Store, Company, Country

# Register your models here.
admin.site.register(Store)
admin.site.register(Company)
admin.site.register(Country)
