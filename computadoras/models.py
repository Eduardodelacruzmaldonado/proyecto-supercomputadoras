from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator


class Supercomputadora(models.Model):
    """
    Modelo de datos para registrar especificaciones tecnicas de supercomputadoras.
    Incluye los 7 campos requeridos para la base de datos SQLite y campos auxiliares
    para documentar la institucion, fabricante y posicion en el ranking TOP500.
    """

    # 1. Nombre formal del sistema
    nombre = models.CharField(
        max_length=120,
        unique=True,
        verbose_name="Nombre de la supercomputadora",
        help_text="Ejemplo: El Capitan, Frontier, Aurora",
    )

    # 2. Pais sede del centro de investigacion
    pais_origen = models.CharField(
        max_length=100,
        verbose_name="País de origen",
        help_text="Ejemplo: Estados Unidos, Japón, Alemania",
    )

    # 3. Numero de cores de procesamiento concurrente
    # Se utiliza PositiveBigIntegerField para admitir valores superiores a 11 millones
    # sin riesgo de desbordamiento en enteros estandar de 32 bits.
    numero_cores = models.PositiveBigIntegerField(
        verbose_name="Número de cores",
        validators=[MinValueValidator(1)],
        help_text="Conteo total de núcleos concurrentes (CPU + aceleradores GPU)",
    )

    # 4. Memoria RAM principal en Terabytes
    ram_tb = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name="Cantidad de RAM (TB)",
        validators=[MinValueValidator(0.01)],
        help_text="Memoria RAM total distribuida en Terabytes",
    )

    # 5. Capacidad de almacenamiento masivo en Terabytes
    almacenamiento_tb = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        verbose_name="Almacenamiento (TB)",
        validators=[MinValueValidator(0.01)],
        help_text="Capacidad de almacenamiento paralelo en Terabytes",
    )

    # 6. Rendimiento de calculo en TeraFLOPS
    # Se emplea DecimalField para evitar errores de redondeo inherentes a FloatField
    teraflops = models.DecimalField(
        max_digits=16,
        decimal_places=2,
        verbose_name="Rendimiento (TeraFLOPS)",
        validators=[MinValueValidator(0.01)],
        help_text="Rendimiento medido (1 PetaFLOPS = 1,000 TFLOPS, 1 ExaFLOPS = 1,000,000 TFLOPS)",
    )

    # 7. Plataforma y sistema operativo base
    sistema_operativo = models.CharField(
        max_length=150,
        verbose_name="Sistema operativo",
        help_text="Distribución base (ej. TOSS / RHEL, HPE Cray OS, SUSE)",
    )

    # Informacion complementaria de arquitectura y organizacion
    fabricante = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="Fabricante / Arquitectura",
        help_text="Ejemplo: HPE Cray EX255a / APU AMD Instinct MI300A",
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
        verbose_name="Posición en TOP500",
        help_text="Lugar en el ranking mundial de supercómputo",
    )

    fecha_registro = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de registro",
    )

    fecha_actualizacion = models.DateTimeField(
        auto_now=True,
        verbose_name="Última modificación",
    )

    class Meta:
        verbose_name = "Supercomputadora"
        verbose_name_plural = "Supercomputadoras"
        ordering = ["-teraflops", "ranking_posicion", "nombre"]

    def __str__(self):
        return f"{self.nombre} ({self.pais_origen}) - {self.teraflops:,.2f} TFLOPS"

    def get_absolute_url(self):
        return reverse("computadoras:detalle", kwargs={"pk": self.pk})

    # Propiedades calculadas en memoria para visualizacion de unidades
    @property
    def petaflops(self):
        """Conversion de TeraFLOPS a PetaFLOPS (1 PFLOPS = 10^3 TFLOPS)"""
        return float(self.teraflops) / 1000.0

    @property
    def exaflops(self):
        """Conversion de TeraFLOPS a ExaFLOPS (1 EFLOPS = 10^6 TFLOPS)"""
        return float(self.teraflops) / 1_000_000.0

    @property
    def ram_petabytes(self):
        """Conversion de RAM en Terabytes a Petabytes (1 PB = 10^3 TB)"""
        return float(self.ram_tb) / 1000.0

    @property
    def almacenamiento_petabytes(self):
        """Conversion de almacenamiento en Terabytes a Petabytes"""
        return float(self.almacenamiento_tb) / 1000.0
