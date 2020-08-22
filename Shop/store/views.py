from django.urls import reverse
from django.shortcuts import render, redirect 
from . import services
from .models import Reviews


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


def product_detail_view(request, product: str):
	'''Рендерит страницу деталей конкретного продукта'''
	product = services.get_object_product_from_str(product)

	if request.method == 'POST':
		text = request.POST.get('text')
		Reviews.objects.create(text=text, product=product)

	return render(request, 'shop-details.html',
		{
			'product': product,
			'departments': services.departments,
			'photos': services.get_photos_for_product(product),
			'quantity_of_hearts': services.count_wishes(request),
			'similar_products': services.get_similar_products(product),
			'reviews': services.get_reviews_for_product(product),
		})


def shop_grid_view(request):
	'''Рендерит страницу с товарами'''
	return render(request, 'shop-grid.html', 
		{
			'products': services.products.order_by(
				'-pub_date'),
			'most_expensive_price': 
				services.get_most_expensive_and_cheapest_price()[0],
			'the_cheapest_price': 
				services.get_most_expensive_and_cheapest_price()[1],
			'quantity_of_hearts': services.count_wishes(request),
			'departments': services.departments,
			'colors': services.colors,
		})


def contact_view(request):
	'''Рендерит страницу обратной связи'''
	if request.method == 'POST':
		services.send_to_mail_message_from_user(
			str(request.POST.get('email')), str(request.POST.get('name')), 
			str(request.POST.get('message'))
		)
		return render(request, 'contact.html')

	return render(request, 'contact.html', {
		'departments': services.departments,
		'quantity_of_hearts': services.count_wishes(request),
	})


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