from django.urls import path
from . import views

urlpatterns = [
	path('', views.show_product_list_view, name='product_list'),
	path('shoping-cart/', views.show_shoping_cart, name='shoping_cart'),
	path('shop_grid/', views.show_shop_grid, name='shop_grid'),
	path('checkout/', views.show_checkout, name='checkout'),
]