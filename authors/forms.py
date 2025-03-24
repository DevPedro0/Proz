from django import forms
from django.contrib.auth.models import User

class FormsAuthors(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name', 
            'last_name',
            'username',
            'email',
            'password'
            ]
        
        help_texts = {
            'email': 'Email Válido Por Favor'
        }
        error_messages = {
            'username': {
                'required': 'Campo Obrigatório',
            }
        }
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Placeholder Test'
            }),
            
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Password Here',
                
            })
        }
        
class FormLogAppHomePage(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']