from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('computadoras.urls')),
]

# Personalización del título del panel de administración
admin.site.site_header = "Panel de Control - Top Supercomputadoras"
admin.site.site_title = "Supercomputadoras SQLite"
admin.site.index_title = "Gestión de Datos de Supercómputo Concurrente"
