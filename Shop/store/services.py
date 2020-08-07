from django.contrib.auth.models import User
from Shop.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from . import check_valid
from . import views
from random import randint

users = User.objects.all()


def send_mail_or_error(email:str, token:str, user:str) -> None:
    try:
        send_mail('Account verification', 
            'Email confirmation link: http://127.0.0.1:8000/accounts/registration/confirmation/' + token + 'I' + str(user), 
            EMAIL_HOST_USER, [email]
        )
    except Exception as e:
        print(e)
        views.context['error'] = '*you entered a non-existent email⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'


def get_user(user_str:str):
    for user in users:
        if user_str == str(user):
            return user

# def create_code(username):
#     code = str(randint(1000, 9999))
#     CODES[username] = code
#     print(CODES)
#     return code


# def is_code_true(code, username):
#     if CODES[username] == code:
#         return True


# def is_username_in_data(username, user_to_change=''):
#     """Проверяет, есть ли пользователь с таким логином"""
#     for user in users:
#         if not user_to_change:
#             if username == user.username:
#                 views.context['error'] = '*this username is used⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'
#                 return True
#         if username == user.username and username != user_to_change.username:
#             views.context['error'] = '*this username is used⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'
#             return True       


    
# def is_obj_in_data(user_to_change, email='email', username='username'):
#     """Проверяет, есть ли уже такая почта или логин"""
#     for user in users:
#         if email == user.email and email != user_to_change.email:
#             views.context['error'] = '*this email is used⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'
#             return True
#         elif username == user.username and username != user_to_change.username:
#             views.context['error'] = '*this username is used⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'
#             return True

# User.objects.get(username=username)

def is_obj_in_data(obj):
    try:
        User.objects.get(username=obj)
        views.context['error'] = '*this username is used⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'
        return True
    except:
        try:
            User.objects.get(email=obj)
            views.context['error'] = '*this email is used⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'
            return True        
        except:
            return False



def get_username_from_email(username_or_email):
    try:
        user = User.objects.get(email=username_or_email)
        return user.username
    except:
        return username_or_email       


def get_email_from_username(username_or_email):    
    try:
        user = User.objects.get(username=username_or_email)
        return user.email
    except:
        return username_or_email

