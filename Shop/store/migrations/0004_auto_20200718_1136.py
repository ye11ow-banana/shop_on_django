# Generated by Django 3.0.6 on 2020-07-18 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_wishes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='cart',
        ),
        migrations.AlterField(
            model_name='product',
            name='wishes',
            field=models.BooleanField(default=False, verbose_name='Wishes'),
        ),
    ]
