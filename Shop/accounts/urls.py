from django.urls import path
from . import views

urlpatterns = [
	path('login/', views.login_view, name='login'),
	path('logout/', views.logout_view, name='logout'),
	path('registration/', views.register_view, name='register'),
	path('registration/activation_account', 
		views.activation_acc_view, name='activation_acc'),
	path('profile/', views.profile_view, name='profile'),
]