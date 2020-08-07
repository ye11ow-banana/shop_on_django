from .validation import CheckValid
from .models import Error


error_instance = Error()


def create_error_if_form_isnt_valid(cheaking_functions: list) -> bool:
	'''Cоздает ошибку, если форма не валидна'''
	for func in cheaking_functions:
		try:
			number_of_error = int(func)
			Error.objects.get_or_create(
				error_id=1, error=error_instance.errors[number_of_error])
			return False		
		except TypeError:
			pass
	return True


class ProfileForm(CheckValid):	
	'''Класс для проверки измененных данных в профиле'''
	def is_valid(self, username: str, email: str, password: str, 
			new_password: str, new_password2: str, user_to_change) -> bool:
		'''Проверяет валидность формы регистрации'''
		cheaking_functions = [
			self.check_username_valid(username), 
			self.is_obj_in_data_for_profile(username, user_to_change),
			self.check_email_valid(email), 
			self.is_obj_in_data_for_profile(email, user_to_change),
			self.check_passwords_right(password, new_password, 
				new_password2, user_to_change)
		]

		return create_error_if_form_isnt_valid(cheaking_functions)


class RegistrationForm(ProfileForm):
	'''Класс для проверки формы регистрации'''
	def is_valid(self, username: str, email: str,
			password: str, password2: str) -> bool:
		'''Проверяет валидность формы регистрации'''
		cheaking_functions = [
			self.check_username_valid(username), 
			self.is_obj_in_data(username),
			self.check_email_valid(email), 
			self.is_obj_in_data(email),
			self.check_password_valid(password, password2)
		]

		return create_error_if_form_isnt_valid(cheaking_functions)

