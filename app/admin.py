from django.contrib import admin
from .models import ImageProduct, TablePromotion, Product, Category, SubCategory

class AdminModelsAPP(admin.ModelAdmin):
    ...
    
admin.site.register(Product, AdminModelsAPP)
admin.site.register(ImageProduct, AdminModelsAPP)
admin.site.register(TablePromotion, AdminModelsAPP)
admin.site.register(Category, AdminModelsAPP)
admin.site.register(SubCategory, AdminModelsAPP)