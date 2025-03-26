from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path("", views.home_page, name='home'),
    path('user/<int:pk>/', views.filter_user, name='page-user-filter')
]
