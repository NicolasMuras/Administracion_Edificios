from django.contrib import admin
from .models import Departamento, Expensas,Edificio
# Register your models here.
admin.site.register(Expensas)
admin.site.register(Edificio)
admin.site.register(Departamento)