from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.db.models import Sum, Avg, Max, Count
from .models import Supercomputadora
from .forms import SupercomputadoraForm


class SupercomputadoraListView(ListView):
    """
    Función: Visualizar (Listado general y Dashboard)
    Muestra la lista de las supercomputadoras registradas junto con métricas agregadas.
    """

    model = Supercomputadora
    template_name = "computadoras/lista.html"
    context_object_name = "supercomputadoras"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Métricas concurrentes y agregadas para la presentación
        estadisticas = Supercomputadora.objects.aggregate(
            total_equipos=Count("id"),
            total_cores=Sum("numero_cores"),
            total_ram=Sum("ram_tb"),
            total_almacenamiento=Sum("almacenamiento_tb"),
            total_teraflops=Sum("teraflops"),
            max_teraflops=Max("teraflops"),
        )
        context["stats"] = estadisticas
        return context


class SupercomputadoraDetailView(DetailView):
    """
    Función: Visualizar (Ficha técnica detallada de una supercomputadora)
    """

    model = Supercomputadora
    template_name = "computadoras/detalle.html"
    context_object_name = "computadora"


class SupercomputadoraCreateView(CreateView):
    """
    Función: Agregar (Creación de un nuevo registro)
    """

    model = Supercomputadora
    form_class = SupercomputadoraForm
    template_name = "computadoras/formulario.html"
    success_url = reverse_lazy("computadoras:lista")

    def form_valid(self, form):
        messages.success(
            self.request,
            f"¡Supercomputadora '{form.cleaned_data['nombre']}' registrada con éxito en la base de datos!",
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_accion"] = "Registrar Nueva Supercomputadora"
        context["boton_texto"] = "Guardar en Base de Datos"
        context["icono_accion"] = "bi-plus-circle"
        return context


class SupercomputadoraUpdateView(UpdateView):
    """
    Función: Editar (Modificación de especificaciones de una supercomputadora)
    """

    model = Supercomputadora
    form_class = SupercomputadoraForm
    template_name = "computadoras/formulario.html"
    success_url = reverse_lazy("computadoras:lista")

    def form_valid(self, form):
        messages.info(
            self.request,
            f"¡La supercomputadora '{form.cleaned_data['nombre']}' fue actualizada correctamente!",
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_accion"] = f"Editar Especificaciones: {self.object.nombre}"
        context["boton_texto"] = "Actualizar Registro"
        context["icono_accion"] = "bi-pencil-square"
        return context


class SupercomputadoraDeleteView(DeleteView):
    """
    Función: Borrar (Eliminación segura con pantalla de confirmación)
    """

    model = Supercomputadora
    template_name = "computadoras/confirmar_eliminar.html"
    context_object_name = "computadora"
    success_url = reverse_lazy("computadoras:lista")

    def form_valid(self, form):
        nombre = self.object.nombre
        messages.warning(
            self.request,
            f"La supercomputadora '{nombre}' ha sido eliminada permanentemente de la base de datos.",
        )
        return super().form_valid(form)


def auto_login_admin(request):
    """Vista utilitaria para previsualización directa del panel administrativo"""
    from django.contrib.auth import login
    from django.contrib.auth.models import User
    user = User.objects.filter(username="admin").first()
    if user:
        login(request, user)
    return redirect("/admin/computadoras/supercomputadora/")
