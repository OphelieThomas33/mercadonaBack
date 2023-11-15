# Generated by Django 4.1 on 2023-11-14 17:16

import Catalog.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Catalog", "0019_alter_category_icon_alter_category_parent_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="icon",
            field=models.ImageField(
                blank=True, null=True, upload_to=Catalog.models.file_location
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to=Catalog.models.file_location
            ),
        ),
    ]
