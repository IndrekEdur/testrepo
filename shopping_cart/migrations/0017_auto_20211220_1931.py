# Generated by Django 3.2.5 on 2021-12-20 17:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0016_auto_20211218_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopping_cart',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 20, 19, 31, 31, 511921)),
        ),
        migrations.AlterField(
            model_name='shopping_cart_item',
            name='added_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 20, 19, 31, 31, 512909)),
        ),
    ]