from django.urls import path
from . import views

urlpatterns = [
	path('', views.main_page_view, name='main_page'),
	path('shop_grid/', views.shop_grid_view, name='shop_grid'),
	path('contact/', views.contact_view, name='contact'),
	path('social_networks/', views.social_networks_view, name='social_networks'),
	path('<slug:slug>/', views.product_detail_view, name='product_detail'),
]