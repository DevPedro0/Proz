from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Class Sub
class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Base(models.Model):
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Criado: {self.create} - Atualizado: {self.update}"

# FK
class Category(models.Model):
    name = models.CharField(max_length=50)
    subCategory = models.ManyToManyField(SubCategory, default="Tudo")
    
    def __str__(self):
        return f"{self.name} - SubCategory: {[i.name for i in self.subCategory.get_queryset()]}"

class TablePromotion(Base):
    number = models.IntegerField(
        validators=[MinValueValidator(0, message="Value Min is 0")]
    )
    juros = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.number}x {"Sem Juros" if self.juros == False else "Com Juros"}"
  
class ImageProduct(Base):
    nameImage = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/")
    
    def __str__(self):
        return f"{self.nameImage}"

# Class Main
  
class Product(Base):
    author = models.ForeignKey(to = User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(decimal_places=2, validators=[MinValueValidator(0, message="Value Min is R$: 00.00")], max_digits=7)
    description = models.CharField(max_length=255)
    textAdd = models.TextField(max_length=255, blank=True, null=True)
    
    urlProduct = models.URLField(unique=True)
    img = models.ForeignKey(ImageProduct, on_delete=models.SET_NULL, null=True, blank=True)
    
    # Novo Valor
    promotion = models.BooleanField(default=False)
    tablePromotion = models.ForeignKey(TablePromotion, on_delete=models.CASCADE)
    avaliacoes = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"{self.author} {self.title} {self.slug} {self.price} {self.description}\
            {self.urlProduct}{self.avaliacoes}{self.category}"