# Generated by Django 5.1.3 on 2025-02-11 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("carts", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="cart",
            options={"verbose_name": "Корзину", "verbose_name_plural": "Корзина"},
        ),
    ]
