from django.shortcuts import render, redirect
from django.http import Http404
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
        
    return redirect('authors:register-form')