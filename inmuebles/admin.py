from django.contrib import admin
from .models import Inmueble, Region, Comuna


class InmuebleAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "comuna",
        "tipo_inmueble",
        "habitaciones",
        "banos",
        "precio_mensual",
    )

    search_fields = (
        "nombre",
        "descripcion",
        "comuna",
        "tipo_inmueble",
    )

    list_filter = (
        "comuna",
        "tipo_inmueble",
        "habitaciones",
        "banos",
    )


admin.site.register(Inmueble, InmuebleAdmin)
admin.site.register(Region)
admin.site.register(Comuna)