<<<<<<< HEAD
from django.http import HttpResponse
from django.views.generic import ListView
from .models import models_


class ModelPrincipalBasedView(ListView):
    model = models_.ModelVaccine
    template_name = 'app/index.html'
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> f0fe4c1 (Initial)
