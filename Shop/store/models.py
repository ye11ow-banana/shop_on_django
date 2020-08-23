from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Department(models.Model):
    name = models.CharField('Название', max_length=100)
    url = models.SlugField(max_length=130, unique=True)

    def __str__(self):
        return self.name

    class Meta: 
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департаменты'


class Color(models.Model):
    name = models.CharField("Название", max_length=100)
    class_for_css = models.CharField("Название класса для css", max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta: 
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'


class Product(models.Model):
    name = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    img = models.ImageField("Фото", upload_to="store/")
    department = models.ForeignKey(Department, verbose_name="Департамент", on_delete=models.CASCADE)
    sale = models.PositiveIntegerField("Скидка", blank=True, help_text="Percent", null=True)
    price = models.PositiveIntegerField("Цена", default=0, help_text="Указывать в долларах")
    price_with_sale = models.PositiveIntegerField("Стоимость со скидкой", default=0, help_text="Указывать в долларах")
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("Черновик", default=False)
    color = models.ManyToManyField(Color, verbose_name='Цвет')
    weight = models.PositiveIntegerField('Масса', help_text='Указывать в килограммах')
    quantity = models.PositiveIntegerField('Количество')
    wishes = models.BooleanField("Желания", default=False)
    class_for_css = models.CharField("Название класса для css", max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'product': self.url})

    class Meta: 
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Gallery(models.Model):
    '''Список фотографий для деталий продукта'''
    img = models.ImageField(upload_to='gallery')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='Фотографии')

    class Meta: 
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'


class Reviews(models.Model):
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    product = models.ForeignKey(Product, verbose_name="продукт", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="пользователь", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.product}"


    class Meta: 
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class News(models.Model):
    email = models.EmailField()

    class Meta: 
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'


class Advert(models.Model):
    title = models.CharField('Название', max_length=100)
    text = models.TextField("Описание", max_length=1000)
    img = models.ImageField(upload_to='store')

    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = 'Реклама'
        verbose_name_plural = 'Рекламы'


class Coupon(models.Model):
    '''Промокод для скидки'''
    # username = models.ManyToManyField(User, verbose_name='Username', blank=True, null=True)
    # title_of_coupon = models.CharField('Title', max_length=100)
    name = models.CharField('Название', max_length=100)
    sale = models.PositiveIntegerField("Sale", blank=True, help_text="Процент", null=True)

    def get_sale(self, old_price):
        '''Расчитать стоимость со скидкой'''
        if str(type(self.sale)) == "<class 'NoneType'>":
            return False
        else:
            price = int(old_price * (100 - self.sale) / 100)
            return price

    class Meta: 
        verbose_name = 'Купон'
        verbose_name_plural = 'Купоны'


class Wish(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    ip = models.GenericIPAddressField(protocol='IPv4', blank=True, null=True)
    item = models.ManyToManyField(Product)

    class Meta:
        verbose_name = 'Список желаний'
        verbose_name_plural = 'Список желаний'