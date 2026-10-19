from django.core.management.base import BaseCommand
from computadoras.models import Supercomputadora
from decimal import Decimal


class Command(BaseCommand):
    help = "Puebla la base de datos SQLite con la información de las 3 supercomputadoras más rápidas del mundo"

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Iniciando carga de datos iniciales..."))

        datos_supercomputadoras = [
            {
                "ranking_posicion": 1,
                "nombre": "El Capitan",
                "pais_origen": "Estados Unidos",
                "numero_cores": 11340000,
                "ram_tb": Decimal("5437.00"),
                "almacenamiento_tb": Decimal("40000.00"),
                "teraflops": Decimal("1809000.00"),  # 1.809 ExaFLOPS
                "sistema_operativo": "TOSS (Tri-Lab Operating System Software / RHEL)",
                "fabricante": "HPE Cray EX255a / AMD Instinct MI300A APU",
                "institucion": "Lawrence Livermore National Laboratory (LLNL)",
            },
            {
                "ranking_posicion": 2,
                "nombre": "Frontier",
                "pais_origen": "Estados Unidos",
                "numero_cores": 9066176,
                "ram_tb": Decimal("9200.00"),
                "almacenamiento_tb": Decimal("70000.00"),
                "teraflops": Decimal("1353000.00"),  # 1.353 ExaFLOPS
                "sistema_operativo": "HPE Cray OS (SUSE Linux Enterprise based)",
                "fabricante": "HPE Cray EX235a / AMD EPYC + AMD Instinct MI250X",
                "institucion": "Oak Ridge National Laboratory (ORNL)",
            },
            {
                "ranking_posicion": 3,
                "nombre": "Aurora",
                "pais_origen": "Estados Unidos",
                "numero_cores": 9264128,
                "ram_tb": Decimal("10900.00"),
                "almacenamiento_tb": Decimal("220000.00"),
                "teraflops": Decimal("1012000.00"),  # 1.012 ExaFLOPS
                "sistema_operativo": "SUSE Linux Enterprise Server / HPE Cray OS",
                "fabricante": "HPE Cray EX / Intel Xeon CPU Max + Intel GPU Max",
                "institucion": "Argonne National Laboratory (ANL)",
            },
        ]

        creados = 0
        actualizados = 0

        for item in datos_supercomputadoras:
            obj, created = Supercomputadora.objects.update_or_create(
                nombre=item["nombre"],
                defaults=item,
            )
            if created:
                creados += 1
                self.stdout.write(
                    self.style.SUCCESS(f"  [+] Registrada supercomputadora: {obj.nombre}")
                )
            else:
                actualizados += 1
                self.stdout.write(
                    self.style.WARNING(f"  [*] Actualizada supercomputadora: {obj.nombre}")
                )

        self.stdout.write(
            self.style.SUCCESS(
                f"\nProceso finalizado: {creados} creadas, {actualizados} actualizadas. Total en BD: {Supercomputadora.objects.count()}"
            )
        )
