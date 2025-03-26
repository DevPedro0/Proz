from django.db import models
from django.contrib.auth.models import User
from .lists import ESTADOS

ESTADOS = ()

class AuthorForeingKeyModelNews(models.Model):
    name = models.CharField(max_length=100)

class LocalModel(models.Model):
    
    estado = models.CharField(
        choices = ESTADOS,
        max_length=20
    )

    def __str__(self):
        test = [item[-1] for item in ESTADOS if (item[0] == self.estado)]
        
        return f'{self.estado} - {test[:]}'
    
class ThemeModel(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class ModelDataNews(models.Model):
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=25, null=True, blank=True)
    description = models.TextField(max_length=255)
    post = models.BooleanField(default=False)
    
    image = models.ImageField(
        upload_to= f'image/src/',
    )
    
    data_published = models.DateTimeField(auto_now_add=True)
    data_actualizer = models.DateTimeField(auto_now=True)
    
    # Foreing Keys Model
    author = models.ForeignKey(
<<<<<<< HEAD
        to = AuthorForeingKeyModelNews,
=======
        to = User,
>>>>>>> 1bdfcf6cba3429de99a1acc1d8bd0e9b8819edac
        on_delete=models.CASCADE,
    )
    
    local = models.ForeignKey(
        to = LocalModel,
        on_delete=models.CASCADE
    )
    
    tema = models.ForeignKey(
        to = ThemeModel,
        on_delete=models.CASCADE
    )
<<<<<<< HEAD

class VaccineModel(models.Model):
    ...
=======
    
    
>>>>>>> 1bdfcf6cba3429de99a1acc1d8bd0e9b8819edac
