# Generated by Django 4.1 on 2023-10-25 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
            options={
                "verbose_name": "company",
                "verbose_name_plural": "companies",
            },
        ),
        migrations.CreateModel(
            name="Country",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
            options={
                "verbose_name": "country",
                "verbose_name_plural": "countries",
            },
        ),
        migrations.CreateModel(
            name="Store",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("address", models.CharField(max_length=255)),
                ("zip_code", models.CharField(max_length=15)),
                ("city", models.CharField(max_length=50)),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Stores.company"
                    ),
                ),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Stores.country"
                    ),
                ),
            ],
        ),
    ]
