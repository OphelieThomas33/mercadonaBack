from django.db import models


# Company table
class Company(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "stores_company"
        verbose_name = "Entreprise"
        verbose_name_plural = "Entreprises"

    def __str__(self):
        return self.name


# country table
class Country(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "stores_country"
        verbose_name = "Pays"
        verbose_name_plural = "Pays"

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
        verbose_name = "Magasin"
        verbose_name_plural = "Magasins"

    def __str__(self):
        return self.name
