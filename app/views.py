from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Product
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth.models import User
from .form import FormApp

def homepage(request):
    form = FormApp
    
    return render(
        request, 
        template_name="global/Log.html", 
        context={"form": form}
    )
def homeProducts(request):
    product = Product.objects.all()
    return render(
        request, 
        template_name="global/homepage.html", 
        context={"product": product})

def homepageProductsList(request, products):
    product = get_list_or_404(
        Product.objects.filter(category__name = products),    
    )
    return render(
        request, 
        template_name="global/test.html", 
        context={"product": product})

def homepageFilter(request, products:str, pk):
    product = get_object_or_404(
        Product.objects.filter(pk = pk),    
    )
    return render(
        request, 
        template_name="global/product.html", 
        context={"product": product }
    )

class LogUser(TemplateView):
    template_name = r"global/Log.html"
    