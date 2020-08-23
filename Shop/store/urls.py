from django.urls import path
from . import views

urlpatterns = [
	path('', views.main_page_view, name='main_page'),
	path('shop_grid/', views.shop_grid_view, name='shop_grid'),
	path('contact/', views.contact_view, name='contact'),
	path('about/', views.about_view, name='about'),
	path('social_networks/', views.social_networks_view, name='social_networks'),
	path('change_wish_list/', views.change_wish_list_view, name='change_wish_list'),
	path('add_review/<int:id>/', views.add_review_view, name='add_review'),
	path('remove_review/<int:id>/', views.remove_review_view, name='remove_review'),
	path('change_review/<int:id>/', views.change_review_view, name='change_review'),
	path('product_detail/<slug:product>/', views.product_detail_view, name='product_detail'),
]