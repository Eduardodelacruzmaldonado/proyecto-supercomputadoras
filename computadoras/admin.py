from django.contrib import admin
from .models import Supercomputadora


@admin.register(Supercomputadora)
class SupercomputadoraAdmin(admin.ModelAdmin):
    list_display = (
        "ranking_posicion",
        "nombre",
        "pais_origen",
        "numero_cores",
        "ram_tb",
        "almacenamiento_tb",
        "teraflops",
        "sistema_operativo",
    )
    list_display_links = ("nombre",)
    list_filter = ("pais_origen", "sistema_operativo")
    search_fields = ("nombre", "pais_origen", "sistema_operativo", "fabricante")
    ordering = ("-teraflops", "ranking_posicion")
    readonly_fields = ("fecha_registro", "fecha_actualizacion")
    fieldsets = (
        (
            "Identificación",
            {
                "fields": (
                    "nombre",
                    "ranking_posicion",
                    "pais_origen",
                    "institucion",
                    "fabricante",
                )
            },
        ),
        (
            "Especificaciones Técnicas (Requeridas)",
            {
                "fields": (
                    "numero_cores",
                    "ram_tb",
                    "almacenamiento_tb",
                    "teraflops",
                    "sistema_operativo",
                )
            },
        ),
        (
            "Metadatos del Sistema",
            {
                "classes": ("collapse",),
                "fields": ("fecha_registro", "fecha_actualizacion"),
            },
        ),
    )
