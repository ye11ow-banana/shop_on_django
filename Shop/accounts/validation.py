from django.contrib.auth.models import User


class CheckValid:
	'''Класс хранит в себе методы для проверки валидности формы'''
	def check_unacceptable_symbols(self, word:str, username_or_email:str):
		'''Проверяет слово на наличие символов. Предназначено для почты или логина'''
		symbols = [
			'.', ',', '@', '#', '$', '%', '^', '&', '(',
			')', '=', '+', '[', ']', '{', '}', '"', '<',
			'>', '\\', '\'', '', '/', '?', '`', '~', '|',
			'№', '*', '!'
		]

		if username_or_email == 'username':
			symbols = symbols[-3::-1]
			for symbol in word:
				if symbol in symbols:
					return '0'

		elif username_or_email == 'email':
			symbols = symbols[3:]
			for symbol in word:
				if symbol in symbols:
					return '1' 

	def check_username_valid(self, username:str):
		"""Проверяет логин на валидность"""
		if len(username) < 4:
			return '2' 
		elif len(username) > 50:
			return '3' 
		else:
			if self.check_unacceptable_symbols(username, 'username'):
				return self.check_unacceptable_symbols(username, 'username')

	def check_email_valid(self, email:str):
		"""Проверяет почту на валидность"""
		if '@' in email:
			if self.check_unacceptable_symbols(email, 'email'):
				return self.check_unacceptable_symbols(email, 'email')

	def check_password_valid(self, password:str, password2:str):
		"""Проверяет пароль на валидность"""
		if len(password) < 8:
			return '5' 
		elif len(password) > 50:
			return '4' 
		elif password != password2:
			return '6' 

	def is_obj_in_data(self, obj:str):
		'''
		Проверяет объект на существование в бд. 
		Предназначено для почты или логина'''
		try:
			User.objects.get(username=obj)
			return '7'
		except Exception as e:
			try:
				User.objects.get(email=obj)
				return '8'
			except: return None



