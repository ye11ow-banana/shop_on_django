# Generated by Django 3.0.6 on 2020-08-24 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_auto_20200823_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='dislike',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='reviews',
            name='like',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]