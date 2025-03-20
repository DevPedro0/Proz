from django.db import models
from validate_docbr import CNPJ
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# Foreing Key Class
class ModelForeingKeyVaccine(models.Model):
    ...



class EnderecoModel(models.Model):
    ...

# Model Vaccine

class ModelVaccine(models.Model):
    ...

# Models App User
class CNPJField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 18)
        kwargs.setdefault('validators', [
            RegexValidator(
                regex=r'^\d{2}.\d{3}.\d{3}/\d{4}-\d{2}',
                message='Formato Inválido, Use: 00.000.000/0000-00 '
            )
        ])
        super().__init__(*args, **kwargs)
        

    
class ModelUser(models.Model):
    # Dados Usuário
    user = models.ForeignKey(
        to = User,
        on_delete=models.CASCADE
    )
    
    # Dados Orgs
    
    cnpj = CNPJField(primary_key=True)
    name = models.CharField(max_length=100)
    endereco = models.ForeignKey(
        to = EnderecoModel,
        on_delete=models.SET_NULL,
        null=True, 
        blank=True
    )
    
    
    def __str__(self):
        return f'{self.user.first_name} - {self.user.last_name} - {self.cnpj}'
    
    
    