from django.contrib.auth.models import User
from django.db import models


class Error(models.Model):
	'''Предназначена для проверки валидности формы'''
	error_id = models.PositiveIntegerField(primary_key=True)
	error = models.CharField('error', max_length=300)

	errors = [
		'*username has unacceptable symbols⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀',
		'*email has unacceptable symbols⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀', 
		'*username shouldn\'t have less than 4 symbols',
		'*username shouldn\'t have more than 50 symbols',
		'*password shouldn\'t have less than 8 symbol',
		'*password shouldn\'t have more than 50 symbols',
		'*you\'ve typed different passwords⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀',
		'*this username is used⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀',
		'*this email is used⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀',
		'*incorrect password⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'
	]

	def __str__(self):
		return self.error


class Code(models.Model):
	'''Код для верификации пользователя'''
	code = models.CharField('code', max_length=4)
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.code

	def get_user(self):
		return self.user

# '*you entered a non-existent email⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'