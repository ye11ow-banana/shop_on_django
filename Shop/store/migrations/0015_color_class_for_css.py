# Generated by Django 3.0.6 on 2020-08-22 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_auto_20200821_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='class_for_css',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название класса для css'),
        ),
    ]
