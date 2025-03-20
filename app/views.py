from django.http import HttpResponse
from django.views.generic import ListView
from .models import models_


class ModelPrincipalBasedView(ListView):
    model = models_.ModelVaccine
    template_name = 'app/index.html'