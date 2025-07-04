from django.urls import path
from .views import ProductRecipeView, ProductRecipeViewFilter, APICreateUser

urlpatterns = [
    path("", ProductRecipeView, name="Api-Principal"),
    path("<int:pk>/", ProductRecipeViewFilter, name = "Api-Principal-Filter"),
    # path("") Path para Busca de Produtos com Author, Será Rankeado com Estrelas
    
    # Path para Usuários
    path("user/create/", APICreateUser, name="API_user")
    
]
