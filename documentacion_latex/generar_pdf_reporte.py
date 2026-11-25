import os
from fpdf import FPDF

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIR, "imagenes")
OUTPUT_PDF = os.path.join(BASE_DIR, "Proyecto_Final_Computacion_Concurrente_Django.pdf")
ROOT_PDF = os.path.join(os.path.dirname(BASE_DIR), "Proyecto_Final_Computacion_Concurrente_Django.pdf")


class PDFReporte(FPDF):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_font("ArialUnicode", "", r"C:\Windows\Fonts\arial.ttf")
        self.add_font("ArialUnicode", "B", r"C:\Windows\Fonts\arialbd.ttf")
        self.add_font("ArialUnicode", "I", r"C:\Windows\Fonts\ariali.ttf")

    def header(self):
        if self.page_no() > 1:
            self.set_font("ArialUnicode", "B", 8)
            self.set_text_color(108, 117, 125)
            self.cell(0, 8, "COMPUTACIÓN CONCURRENTE | PROYECTO FINAL", align="L")
            self.cell(0, 8, "LICENCIATURA EN CIENCIA DE DATOS", align="R")
            self.ln(9)
            self.set_draw_color(222, 226, 230)
            self.set_line_width(0.3)
            self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
            self.ln(4)

    def footer(self):
        if self.page_no() > 1:
            self.set_y(-15)
            self.set_font("ArialUnicode", "I", 8)
            self.set_text_color(108, 117, 125)
            self.cell(0, 10, "Prof. Esp. Adrián Durán Chavesti - Base de Datos Web", align="L")
            self.cell(0, 10, f"Página {self.page_no()}", align="C")
            self.cell(0, 10, "Django & SQLite (CRUD)", align="R")

    def chapter_title(self, num_str, title_str):
        self.set_font("ArialUnicode", "B", 13)
        self.set_text_color(13, 110, 253)
        self.set_fill_color(248, 249, 250)
        self.ln(3)
        self.cell(0, 8.0, f"  {num_str} {title_str}", fill=True, new_x="LMARGIN", new_y="NEXT")
        self.ln(3)

    def section_title(self, title_str):
        self.set_font("ArialUnicode", "B", 10.5)
        self.set_text_color(33, 37, 41)
        self.ln(2)
        self.cell(0, 6.0, title_str, new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

    def body_paragraph(self, text):
        self.set_font("ArialUnicode", "", 9.0)
        self.set_text_color(33, 37, 41)
        self.multi_cell(0, 4.8, text)
        self.ln(2)

    def code_block(self, code_text):
        self.set_font("Courier", "", 7.5)
        self.set_fill_color(248, 249, 250)
        self.set_text_color(33, 37, 41)
        self.set_draw_color(222, 226, 230)
        self.multi_cell(0, 4.0, code_text, border=1, fill=True)
        self.ln(2)

    def add_screenshot(self, img_filename, caption_text, width=155):
        img_path = os.path.join(IMG_DIR, img_filename)
        if os.path.exists(img_path):
            if self.get_y() > 210:
                self.add_page()
            self.image(img_path, x=(self.w - width) / 2, w=width)
            self.ln(2)
            self.set_font("ArialUnicode", "I", 8.0)
            self.set_text_color(108, 117, 125)
            self.cell(0, 4.5, caption_text, align="C", new_x="LMARGIN", new_y="NEXT")
            self.ln(3)


def generar_pdf():
    pdf = PDFReporte(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=True, margin=18)
    pdf.set_margins(18, 18, 18)

    # =========================================================================
    # PORTADA
    # =========================================================================
    pdf.add_page()
    pdf.set_fill_color(33, 37, 41)
    pdf.rect(0, 0, 210, 12, style="F")

    pdf.set_y(24)
    pdf.set_font("ArialUnicode", "B", 14.0)
    pdf.set_text_color(33, 37, 41)
    pdf.cell(0, 7, "LICENCIATURA EN CIENCIA DE DATOS", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("ArialUnicode", "B", 11.5)
    pdf.set_text_color(13, 110, 253)
    pdf.cell(0, 6, "ASIGNATURA: COMPUTACIÓN CONCURRENTE", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)

    pdf.set_draw_color(13, 110, 253)
    pdf.set_line_width(1.0)
    pdf.line(20, pdf.get_y(), 190, pdf.get_y())
    pdf.ln(8)

    pdf.set_font("ArialUnicode", "B", 15.0)
    pdf.set_text_color(33, 37, 41)
    pdf.multi_cell(
        0, 7.5,
        "PROYECTO FINAL:\nCreación de una Base de Datos con Acceso Web usando Django en Python",
        align="C"
    )
    pdf.ln(2)
    pdf.set_font("ArialUnicode", "", 10.0)
    pdf.set_text_color(108, 117, 125)
    pdf.cell(0, 5.5, "Gestión de Datos y Operaciones CRUD (Agregar, Editar, Borrar, Visualizar)", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)

    pdf.set_draw_color(222, 226, 230)
    pdf.set_line_width(0.5)
    pdf.line(40, pdf.get_y(), 170, pdf.get_y())
    pdf.ln(8)

    # Cuadro institucional
    pdf.set_fill_color(248, 249, 250)
    pdf.set_draw_color(222, 226, 230)
    box_y = pdf.get_y()
    pdf.rect(20, box_y, 170, 70, style="DF")

    pdf.set_y(box_y + 5)
    pdf.set_font("ArialUnicode", "B", 9.5)
    pdf.set_text_color(33, 37, 41)
    pdf.cell(85, 5.5, "   Docente:", align="L")
    pdf.cell(85, 5.5, "Fecha de Entrega:   ", align="R", new_x="LMARGIN", new_y="NEXT")

    pdf.set_font("ArialUnicode", "", 9.0)
    pdf.set_text_color(73, 80, 87)
    pdf.cell(85, 5.0, "   Esp. Adrián Durán Chavesti", align="L")
    pdf.cell(85, 5.0, "Jueves 26 de Noviembre   ", align="R", new_x="LMARGIN", new_y="NEXT")

    pdf.ln(2)
    pdf.set_font("ArialUnicode", "B", 9.5)
    pdf.set_text_color(33, 37, 41)
    pdf.cell(85, 5.5, "   Asignatura:", align="L")
    pdf.cell(85, 5.5, "Ponderación:   ", align="R", new_x="LMARGIN", new_y="NEXT")

    pdf.set_font("ArialUnicode", "", 9.0)
    pdf.set_text_color(73, 80, 87)
    pdf.cell(85, 5.0, "   Computación Concurrente", align="L")
    pdf.cell(85, 5.0, "10 puntos (Exposición y Pruebas)   ", align="R", new_x="LMARGIN", new_y="NEXT")

    pdf.ln(2)
    pdf.set_font("ArialUnicode", "B", 9.5)
    pdf.set_text_color(33, 37, 41)
    pdf.cell(0, 5.5, "   Integrantes del Equipo (7 Expositores):", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("ArialUnicode", "", 9.0)
    pdf.set_text_color(73, 80, 87)
    pdf.cell(0, 5.0, "   Equipo de Laboratorio - Licenciatura en Ciencia de Datos", new_x="LMARGIN", new_y="NEXT")

    pdf.set_y(box_y + 80)
    pdf.set_fill_color(248, 249, 250)
    pdf.set_draw_color(222, 226, 230)
    pdf.rect(20, pdf.get_y(), 170, 26, style="DF")
    pdf.set_y(pdf.get_y() + 3.0)
    pdf.set_font("ArialUnicode", "B", 8.8)
    pdf.set_text_color(13, 110, 253)
    pdf.cell(0, 4.8, "Objetivo General Planteado en la Rúbrica:", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("ArialUnicode", "I", 8.5)
    pdf.set_text_color(73, 80, 87)
    pdf.multi_cell(
        0, 4.3,
        '"Con ayuda del framework Django crear y gestionar una base de datos SQLite con el lenguaje de programación Python, '
        'registrando la información relevante de las 3 computadoras más rápidas del mundo y habilitando las funciones de Agregar, Editar, Borrar y Visualizar."',
        align="C"
    )

    pdf.set_y(260)
    pdf.set_font("ArialUnicode", "B", 9.0)
    pdf.set_text_color(108, 117, 125)
    pdf.cell(0, 5, "LICENCIATURA EN CIENCIA DE DATOS - SEMESTRE ACADÉMICO 2026-II", align="C")

    # =========================================================================
    # SECCIÓN 1: GUÍA DE EXPOSICIÓN (7 INTEGRANTES)
    # =========================================================================
    pdf.add_page()
    pdf.chapter_title("1.", "Guía y División del Proyecto para los 7 Expositores")

    pdf.section_title("Integrante 1: Objetivo del Proyecto y Requisitos de la Práctica")
    pdf.body_paragraph(
        "• Contexto y Propósito: El objetivo de la práctica en Computación Concurrente es construir una aplicación web completa "
        "con base de datos relacional SQLite utilizando el framework Django en Python.\n"
        "• Conjunto de Datos: Se utilizan las 3 supercomputadoras más potentes del mundo (El Capitan, Frontier y Aurora) como "
        "los registros que se ingresan en la base de datos para almacenar y manipular información técnica a gran escala.\n"
        "• Requisitos de la Rúbrica: Cumplir con los 7 campos obligatorios por registro y habilitar las 4 funciones CRUD: "
        "Agregar, Editar, Borrar y Visualizar."
    )

    pdf.section_title("Integrante 2: Arquitectura Django, Patrón MVT y Seguridad (ORM)")
    pdf.body_paragraph(
        "• ¿Qué es Django?: Es un framework de desarrollo web en Python que incluye herramientas integradas para autenticación, "
        "administración y bases de datos, permitiendo un desarrollo ágil y profesional.\n"
        "• El Patrón MVT (Modelo - Vista - Template):\n"
        "   - Modelo (models.py): Estructura la tabla y las reglas de los datos.\n"
        "   - Vista (views.py): Contiene la lógica que atiende las solicitudes y consulta los registros.\n"
        "   - Template (templates/): Genera el HTML que el usuario visualiza en su navegador.\n"
        "• Seguridad y Prevención de Inyecciones SQL: Al usar el ORM de Django, las consultas nunca se concatenan como texto directo "
        "en SQL. Django utiliza parámetros seguros que neutralizan automáticamente cualquier intento de inyección de código malicioso."
    )

    pdf.section_title("Integrante 3: Base de Datos SQLite y Código del Modelo")
    pdf.body_paragraph(
        "• Base de Datos Integrada: SQLite viene configurado por defecto en Django en el archivo local 'db.sqlite3', sin requerir servidores externos.\n"
        "• Los 7 Campos Obligatorios Solicitados:\n"
        "   1. Nombre  |  2. País de origen  |  3. Número de cores  |  4. Cantidad de RAM (TB)\n"
        "   5. Almacenamiento (TB)  |  6. TeraFLOPS  |  7. Sistema operativo\n"
        "• Código Fuente de la Base de Datos (models.py):"
    )

    codigo_modelo = (
        "class Supercomputadora(models.Model):\n"
        "    nombre = models.CharField(max_length=120, unique=True, verbose_name='Nombre')\n"
        "    pais_origen = models.CharField(max_length=100, verbose_name='Pais de origen')\n"
        "    numero_cores = models.PositiveBigIntegerField(verbose_name='Numero de cores')\n"
        "    ram_tb = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='RAM (TB)')\n"
        "    almacenamiento_tb = models.DecimalField(max_digits=14, decimal_places=2, verbose_name='Almacenamiento (TB)')\n"
        "    teraflops = models.DecimalField(max_digits=16, decimal_places=2, verbose_name='Rendimiento (TeraFLOPS)')\n"
        "    sistema_operativo = models.CharField(max_length=150, verbose_name='Sistema operativo')\n"
    )
    pdf.code_block(codigo_modelo)

    pdf.add_page()
    pdf.section_title("Integrante 4: Diseño Frontend, Maquetación HTML5 y Estilos")
    pdf.body_paragraph(
        "• Diseño Claro y Adaptable: Se utilizó HTML5 y Bootstrap 5 para crear una interfaz limpia, comprensible y responsiva "
        "que funciona correctamente en computadoras o teléfonos móviles.\n"
        "• Modularidad con base.html: Para evitar duplicar la barra de navegación, el encabezado y el pie de página en cada pantalla, "
        "se creó una plantilla base ('base.html'). Las demás vistas solo rellenan la sección central con la etiqueta {% block content %}. "
        "Esto hace que el código sea limpio y que todo el sitio comparta el mismo diseño de forma ordenada."
    )

    pdf.section_title("Integrante 5: Operaciones del CRUD (Parte 1: Visualizar y Agregar)")
    pdf.body_paragraph(
        "• Función Visualizar:\n"
        "   - Catálogo General (/): Muestra en una tabla organizada las computadoras guardadas en SQLite, junto a un resumen numérico "
        "con los totales de cores, TeraFLOPS y almacenamiento acumulados.\n"
        "   - Ficha Técnica (/<id>/): Al pulsar en 'Ver', se muestran los detalles individuales de la computadora y conversiones automáticas "
        "(PetaFLOPS, ExaFLOPS y Petabytes).\n"
        "• Función Agregar (/nueva/):\n"
        "   - Permite dar de alta un nuevo equipo mediante un formulario web validado que impide dejar campos requeridos en blanco."
    )

    pdf.section_title("Integrante 6: Operaciones del CRUD (Parte 2: Editar y Borrar)")
    pdf.body_paragraph(
        "• Función Editar (/<id>/editar/):\n"
        "   - Abre el formulario con los datos actuales precargados, permitiendo modificar cualquier campo y guardar los cambios al instante en SQLite.\n"
        "• Función Borrar (/<id>/eliminar/):\n"
        "   - Seguridad de Eliminación: La eliminación no se ejecuta directamente con un solo clic. Django presenta una pantalla de confirmación "
        "que utiliza una petición HTTP POST protegida con un token {% csrf_token %}, evitando borrados involuntarios o ataques externos."
    )

    pdf.section_title("Integrante 7: Despliegue en la Nube con Render y Conclusiones")
    pdf.body_paragraph(
        "• Despliegue en Render:\n"
        "   - El proyecto está vinculado a un repositorio remoto en GitHub. Al actualizar el código, Render ejecuta el script 'build.sh' "
        "(instalación de paquetes, recolección de archivos estáticos y migraciones de SQLite).\n"
        "   - El archivo 'Procfile' inicia el servidor en producción con Gunicorn, manteniendo la aplicación activa en la nube.\n"
        "• Conclusiones:\n"
        "   - El proyecto cumple al 100% con la consigna solicitada en la rúbrica oficial, integrando base de datos, backend en Django y "
        "frontend responsivo de forma clara y fácil de defender en el laboratorio."
    )

    # =========================================================================
    # SECCIÓN 2: DATOS DE LAS 3 COMPUTADORAS
    # =========================================================================
    pdf.add_page()
    pdf.chapter_title("2.", "Datos Registrados en SQLite (3 Computadoras más Rápidas)")

    # Tabla
    pdf.set_font("ArialUnicode", "B", 7.5)
    pdf.set_fill_color(33, 37, 41)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(32, 6.0, "Campo Requerido", border=1, fill=True)
    pdf.cell(46, 6.0, "#1 El Capitan (EE.UU.)", border=1, fill=True)
    pdf.cell(46, 6.0, "#2 Frontier (EE.UU.)", border=1, fill=True)
    pdf.cell(46, 6.0, "#3 Aurora (EE.UU.)", border=1, fill=True, new_x="LMARGIN", new_y="NEXT")

    tabla_datos = [
        ("1. Nombre", "El Capitan", "Frontier", "Aurora"),
        ("2. País de Origen", "Estados Unidos", "Estados Unidos", "Estados Unidos"),
        ("3. Número de Cores", "11,340,000 cores", "9,066,176 cores", "9,264,128 cores"),
        ("4. Cantidad de RAM", "5,437 TB (~5.44 PB)", "9,200 TB (~9.20 PB)", "10,900 TB (~10.90 PB)"),
        ("5. Almacenamiento", "40,000 TB (40 PB)", "70,000 TB (70 PB)", "220,000 TB (220 PB)"),
        ("6. TeraFLOPS", "1,809,000.00 TFLOPS", "1,353,000.00 TFLOPS", "1,012,000.00 TFLOPS"),
        ("7. Sistema Operativo", "TOSS (RHEL-based)", "HPE Cray OS", "SUSE Linux Enterprise"),
        ("Institución", "Lawrence Livermore Lab", "Oak Ridge Nat. Lab", "Argonne Nat. Lab"),
    ]

    pdf.set_font("ArialUnicode", "", 7.5)
    pdf.set_text_color(33, 37, 41)
    alt = False
    for fila in tabla_datos:
        pdf.set_fill_color(248, 249, 250) if alt else pdf.set_fill_color(255, 255, 255)
        pdf.cell(32, 5.2, f" {fila[0]}", border=1, fill=True)
        pdf.cell(46, 5.2, f" {fila[1]}", border=1, fill=True)
        pdf.cell(46, 5.2, f" {fila[2]}", border=1, fill=True)
        pdf.cell(46, 5.2, f" {fila[3]}", border=1, fill=True, new_x="LMARGIN", new_y="NEXT")
        alt = not alt

    pdf.ln(4)

    # =========================================================================
    # SECCIÓN 3: EVIDENCIA VISUAL DEL CRUD
    # =========================================================================
    pdf.chapter_title("3.", "Evidencia de Funcionamiento del CRUD Web")

    pdf.section_title("3.1. Función Visualizar: Catálogo General en SQLite")
    pdf.body_paragraph("Pantalla principal con métricas acumuladas y tabla de registros:")
    pdf.add_screenshot("10_web_dashboard.png", "Figura 1: Vista general del listado y totales calculados en SQLite.")

    pdf.add_page()
    pdf.section_title("3.2. Función Visualizar: Ficha Técnica Detallada")
    pdf.body_paragraph("Vista individual de un registro con conversiones automáticas:")
    pdf.add_screenshot("11_web_detalle.png", "Figura 2: Ficha técnica detallada de una supercomputadora.")

    pdf.section_title("3.3. Función Agregar: Formulario Web de Alta")
    pdf.body_paragraph("Formulario para registrar nuevas computadoras con validación de campos:")
    pdf.add_screenshot("12_web_agregar_formulario.png", "Figura 3: Formulario web de alta de registros.")

    pdf.add_page()
    pdf.section_title("3.4. Función Editar: Modificación de Especificaciones")
    pdf.body_paragraph("Formulario con datos precargados listo para actualizar campos en SQLite:")
    pdf.add_screenshot("13_web_editar_formulario.png", "Figura 4: Formulario de edición de especificaciones.")

    pdf.section_title("3.5. Función Borrar: Confirmación Segura de Eliminación")
    pdf.body_paragraph("Diálogo de confirmación previa con petición POST protegida:")
    pdf.add_screenshot("14_web_confirmar_eliminar.png", "Figura 5: Pantalla de confirmación para eliminar un registro.")

    pdf.add_page()
    pdf.section_title("3.6. Panel Administrativo Oficial de Django (/admin/)")
    pdf.body_paragraph("Interfaz administrativa nativa con filtros y buscador de registros:")
    pdf.add_screenshot("16_web_admin_listado.png", "Figura 6: Panel de administración integrado de Django.")

    # =========================================================================
    # SECCIÓN 4: REFERENCIAS CITADAS EN LA CONSIGNAS
    # =========================================================================
    pdf.chapter_title("4.", "Referencias y Enlaces Citados en la Cátedra")
    enlaces = [
        ("Visual Studio Code", "https://code.visualstudio.com/"),
        ("¿Qué es Django y por qué importa? - Django y DRF", "https://www.youtube.com/watch?v=B8OlRdYwNlA"),
        ("Django Portafolio, Ejemplo Práctico", "https://www.youtube.com/watch?v=zBjMF6je24U"),
        ("Django REST Framework y React CRUD", "https://www.youtube.com/watch?v=38XWpyEK8IY"),
        ("Crea una agenda virtual con Django", "https://www.youtube.com/watch?v=EQ-kqDmfUoM"),
        ("TOP500 List", "https://top500.org/"),
    ]
    pdf.set_font("ArialUnicode", "", 8.5)
    for nombre, url in enlaces:
        pdf.set_text_color(33, 37, 41)
        pdf.cell(70, 5.0, f"• {nombre}: ", align="L")
        pdf.set_text_color(13, 110, 253)
        pdf.cell(0, 5.0, url, align="L", new_x="LMARGIN", new_y="NEXT")

    pdf.output(OUTPUT_PDF)
    # Copiar tambien a la raiz
    try:
        import shutil
        shutil.copyfile(OUTPUT_PDF, ROOT_PDF)
    except Exception:
        pass
    print(f"[OK] PDF generado: {OUTPUT_PDF}")


if __name__ == "__main__":
    generar_pdf()
