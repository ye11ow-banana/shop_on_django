from django.urls import reverse
from django.shortcuts import render, redirect 
from . import services


def main_page_view(request):
	'''Рендерит главную страницу'''	
	return render(request, 'index.html', 
		{
			'top_slider_products': services.products.order_by(
				'-pub_date')[:5],
			'departments': services.departments,
			'advert': services.advert,
			'user': request.user,
			'quantity_of_hearts': services.count_wishes(request),
			'featured_products': services.products,
		})


def product_detail_view(request, slug):
	'''Рендерит страницу деталей конкретного продукта'''
	return render(request, 'shop-details.html',
		{
			'products': services.products.filter(url=slug),
		})


def shop_grid_view(request):
	'''Рендерит страницу с товарами'''
	return render(request, 'shop-grid.html', 
		{
			'products': services.products,
			'quantity_of_hearts': services.count_wishes(request),
		})


def contact_view(request):
	'''Рендерит страницу обратной связи'''
	return render(request, 'contact.html')


def social_networks_view(request):
	'''Рендерит страницу о том, что нас 
	пока нету в этот соц сети'''
	return render(request, 'social_networks.html')


def change_wish_list_view(request):
	if request.method == 'POST':
		pk = request.POST.get('id')
		
		if request.user.is_authenticated:
			services.change_wish_list_of_user(request, pk)
		else:
			services.change_wish_list(request, pk)

		return redirect(request.POST.get('back'))


def about_view(request):
	return render(request, 'about.html')