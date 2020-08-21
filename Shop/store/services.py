from . import views
from .models import Product, Department, Advert, Wish


products = Product.objects.all().filter(draft=False)
departments = Department.objects.all()
advert = Advert.objects.all()[0]

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