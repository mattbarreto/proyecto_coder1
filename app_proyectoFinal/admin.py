from django.contrib import admin
from app_proyectoFinal.models import Atleta, Avatar, Entrenador, Rutina

# Register your models here.

admin.site.register(Atleta)
admin.site.register(Entrenador)
admin.site.register(Rutina)
admin.site.register(Avatar)