from django.test import TestCase, Client
from django.urls import reverse
from decimal import Decimal
from .models import Supercomputadora


class SupercomputadoraModelTest(TestCase):
    def setUp(self):
        self.comp = Supercomputadora.objects.create(
            nombre="Fugaku",
            pais_origen="Japón",
            numero_cores=7630848,
            ram_tb=Decimal("4850.00"),
            almacenamiento_tb=Decimal("30000.00"),
            teraflops=Decimal("442010.00"),
            sistema_operativo="Red Hat Enterprise Linux",
            fabricante="Fujitsu / ARM A64FX",
            institucion="RIKEN Center for Computational Science",
            ranking_posicion=4,
        )

    def test_creacion_y_str(self):
        self.assertEqual(str(self.comp), "Fugaku (Japón) - 442,010.00 TFLOPS")

    def test_propiedades_calculadas(self):
        self.assertAlmostEqual(self.comp.petaflops, 442.01, places=2)
        self.assertAlmostEqual(self.comp.exaflops, 0.442, places=3)
        self.assertAlmostEqual(self.comp.ram_petabytes, 4.85, places=2)
        self.assertAlmostEqual(self.comp.almacenamiento_petabytes, 30.0, places=1)


class SupercomputadoraCRUDViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.comp = Supercomputadora.objects.create(
            nombre="Frontier",
            pais_origen="Estados Unidos",
            numero_cores=9066176,
            ram_tb=Decimal("9200.00"),
            almacenamiento_tb=Decimal("70000.00"),
            teraflops=Decimal("1353000.00"),
            sistema_operativo="HPE Cray OS",
            ranking_posicion=2,
        )

    def test_visualizar_listado(self):
        """Verifica la función Visualizar (Listado general)"""
        response = self.client.get(reverse("computadoras:lista"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Frontier")
        self.assertContains(response, "Estados Unidos")

    def test_visualizar_detalle(self):
        """Verifica la función Visualizar (Detalle de una supercomputadora)"""
        response = self.client.get(reverse("computadoras:detalle", kwargs={"pk": self.comp.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Frontier")
        self.assertContains(response, "HPE Cray OS")

    def test_agregar_supercomputadora(self):
        """Verifica la función Agregar (Create)"""
        data = {
            "nombre": "Aurora",
            "pais_origen": "Estados Unidos",
            "numero_cores": 9264128,
            "ram_tb": "10900.00",
            "almacenamiento_tb": "220000.00",
            "teraflops": "1012000.00",
            "sistema_operativo": "SUSE Linux Enterprise Server",
            "fabricante": "Intel / HPE Cray",
            "institucion": "Argonne National Laboratory",
            "ranking_posicion": 3,
        }
        response = self.client.post(reverse("computadoras:crear"), data)
        self.assertEqual(response.status_code, 302)  # Redirección exitosa
        self.assertTrue(Supercomputadora.objects.filter(nombre="Aurora").exists())

    def test_editar_supercomputadora(self):
        """Verifica la función Editar (Update)"""
        data = {
            "nombre": "Frontier Modificado",
            "pais_origen": "Estados Unidos",
            "numero_cores": 9100000,
            "ram_tb": "9300.00",
            "almacenamiento_tb": "75000.00",
            "teraflops": "1400000.00",
            "sistema_operativo": "HPE Cray OS v2",
            "ranking_posicion": 2,
        }
        response = self.client.post(reverse("computadoras:editar", kwargs={"pk": self.comp.pk}), data)
        self.assertEqual(response.status_code, 302)
        self.comp.refresh_from_db()
        self.assertEqual(self.comp.nombre, "Frontier Modificado")
        self.assertEqual(self.comp.numero_cores, 9100000)

    def test_borrar_supercomputadora(self):
        """Verifica la función Borrar (Delete)"""
        pk = self.comp.pk
        response = self.client.post(reverse("computadoras:eliminar", kwargs={"pk": pk}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Supercomputadora.objects.filter(pk=pk).exists())
