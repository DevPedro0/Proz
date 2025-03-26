from django.urls import path
from .views import register, register_create, login_, login_create


app_name = 'authors'
urlpatterns = [
    path('register/', register, name='register-form'),
    path('register/create/', register_create, name = 'log'),
    path('login/', login_, name='login-form'),
    path('login/create/', login_create, name = 'log-create'),
]