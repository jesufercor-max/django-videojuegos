from django.contrib import admin

# Register your models here.
from .models import Juego, Plataforma, Desarrolladora
admin.site.register(Juego)
admin.site.register(Plataforma)
admin.site.register(Desarrolladora)