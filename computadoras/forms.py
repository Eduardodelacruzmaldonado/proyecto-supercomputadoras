from django import forms
from .models import Supercomputadora


class SupercomputadoraForm(forms.ModelForm):
    """
    Formulario basado en modelo (ModelForm) para crear y editar registros
    de Supercomputadoras con estilos Bootstrap 5 y validaciones integradas.
    """

    class Meta:
        model = Supercomputadora
        fields = [
            "nombre",
            "pais_origen",
            "numero_cores",
            "ram_tb",
            "almacenamiento_tb",
            "teraflops",
            "sistema_operativo",
            "fabricante",
            "institucion",
            "ranking_posicion",
        ]
        widgets = {
            "nombre": forms.TextInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "p. ej. El Capitan",
                    "required": True,
                }
            ),
            "pais_origen": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "p. ej. Estados Unidos",
                    "required": True,
                }
            ),
            "numero_cores": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "p. ej. 11340000",
                    "min": "1",
                    "step": "1",
                    "required": True,
                }
            ),
            "ram_tb": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "p. ej. 5437.00",
                    "min": "0.01",
                    "step": "0.01",
                    "required": True,
                }
            ),
            "almacenamiento_tb": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "p. ej. 40000.00",
                    "min": "0.01",
                    "step": "0.01",
                    "required": True,
                }
            ),
            "teraflops": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "p. ej. 1809000.00",
                    "min": "0.01",
                    "step": "0.01",
                    "required": True,
                }
            ),
            "sistema_operativo": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "p. ej. TOSS (Tri-Lab OS / RHEL)",
                    "required": True,
                }
            ),
            "fabricante": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "p. ej. HPE Cray EX255a / AMD Instinct MI300A",
                }
            ),
            "institucion": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "p. ej. Lawrence Livermore National Laboratory (LLNL)",
                }
            ),
            "ranking_posicion": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "p. ej. 1",
                    "min": "1",
                }
            ),
        }
        labels = {
            "nombre": "Nombre de la Supercomputadora",
            "pais_origen": "País de Origen",
            "numero_cores": "Número de Núcleos (Cores)",
            "ram_tb": "Cantidad de Memoria RAM (TB)",
            "almacenamiento_tb": "Capacidad de Almacenamiento (TB)",
            "teraflops": "Rendimiento Teórico / Medido (TeraFLOPS)",
            "sistema_operativo": "Sistema Operativo",
            "fabricante": "Fabricante / Arquitectura (Opcional)",
            "institucion": "Institución o Laboratorio (Opcional)",
            "ranking_posicion": "Posición en TOP500 (Opcional)",
        }
