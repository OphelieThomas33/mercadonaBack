from django.db import models


# Company table
class Company(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "stores_company"
        verbose_name = "company"
        verbose_name_plural = "companies"

    def __str__(self):
        return self.name


# country table
class Country(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "stores_country"
        verbose_name = "country"
        verbose_name_plural = "countries"

    def __str__(self):
        return self.name


# store table
# a store can have only one country
# a store can have only one company
class Store(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=15)
    city = models.CharField(max_length=50)
    country = models.ForeignKey("Country", on_delete=models.CASCADE)
    company = models.ForeignKey("Company", on_delete=models.CASCADE)

    class Meta:
        db_table = "stores_stores"

    def __str__(self):
        return self.name
