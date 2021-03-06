from django.shortcuts import render, redirect 
from . import services 
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def main_page_view(request):
	'''Рендерит главную страницу'''	
	return render(request, 'index.html', 
		{
			'products': services.products,
			'departments': services.departments,
			'advert': services.advert,
			'quantity_of_hearts': len(services.wishes_of_user(request)),
			'wishes_of_user': services.wishes_of_user(request),
		})


def product_detail_view(request, product: str):
	'''Рендерит страницу деталей конкретного продукта'''
	product = services.get_model_object_of_product(product)

	return render(request, 'shop-details.html',
		{
			'product': product,
			'departments': services.departments,
			'photos': services.galleries.filter(product=product),
			'quantity_of_hearts': len(services.wishes_of_user(request)),	
			'similar_products': services.get_similar_products(product),
			'reviews': services.reviews.filter(product=product),
			'liked': services.add_to_like_list(request),
			'disliked': services.add_to_dislike_list(request),
			'wishes_of_user': services.wishes_of_user(request),
		})


def add_dislike_view(request, id: int):
	if request.method == 'POST':
		services.add_dislike(request.user, id)

	return redirect(request.POST.get('path'))


def add_like_view(request, id: int):
	if request.method == 'POST':
		services.add_like(request.user, id)

	return redirect(request.POST.get('path'))


def add_answer_view(request, id: int, pk: int):
	if request.method == 'POST':
		services.add_review(request, 
			services.get_model_object_of_product(id), pk)

	return redirect(request.POST.get('path'))


def add_review_view(request, id: int):
	if request.method == 'POST':
		services.add_review(request, 
			services.get_model_object_of_product(id))

	return redirect(request.POST.get('path'))


def remove_review_view(request, id: int):
	if request.method == 'POST':
		services.delete_review(id)

	return redirect(request.POST.get('path'))


def change_review_view(request, id: int):
	if request.method == 'POST':
		reviews = services.reviews.filter(id=id)[0]
		reviews.text = request.POST.get('text')
		reviews.save()

	return redirect(request.POST.get('path'))


def change_wish_list_view(request, id: int):
	if request.method == 'POST':
		services.change_wish_list(
			request, services.get_model_object_of_product(id))

	return redirect(request.POST.get('path'))


def shop_grid_view(request):
	'''Рендерит страницу с товарами'''
	page = request.GET.get('page', 1)

	paginator = Paginator(services.products, 4)

	try:
		paginated_products = paginator.page(page)
	except PageNotAnInteger:
		paginated_products = paginator.page(1)
	except EmptyPage:
		paginated_products = paginator.page(paginator.num_pages)

	return render(request, 'shop-grid.html', 
		{
			'products': services.products,
			'paginated_products': paginated_products,
			'most_expensive_price': 
				services.get_most_expensive_and_cheapest_price()[0],  # !
			'the_cheapest_price': 
				services.get_most_expensive_and_cheapest_price()[1],  # !
			'quantity_of_hearts': len(services.wishes_of_user(request)),
			'departments': services.departments,
			'colors': services.colors,
			'wishes_of_user': services.wishes_of_user(request),
		})


def contact_view(request):
	'''Рендерит страницу обратной связи'''
	if request.method == 'POST':
		services.send_to_mail_message_from_user(
			str(request.POST.get('email')), str(request.POST.get('name')), 
			str(request.POST.get('message'))
		)

	return render(request, 'contact.html', {
		'departments': services.departments,
		'quantity_of_hearts': len(services.wishes_of_user(request)),
		'wishes_of_user': services.wishes_of_user(request),
	})


def social_networks_view(request):
	'''Рендерит страницу о том, что нас 
	пока нету в этот соц сети'''
	return render(request, 'social_networks.html', {
		'quantity_of_hearts': len(services.wishes_of_user(request)),
	})


def about_view(request):
	return render(request, 'about.html')


def add_rating_view(request):
	if request.method == 'POST':
		services.add_rating(
			request.user,
			services.get_model_object_of_product(
				request.POST.get('product_id')),
			request.POST.get('stars_quantity')		
		)

	return redirect(request.POST.get('path'))