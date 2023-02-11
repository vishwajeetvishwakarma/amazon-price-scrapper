# Generated by Django 4.1.6 on 2023-02-11 07:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0002_alter_product_current_price_alter_product_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='current_price',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='data',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 11, 13, 10, 15, 782105), null=True),
        ),
    ]
