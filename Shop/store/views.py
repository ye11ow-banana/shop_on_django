from django.shortcuts import render
from .services import products, departments, adverts


def main_page_view(request):
	'''Рендерит главную страницу'''
	return render(request, 'index.html', 
		{
			'top_slider_products': products.order_by(
				'-pub_date')[:5],
			'departments': departments,
			'adverts': adverts,
			'user': request.user,
		})


def product_detail_view(request, slug):
	'''Рендерит страницу деталей конкретного продукта'''
	return render(request, 'shop-details.html',
		{
			'products': products.filter(url=slug),
		})


def shop_grid_view(request):
	'''Рендерит страницу с товарами'''
	return render(request, 'shop-grid.html')


def contact_view(request):
	'''Рендерит страницу обратной связи'''
	return render(request, 'contact.html')


def social_networks_view(request):
	'''Рендерит страницу о том, что нас 
	пока нету в этот соц сети'''
	return render(request, 'social_networks.html')