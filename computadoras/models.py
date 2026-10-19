from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator


class Supercomputadora(models.Model):
    """
    Modelo para gestionar la información de las supercomputadoras más rápidas del mundo.
    Cumple estrictamente con los 7 campos solicitados en el proyecto:
    1. Nombre
    2. País de origen
    3. Número de cores
    4. Cantidad de RAM (TB)
    5. Almacenamiento (TB)
    6. TeraFLOPS
    7. Sistema operativo
    """

    nombre = models.CharField(
        max_length=120,
        unique=True,
        verbose_name="Nombre de la supercomputadora",
        help_text="Ejemplo: El Capitan, Frontier, Aurora",
    )

    pais_origen = models.CharField(
        max_length=100,
        verbose_name="País de origen",
        help_text="Ejemplo: Estados Unidos, Japón, China",
    )

    numero_cores = models.PositiveBigIntegerField(
        verbose_name="Número de cores",
        validators=[MinValueValidator(1)],
        help_text="Cantidad total de núcleos de procesamiento (CPU + GPU/aceleradores)",
    )

    ram_tb = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name="Cantidad de RAM (TB)",
        validators=[MinValueValidator(0.01)],
        help_text="Memoria RAM total expresada en Terabytes (TB)",
    )

    almacenamiento_tb = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        verbose_name="Almacenamiento (TB)",
        validators=[MinValueValidator(0.01)],
        help_text="Capacidad de almacenamiento masivo en Terabytes (TB)",
    )

    teraflops = models.DecimalField(
        max_digits=16,
        decimal_places=2,
        verbose_name="Rendimiento (TeraFLOPS)",
        validators=[MinValueValidator(0.01)],
        help_text="Capacidad de cálculo en TeraFLOPS (1 PetaFLOPS = 1,000 TeraFLOPS, 1 ExaFLOPS = 1,000,000 TeraFLOPS)",
    )

    sistema_operativo = models.CharField(
        max_length=150,
        verbose_name="Sistema operativo",
        help_text="Ejemplo: TOSS (RHEL-based), HPE Cray OS, SUSE Linux",
    )

    # Campos complementarios para enriquecer la presentación
    fabricante = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="Fabricante / Arquitectura",
        help_text="Ejemplo: HPE Cray EX255a / AMD Instinct MI300A",
    )

    institucion = models.CharField(
        max_length=180,
        blank=True,
        verbose_name="Institución / Laboratorio",
        help_text="Ejemplo: Lawrence Livermore National Laboratory (LLNL)",
    )

    ranking_posicion = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Posición en el TOP500",
        help_text="Posición que ocupa a nivel global",
    )

    fecha_registro = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de registro",
    )

    fecha_actualizacion = models.DateTimeField(
        auto_now=True,
        verbose_name="Última actualización",
    )

    class Meta:
        verbose_name = "Supercomputadora"
        verbose_name_plural = "Supercomputadoras"
        ordering = ["-teraflops", "ranking_posicion", "nombre"]

    def __str__(self):
        return f"{self.nombre} ({self.pais_origen}) - {self.teraflops:,.2f} TFLOPS"

    def get_absolute_url(self):
        return reverse("computadoras:detalle", kwargs={"pk": self.pk})

    @property
    def petaflops(self):
        """Devuelve el rendimiento en PetaFLOPS (1 PFLOPS = 1,000 TFLOPS)"""
        return float(self.teraflops) / 1000.0

    @property
    def exaflops(self):
        """Devuelve el rendimiento en ExaFLOPS (1 EFLOPS = 1,000,000 TFLOPS)"""
        return float(self.teraflops) / 1_000_000.0

    @property
    def ram_petabytes(self):
        """Devuelve la RAM en Petabytes (1 PB = 1,000 TB)"""
        return float(self.ram_tb) / 1000.0

    @property
    def almacenamiento_petabytes(self):
        """Devuelve el almacenamiento en Petabytes (1 PB = 1,000 TB)"""
        return float(self.almacenamiento_tb) / 1000.0
