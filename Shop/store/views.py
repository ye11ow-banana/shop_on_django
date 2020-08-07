from django.urls import reverse
from django.shortcuts import render, redirect 
from .models import Product, Department, Advert


products_all = Product.objects.all()
departments = Department.objects.all()
adverts = Advert.objects.all()

def show_product_list_view(request):
	"""Рендерит продукты для главной страницы"""
	top_slider_products = products_all.filter(draft=False).order_by('-pub_date')[:5]
	# featured_products = FeaturedProduct

	return render(request, 'index.html',
				{
					'top_slider_products': top_slider_products,
					# 'featured_products': featured_products.featured_products,
					'departments': departments,
					'adverts': adverts,
					'user': request.user,
				})


def show_product_detail_view(request, slug):
	"""Рендерит страницу деталей конкретного продукта"""
	product = Product.objects.get(url=slug)

	return render(request, 'store/shop-details.html',
			{
				'product': product,
			})	

def show_checkout(request):
	"""Рендерит страницу с оплатой"""
	return render(request, 'store/checkout.html')
    
def show_shoping_cart(request):
	"""Рендерит страницу с товарами, которые хочет купить пользователь"""
	return render(request, 'store/shoping-cart.html')


def show_shop_grid(request):
	"""Рендерит страницу с товарами"""
	return render(request, 'store/shop-grid.html')

     