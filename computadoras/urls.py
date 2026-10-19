from django.urls import path
from . import views

app_name = "computadoras"

urlpatterns = [
    # Visualizar (Listado)
    path("", views.SupercomputadoraListView.as_view(), name="lista"),
    # Visualizar (Detalle individual)
    path("<int:pk>/", views.SupercomputadoraDetailView.as_view(), name="detalle"),
    # Agregar
    path("nueva/", views.SupercomputadoraCreateView.as_view(), name="crear"),
    # Editar
    path("<int:pk>/editar/", views.SupercomputadoraUpdateView.as_view(), name="editar"),
    # Borrar
    path("<int:pk>/eliminar/", views.SupercomputadoraDeleteView.as_view(), name="eliminar"),
    # Autologin admin preview
    path("auto-admin/", views.auto_login_admin, name="auto_admin"),
]
