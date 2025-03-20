from django.urls import path
from . import views

urlpatterns = [
    path('', views.ModelPrincipalBasedView.as_view())
]
