from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from . import forms


def register(request):
    register_form_data = request.session.get('register_form_data', None)
    form = forms.FormsAuthors(register_form_data)
    return render(
        request,
        'register.html',
        context= {
            'form': form
        }
    )
    
def register_create(request):
    if not request.POST:
        raise Http404()
    else:
        POST = request.POST
        request.session['register_form_data'] = POST
        
        form = forms.FormsAuthors(request.POST)
        
    return redirect('authors:page-log-user')

def log(request):
    
    form = forms.FormLogAppHomePage
    # if request.POST:
    #     email = request.POST['email']
    #     password = request.POST['password']
        
    #     log_authenticate = authenticate(
    #         request, 
    #         email = email,
    #         password = password
    #     )
        
    #     if email is not None:
    #         login(
    #             request,
    #             user = log_authenticate
    #         )
            
    #     redirect('authors:')
    # else:
    #     form = forms.FormLogAppHomePage()
        
        
    return render(
        request,
        'log.html',
        context = {
            'form': form
        } 
    )

            
def view_homepage(request):
    form = forms.FormLogAppHomePage
    return render(
        request,
        'log.html',
        context = {
            'form': form
        }
    )