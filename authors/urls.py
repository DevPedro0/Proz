from django.urls import path
from . import views

app_name = 'authors'
urlpatterns = [
    path('', views.view_homepage, name='home'),
    path('register/', views.register, name='register-form'),
    path('register/create/', views.register_create, name = 'log'),
    path('login/', views.log, name='page-log-user')
]