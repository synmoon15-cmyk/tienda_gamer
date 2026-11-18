from django.contrib import admin
from .models import Plataforma, Videojuego


@admin.register(Plataforma)
class PlataformaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)


@admin.register(Videojuego)
class VideojuegoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'plataforma', 'precio', 'fecha_lanzamiento', 'disponible')
    list_filter = ('plataforma', 'disponible')
    search_fields = ('titulo',)
