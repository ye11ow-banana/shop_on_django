# Generated by Django 3.0.6 on 2020-08-22 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_color_class_for_css'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price_with_sale',
            field=models.PositiveIntegerField(default=0, help_text='Указывать в долларах', verbose_name='Стоимость со скидкой'),
        ),
    ]
