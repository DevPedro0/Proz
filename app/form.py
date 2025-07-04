from django.forms import ModelForm
from django.contrib.auth.models import User

class FormApp(ModelForm):
    class Meta:
        model = User
        fields = ["email", "password"]