from django.contrib import admin
from .models import Habitacion


class HabitacionAdmin(admin.ModelAdmin):
    list_display = ('numero', 'tipo', 'precio_por_noche', 'descripcion')
    search_fields = ('numero', 'tipo', 'descripcion')
    list_filter = ('precio_por_noche',)

admin.site.register(Habitacion, HabitacionAdmin)