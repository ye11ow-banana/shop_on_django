# Generated by Django 3.0.6 on 2020-08-21 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_product_class_for_css'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='img',
            field=models.ImageField(upload_to='store'),
        ),
    ]
