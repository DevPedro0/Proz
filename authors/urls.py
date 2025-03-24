from django.urls import path
from .views import register, register_create

app_name = 'authors'
urlpatterns = [
    path('register/', register, name='register-form'),
    path('register/create/', register_create, name = 'log')
]