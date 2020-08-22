from . import views
from .models import Product, Department, Advert, Wish, Color, Gallery, Reviews
from Shop.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

products = Product.objects.all().filter(draft=False)
departments = Department.objects.all()
advert = Advert.objects.all()[0]
colors = Color.objects.all()
reviews = Reviews.objects.all()

def get_reviews_for_product(product):
	return reviews.filter(
		product=product)


def get_object_product_from_str(product: str):
	print(products.filter(url=product))
	return products.filter(url=product)[0]


def get_photos_for_product(product) -> list:
	return Gallery.objects.all().filter(
		product=product)


def get_ip(request) -> str:
	'''возвращает ip пользователя'''
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')
	return ip

def change_wish_list_of_user(request, pk: int) -> None:
	if Wish.objects.filter(item=pk):
		Wish.objects.filter(item=pk).delete()
	else:
		wish = Wish.objects.create(user=request.user)
		wish.item.add(pk)


def change_wish_list(request, pk: int) -> None:
	if Wish.objects.filter(item=pk):
		Wish.objects.filter(item=pk).delete()
	else:
		wish = Wish.objects.create(ip=get_ip(request))
		wish.item.add(pk)				
		

def count_wishes(request) -> int:
	if request.user.is_authenticated:
		return len(Wish.objects.filter(user=request.user))
	else:
		return len(Wish.objects.filter(ip=get_ip(request)))


def get_most_expensive_and_cheapest_price() -> list:
	'''Высчитывает самую большую и самую маленькую цены'''
	most_expensive = 0
	the_cheapest = 1000
	for product in products:
		price = product.price

		if product.price_with_sale:
			price = product.price_with_sale

		if most_expensive < price:
			most_expensive = price

		if the_cheapest > price:
			the_cheapest = price	

	return [most_expensive, the_cheapest]


def send_to_mail_message_from_user(email: str, 
	name: str, message: str) -> None:
	'''Отправляет сообщение пользователя админу'''
	send_mail(email + ' - ' + name, 
		message, 
		EMAIL_HOST_USER, [EMAIL_HOST_USER]
	)


def get_similar_products(product_obj) -> list:
	similar_products = []

	for product in products.filter(
		department=product_obj.department):
		if product != product_obj:
			similar_products.append(product)

	return similar_products