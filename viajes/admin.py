from django.contrib import admin
from .models import Destino


@admin.register(Destino)
class DestinoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "pais", "ciudad", "precio", "dias", "destacado")
    list_filter = ("pais", "destacado")
    search_fields = ("nombre", "pais", "ciudad", "descripcion")