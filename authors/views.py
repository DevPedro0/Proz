from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.contrib import messages
from django.http import Http404
from . import forms


def register(request):
    form = forms.FormsAuthors(request.session.get('register_form_data', None))
    return render(request, 'register.html', {'form': form})
    
def register_create(request):
    if request.method != 'POST':
        return redirect('authors:register-form')

    request.session['register_form_data'] = request.POST
    form = forms.FormsAuthors(request.POST)
    
    if form.is_valid():
        form.save()
        messages.success(request, 'Your user is created, please log in.')
        request.session.pop('register_form_data', None)  # Evita exceção

        return redirect('authors:login-form')  # Redireciona direto para o login
    
    return redirect('authors:register-form')

def login_(request):
    return render(request, 'log.html', {
        'form': forms.LoginForm(),
        'form_action': reverse('authors:log-create'),
    })

def login_create(request):
    if not request.POST:
         raise Http404()
 
    form = forms.LoginForm(request.POST)
    login_url = reverse('authors:login-form')

    if form.is_valid():
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )

        if authenticated_user is not None:
            messages.success(request, 'Your are logged in.')
            login(request, authenticated_user)
            return redirect('app:home')
        else:
            messages.error(request, 'Invalid credentials')
            return Http404("Forms Log Not Found")
    else:
<<<<<<< HEAD
        messages.error(request, 'Invalid username or password')

    return redirect(login_url)
=======
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
>>>>>>> 1bdfcf6cba3429de99a1acc1d8bd0e9b8819edac
