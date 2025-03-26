from . import models
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


def home_page(request):
    if request.user.is_authenticated:
        return render(
            request,
            'app/index.html',
            context={
                'user': request.user
            }
        )
        
    else:
        raise Http404()
    
def filter_user(request, pk):
    filter_user_page = get_object_or_404(User, pk = pk)
    
    if request.user.is_authenticated:
        return render(
            request,
            'app/user.html',
            context={
                'user': filter_user_page
            }
        )
        
    raise Http404()
