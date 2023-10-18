from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "company"
        verbose_name_plural = "companies"

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "country"
        verbose_name_plural = "countries"

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=15)
    city = models.CharField(max_length=50)
    country = models.ForeignKey("Country", on_delete=models.CASCADE)
    company = models.ForeignKey("Company", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
