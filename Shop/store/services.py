from . import views
from .models import Product, Department, Advert


products = Product.objects.all().filter(draft=False)
departments = Department.objects.all()
adverts = Advert.objects.all()


