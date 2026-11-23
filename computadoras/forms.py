from django import forms
from .models import Supercomputadora


class SupercomputadoraForm(forms.ModelForm):
    """
    Formulario basado en el modelo Supercomputadora con validaciones y
    clases de Bootstrap 5 para renderizar campos limpios y responsivos.
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
                    "class": "form-control",
                    "placeholder": "Ej. El Capitan",
                    "required": True,
                }
            ),
            "pais_origen": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej. Estados Unidos",
                    "required": True,
                }
            ),
            "numero_cores": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej. 11340000",
                    "min": "1",
                    "step": "1",
                    "required": True,
                }
            ),
            "ram_tb": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej. 5437.00",
                    "min": "0.01",
                    "step": "0.01",
                    "required": True,
                }
            ),
            "almacenamiento_tb": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej. 40000.00",
                    "min": "0.01",
                    "step": "0.01",
                    "required": True,
                }
            ),
            "teraflops": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej. 1809000.00",
                    "min": "0.01",
                    "step": "0.01",
                    "required": True,
                }
            ),
            "sistema_operativo": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej. TOSS (RHEL-based) / HPE Cray OS",
                    "required": True,
                }
            ),
            "fabricante": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej. HPE Cray EX255a / AMD Instinct MI300A",
                }
            ),
            "institucion": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej. Lawrence Livermore National Laboratory (LLNL)",
                }
            ),
            "ranking_posicion": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej. 1",
                    "min": "1",
                }
            ),
        }
        labels = {
            "nombre": "Nombre de la supercomputadora",
            "pais_origen": "País de origen",
            "numero_cores": "Número de cores",
            "ram_tb": "Cantidad de RAM (TB)",
            "almacenamiento_tb": "Almacenamiento (TB)",
            "teraflops": "Rendimiento (TeraFLOPS)",
            "sistema_operativo": "Sistema operativo",
            "fabricante": "Fabricante / Arquitectura (opcional)",
            "institucion": "Institución o centro (opcional)",
            "ranking_posicion": "Posición en ranking TOP500 (opcional)",
        }
