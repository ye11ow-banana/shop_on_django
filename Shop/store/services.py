from .models import (
	Product, Department, Advert, Wish, 
	Color, Gallery, Reviews, Like, Dislike
)
from Shop.settings import EMAIL_HOST_USER
from django.core.mail import send_mail


products = Product.objects.all().filter(
	draft=False).order_by('-pub_date')
departments = Department.objects.all()
advert = Advert.objects.all()[0]
colors = Color.objects.all()
galleries = Gallery.objects.all()
reviews = Reviews.objects.all()
wishes = Wish.objects.all()


def add_dislike(user, id: int) -> None:  # !
	review = reviews.filter(id=id)[0]

	try:
		like = Like.objects.filter(user=user, review=review)
		dislike = Dislike.objects.filter(user=user, review=review)

		if like:
			like.delete()
			review.quantity_of_likes -= 1

		if dislike:
			dislike.delete()
			review.quantity_of_dislikes -= 1
		else:
			dislike.create(user=user, review=review)
			review.quantity_of_dislikes += 1

		review.save()

	except TypeError:
		pass


def add_like(user, id: int) -> None:  # !
	review = reviews.filter(id=id)[0]

	try:
		like = Like.objects.filter(user=user, review=review)
		dislike = Dislike.objects.filter(user=user, review=review)

		if dislike:
			dislike.delete()
			review.quantity_of_dislikes -= 1

		if like:
			like.delete()
			review.quantity_of_likes -= 1
		else:
			like.create(user=user, review=review)
			review.quantity_of_likes += 1

		review.save()

	except TypeError:
		pass


def add_review(request, product) -> None:  # !
	
	try:
		Reviews.objects.create(
			text=request.POST.get('text'), 
			product=product, user=request.user
		)

	except TypeError:
		print('Попытка взлома!')


def get_ip(request) -> str:  # !
	'''возвращает ip пользователя'''
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')
	return ip


def change_wish_list_of_user(user, id: int) -> None:  # !
	try:
		wishes.filter(item=id).delete()

	except ValueError:
		wishes.create(user=user).item.add(id)


def change_wish_list_of_anonymous(request, id: int) -> None:  # !
	try:
		wishes.filter(item=id).delete()

	except ValueError:
		wishes.create(ip=get_ip(request)).item.add(id)				
		

def count_wishes(request) -> int:  # !
	try:
		return len(wishes.filter(user=request.user))

	except TypeError:
		return len(wishes.filter(ip=get_ip(request)))		


def get_most_expensive_and_cheapest_price() -> list:  # !
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
	name: str, message: str) -> None:  # !
	'''Отправляет сообщение пользователя админу'''
	send_mail(email + ' - ' + name, 
		message, 
		EMAIL_HOST_USER, [EMAIL_HOST_USER]
	)


def get_similar_products(product_obj) -> list:  # !
	similar_products = []

	for product in products.filter(
		department=product_obj.department):
		if product != product_obj:
			similar_products.append(product)

	return similar_products


def get_model_object_of_product(argument):  # !
	try:
		return Product.objects.get(id=argument)
	except ValueError:
		pass

	try:
		return products.filter(url=argument)[0]
	except ValueError:
		pass

	
def add_to_list(objects: list) -> list:  # !
	feel_list = []
	for obj in objects:
		feel_list.append(obj.review)

	return feel_list


def add_to_like_list(request):   # !
	try:
		return add_to_list(Like.objects.filter(
			user=request.user))		
	except TypeError:
		pass


def add_to_dislike_list(request):  # !		
	try:
		return add_to_list(Dislike.objects.filter(
			user=request.user))	
	except TypeError:
		pass
