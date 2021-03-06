# Generated by Django 3.0.6 on 2020-08-10 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20200810_1248'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name': 'Галерея', 'verbose_name_plural': 'Галереи'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Новости', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterModelOptions(
            name='reviews',
            options={'verbose_name': 'Отзывы', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.AlterField(
            model_name='advert',
            name='text',
            field=models.TextField(max_length=1000, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='advert',
            name='text_en',
            field=models.TextField(max_length=1000, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='advert',
            name='text_ru',
            field=models.TextField(max_length=1000, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='advert',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='advert',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='advert',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='color',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='color',
            name='name_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='color',
            name='name_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='name_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='name_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='sale',
            field=models.PositiveIntegerField(blank=True, help_text='Процент', null=True, verbose_name='Sale'),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='department',
            name='name_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='department',
            name='name_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Фотографии', to='store.Product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.ManyToManyField(to='store.Color', verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='product',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Department', verbose_name='Департамент'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='draft',
            field=models.BooleanField(default=False, verbose_name='Черновик'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(upload_to='store/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(default=0, help_text='Указывать в долларах', verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sale',
            field=models.PositiveIntegerField(blank=True, help_text='Percent', null=True, verbose_name='Скидка'),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.PositiveIntegerField(help_text='Указывать в килограммах', verbose_name='Масса'),
        ),
        migrations.AlterField(
            model_name='product',
            name='wishes',
            field=models.BooleanField(default=False, verbose_name='Желания'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='name_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='name_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Product', verbose_name='продукт'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='text',
            field=models.TextField(max_length=5000, verbose_name='Сообщение'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='text_en',
            field=models.TextField(max_length=5000, null=True, verbose_name='Сообщение'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='text_ru',
            field=models.TextField(max_length=5000, null=True, verbose_name='Сообщение'),
        ),
    ]
