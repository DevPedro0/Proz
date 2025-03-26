from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

print(User.objects.all().first())


class FormsAuthors(forms.ModelForm):
    password2 = forms.CharField(
        max_length=255,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': "Verification Password"
            }
        )
    )
    
    cnpj = forms.CharField(
        max_length=18,
        validators=[
            RegexValidator(
                 regex=r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$',
                 message="Format Invalid.  Use: 00.000.000/0000-00"
            )
        ]
    )
    
    class Meta:
        model = User
        fields = [
            'first_name', 
            'last_name',
            'username',
            'email',
            'password',
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
        
    def clean_password(self):
        data = self.cleaned_data.get('password')
        if 'atenção' in data:
            raise ValidationError(
                message='Não Digite "atenção" no Campo',
                code='invalid'
            )
            
        return data
    
    def clean(self):
        cleaned_data = super().clean()
        pass1 = cleaned_data.get('password')
        pass2 = cleaned_data.get('password2')
        
        if pass1 != pass2:
            raise ValidationError({
            'password': 'Password Is Not Equal'
            }
        )

class LoginForm(forms.Form):
 
     username = forms.CharField()
     password = forms.CharField(
         widget=forms.PasswordInput()
     )