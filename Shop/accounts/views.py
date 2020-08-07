from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse
from django.shortcuts import render, redirect 

from .forms import RegistrationForm, ProfileForm
from . import services


def register_view(request):
	'''Регистрирует пользователя'''
	services.get_page_or_404(request, False)
	if request.method == 'POST':
		username, email, password, password2 = services.get_all_info_from_form(request)

		if RegistrationForm().is_valid(username, email, password, password2):	
			user = services.create_new_user(username, email, password)	
			services.send_to_mail_generated_code(email, user)
			return redirect(reverse('activation_acc'))

		error_message = services.error[0].error
		services.error.delete()
		return render(request, 'registration/registration_form.html', 
			{'error': error_message})

	return render(request, 'registration/registration_form.html')


def activation_acc_view(request):
	'''Активирует аккаунт пользователя'''
	services.get_page_or_404(request, False)
	if request.method == 'POST':
		code = request.POST.get('code').lstrip(' ').rstrip(' ')

		if services.check_code(code):
			user = services.get_user_from_code(code)
			user.is_active = True
			user.save()
			return redirect(reverse('login'))

		return render(request, 'registration/activation_account.html', 
			{'error': '*you\'ve typed non-exist code⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'})

	return render(request, 'registration/activation_account.html')


def login_view(request):
	'''Логинит пользователя'''
	print(request.path)
	services.get_page_or_404(request, False)
	if request.method == 'POST':
		username_or_email, password = services.get_all_info_from_form(request)
		user_obj = services.get_user_from_username_or_email(username_or_email)

		user = authenticate(request, 
			username=services.get_username_from_email(
				username_or_email), 
			password=password
		)		

		if user_obj.is_active:
			try:
				login(request, user)
				return redirect('/')
			except: 
				return render(request, 'login/login.html', 
					{'error': '*incorrect username or password⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ '})

		return render(request, 'login/login.html', 
			{'error': '*you have to confirm your email⠀to login⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ '})			

	return render(request, 'login/login.html')


def logout_view(request):
	'''Выводит пользователя из учетной записи'''
	services.get_page_or_404(request, True)
	logout(request) 
	return redirect(reverse('product_list'))


def profile_view(request):
	'''Меняет информацию пользователя: его имя, пароль, почту и т. д.'''
	services.get_page_or_404(request, True)
	if request.method == 'POST':
		user_to_change = request.user

		form = services.get_all_info_from_form(request)
		username, email, password, new_password, new_password2 = form

		if ProfileForm().is_valid(username, email, password, 
			new_password, new_password2, user_to_change):				

			user_to_change.set_password(new_password)
			update_session_auth_hash(request, user_to_change)
			user_to_change.username = username
			user_to_change.email = email
			user_to_change.save()
			
			return redirect(reverse('product_list'))


		error_message = services.error[0].error
		services.error.delete()
		return render(request, 'profile/profile.html', {
			'error': error_message})

	return render(request, 'profile/profile.html', {'user': request.user})