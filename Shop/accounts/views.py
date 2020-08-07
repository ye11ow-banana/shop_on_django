from django.contrib.auth import authenticate, login, logout  
from django.urls import reverse
from django.shortcuts import render, redirect 

from .forms import RegistrationForm
from . import services


def register_view(request):
	'''Регистрирует пользователя'''
	services.get_page_or_404(request, False)
	if request.method == 'POST':
		username, email, password, password2 = services.get_all_info_from_form(request)
		# username = request.POST.get('username').lstrip(' ').rstrip(' ')
		# email = request.POST.get('email').lstrip(' ').rstrip(' ')
		# password = request.POST.get('password').lstrip(' ').rstrip(' ')
		# password2 = request.POST.get('password2').lstrip(' ').rstrip(' ')

		if RegistrationForm().is_valid(username, email, password, password2):	
			user = services.create_new_user(username, email, password)	
			services.send_to_mail_generated_code(email, user)
			return redirect(reverse('activation_acc'))

		try:
			error_message = services.error[0].error
			services.error.delete()
			return render(request, 'registration/registration_form.html', 
				{'error': error_message})
		except:
			return render(request, 'registration/registration_form.html', 
				{'error': False})

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
	return redirect('/')

def send_link_to_email_view(request):
	"""Отправляет на почту ссылку на сброс пароля"""
	if request.method == 'POST':
		services.username_or_email(request)


	return render(request, 'accounts/1_step-type_email.html', context)


def change_password_view(request):
	"""Меняет пароль пользователя"""
# token = default_token_generator.make_token(user)
	if request.method == 'POST':
		password = request.POST.get('password').lstrip(' ').rstrip(' ')
		password2 = request.POST.get('password2').lstrip(' ').rstrip(' ') 
		if services.is_password_valid(password, password2):
			u = User.objects.get(email=email) 
			u.set_password(password)
			u.save()                 
			return redirect(reverse('login'))

	return render(request, 'accounts/2_step-type_new_password', context)


def change_info_of_user_view(request):
	"""Меняет информацию пользователя: его имя, пароль, почту и т. д."""
	if request.method == 'POST':
		user_to_change = request.user
		username = request.POST.get('username').lstrip(' ').rstrip(' ')
		email = request.POST.get('email').lstrip(' ').rstrip(' ')

		if  check_valid.is_username_valid(username) and \
			check_valid.is_email_valid(email):

			# context['error'] = '*account with this email does not exist' 
			user_to_change.username = username
			user_to_change.email = email
			user_to_change.save()

			return redirect(reverse('product_list'))

	else:
		services.get_page_or_404(request, True)

		return render(request, 'accounts/profile.html', {'user': request.user})

	return render(request, 'accounts/profile.html', context)        