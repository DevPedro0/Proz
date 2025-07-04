from django.urls import path
from .views import homepage, homepageFilter, homepageProductsList, LogUser, homeProducts

app_name = "appHome"
urlpatterns = [
    path("", homepage, name="Home_Page"),
    path("product/", homeProducts, name="ListProducts"),
    path(r"product/<str:products>/", homepageProductsList, name="Home_Products"),
    path(r"product/<str:products>/<int:pk>/", homepageFilter, name="Home_Products_Filters"),
    
    # Page Log In e Sing In
    path("log/", LogUser.as_view()),
    path("sing/", LogUser.as_view()),
    
    # Search
    # path("search/")
]
