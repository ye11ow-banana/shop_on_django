from django.contrib.auth.models import User
from Shop.settings import EMAIL_HOST_USER
from random import randint
from django.core.mail import send_mail
from .models import Error
from .models import Code
from django.http import Http404
import webbrowser


error = Error.objects.all().filter(error_id=1)


def send_to_mail_generated_code(email: str, user) -> None:
	'''Генерит код и отправляет его на почту'''
	code = str(randint(1000, 9999))
	Code.objects.create(code=code, user=user)
	send_mail('Account activation', 
		'Code to activate your account: ' + code, 
		EMAIL_HOST_USER, [email]
	)


def get_user_from_code(code: str):
	'''Принимает код, а возвращает юзера-владельца этого кода'''
	user = Code.objects.get(code=code).get_user()
	Code.objects.get(code=code).delete()
	return user


def check_code(code: str) -> bool:
	'''Проверяем код, введеный юзером, 
	с кодом, отправленным на почту'''
	try:
		Code.objects.get(code=code)
		return True
	except: return False


def get_username_from_email(email: str) -> str:
	'''Берет email, а возвращает username'''
	try:
		user = User.objects.get(email=email)
		return user.username
	except:
		return email  # это уже username


def create_new_user(username: str, email: str, password: str):
	'''Создает нового пользователя в бд'''
	user = User.objects.create_user(username, email, password)
	user.is_active = False
	user.save()
	return user


def get_page_or_404(request, is_authenticated_see_page=True) -> None:
	'''Смотря какой is_authenticated_see_page аргумент, 
	функция либо выводит 404 ошибку, либо показывает страницу'''
	if not is_authenticated_see_page:
		if request.user.is_authenticated:
			raise Http404()

	elif is_authenticated_see_page:
		if not request.user.is_authenticated:
			raise Http404()


def get_all_info_from_form(request) -> list:
	'''Возвращает все поля из формы'''
	names_of_field_in_form = [
		'username_or_email', 'username', 'email', 'password',
		'password2', 'new_password', 'new_password2'
	]

	form = []

	for name in names_of_field_in_form:
		try:
			form.append(
				request.POST.get(name).lstrip(' ').rstrip(' ')
			)
		except: pass

	return form


def get_user_from_username_or_email(username_or_email: str):
	'''Возвращет объект пользователя из бд 
	по полю почты или ника'''
	try:
		return User.objects.get(
			username=get_username_from_email(username_or_email)
		)
	except: pass
	

def open_tab_with_site_of_mail_of_user(email_of_user: str) -> None:
	'''Открывает сайт почты пользователя'''
	emails = [
		'mail.ru/', 'inbox.ru/', 'list.ru/', 'bk.ru/',
		'i.ua/', 'ukr.net/', 'gmail.com/', 'yandex.ru/', 
		'yandex.ua/', 'ya.ru/', 'yandex.com/'
	]

	email_of_user = email_of_user[(email_of_user.index('@') + 1):] + '/'

	for email in emails:
		if email == email_of_user:
			webbrowser.open('https://' + email, new=1)
			return None