# Generated by Django 4.1 on 2023-10-29 01:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("Catalog", "0008_remove_category_subcategory_category_icon_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="parent",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="subcategories",
                to="Catalog.category",
            ),
        ),
        migrations.AlterField(
            model_name="discount",
            name="end_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 10, 29, 2, 17, 51, 886904, fold=1)
            ),
        ),
        migrations.AlterField(
            model_name="discount",
            name="start_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 10, 29, 2, 17, 51, 886904, fold=1)
            ),
        ),
    ]
