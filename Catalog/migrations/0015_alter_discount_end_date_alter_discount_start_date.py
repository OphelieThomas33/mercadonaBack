# Generated by Django 4.1 on 2023-11-07 17:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Catalog", "0014_alter_discount_end_date_alter_discount_start_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="discount",
            name="end_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 7, 18, 34, 29, 988765)
            ),
        ),
        migrations.AlterField(
            model_name="discount",
            name="start_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 7, 18, 34, 29, 988765)
            ),
        ),
    ]