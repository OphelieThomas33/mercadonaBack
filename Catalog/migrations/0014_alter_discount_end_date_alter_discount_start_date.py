# Generated by Django 4.1 on 2023-11-06 14:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Catalog", "0013_alter_discount_end_date_alter_discount_start_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="discount",
            name="end_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 6, 15, 33, 45, 923247)
            ),
        ),
        migrations.AlterField(
            model_name="discount",
            name="start_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 6, 15, 33, 45, 923247)
            ),
        ),
    ]