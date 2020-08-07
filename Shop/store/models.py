from django.db import models
from django.urls import reverse


class Department(models.Model):
    name = models.CharField('Title', max_length=100)
    url = models.SlugField(max_length=130, unique=True)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField("Title", max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField("Title", max_length=100)
    description = models.TextField("Description")
    img = models.ImageField("Image", upload_to="store/")
    department = models.ForeignKey(Department, verbose_name="Department", on_delete=models.CASCADE)
    sale = models.PositiveIntegerField("Sale", blank=True, help_text="Percent", null=True)
    price = models.PositiveIntegerField("Price", default=0, help_text="Indicate the amount in dollars")
    pub_date = models.DateTimeField('Published date', auto_now_add=True)
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("Draft", default=False)
    color = models.ManyToManyField(Color, verbose_name='Color')
    weight = models.PositiveIntegerField('Weight', help_text='Indicate mass in kilograms')
    quantity = models.PositiveIntegerField('Quantity')
    wishes = models.BooleanField("Wishes", default=False)

    def get_sale(self):
        '''Расчитать стоимость со скидкой'''
        if str(type(self.sale)) == "<class 'NoneType'>":
            return False
        else:
            price = self.price * ((100 - self.sale) / 100)
            return price

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.url})


class Gallery(models.Model):
    '''Список фотографий для деталий продукта'''
    img = models.ImageField(upload_to='gallery')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

    class Meta: 
        verbose_name = 'Gellery'
        verbose_name_plural = 'Gelleries'


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField("Name", max_length=100)
    text = models.TextField("Message", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    product = models.ForeignKey(Product, verbose_name="product", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.product}"


    class Meta: 
        verbose_name = 'Reviews'
        verbose_name_plural = 'Reviews'


class News(models.Model):
    email = models.EmailField()

    class Meta: 
        verbose_name = 'News'
        verbose_name_plural = 'News'


class Advert(models.Model):
    title = models.CharField('Title', max_length=100)
    text = models.TextField("Description", max_length=1000)
    img = models.ImageField(upload_to='adverts')

    def __str__(self):
        return self.title


class Coupon(models.Model):
    '''Промокод для скидки'''
    # username = models.ManyToManyField(User, verbose_name='Username', blank=True, null=True)
    # title_of_coupon = models.CharField('Title', max_length=100)
    name = models.CharField('Title', max_length=100)
    sale = models.PositiveIntegerField("Sale", blank=True, help_text="Percent", null=True)

    def get_sale(self, old_price):
        '''Расчитать стоимость со скидкой'''
        if str(type(self.sale)) == "<class 'NoneType'>":
            return False
        else:
            price = int(old_price * (100 - self.sale) / 100)
            return price


# class Profile(models.Model):
#     username = models.OneToOneField(settings.AUTH_USER_MODEL)

#     def __str__(self):
#         return 'Profile for user {}'.format(self.user.username)


# class Wish(models.Model):
#     customer = models.GenericIPAddressField()
#     ip = models.GenericIPAddressField()
#     item = models.ForeignKey(Product)

#     class Meta:
#         unique_together = ['customer', 'item']


