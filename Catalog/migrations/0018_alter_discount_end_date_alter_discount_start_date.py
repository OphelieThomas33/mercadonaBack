# Generated by Django 4.1 on 2023-11-12 15:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Catalog", "0017_alter_discount_end_date_alter_discount_start_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="discount",
            name="end_date",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="discount",
            name="start_date",
            field=models.DateField(),
        ),
    ]
