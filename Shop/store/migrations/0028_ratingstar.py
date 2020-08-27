# Generated by Django 3.0.6 on 2020-08-26 09:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0027_reviews_pub_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.PositiveSmallIntegerField(verbose_name='количество звезд рейтинга')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Product', verbose_name='продукт')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
        ),
    ]
