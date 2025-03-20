from django.contrib import admin
from app.models import models_ as m
from app.models import modelsNews as mn

class RegisterModelAdmin(admin.ModelAdmin):
    ...
    
admin.site.register(m.ModelUser,RegisterModelAdmin)


class RegisterModelNewsAdmin(admin.ModelAdmin):
    ...
    
admin.site.register(mn.ModelDataNews, RegisterModelNewsAdmin)
admin.site.register(mn.LocalModel, RegisterModelNewsAdmin)
admin.site.register(mn.ThemeModel, RegisterModelNewsAdmin)