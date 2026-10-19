import os
from fpdf import FPDF

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIR, "imagenes")
OUTPUT_PDF = os.path.join(BASE_DIR, "Proyecto_Final_Computacion_Concurrente_Django.pdf")

class PDFReporte(FPDF):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_font("ArialUnicode", "", r"C:\Windows\Fonts\arial.ttf")
        self.add_font("ArialUnicode", "B", r"C:\Windows\Fonts\arialbd.ttf")
        self.add_font("ArialUnicode", "I", r"C:\Windows\Fonts\ariali.ttf")

    def header(self):
        if self.page_no() > 1:
            self.set_font("ArialUnicode", "B", 8)
            self.set_text_color(100, 116, 139)
            self.cell(0, 8, "COMPUTACIÓN CONCURRENTE | PROYECTO FINAL DJANGO & SQLITE", align="L")
            self.cell(0, 8, "LICENCIATURA EN CIENCIA DE DATOS", align="R")
            self.ln(9)
            self.set_draw_color(226, 232, 240)
            self.set_line_width(0.3)
            self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
            self.ln(4)

    def footer(self):
        if self.page_no() > 1:
            self.set_y(-15)
            self.set_font("ArialUnicode", "I", 8)
            self.set_text_color(148, 163, 184)
            self.cell(0, 10, "Prof. Adrián Durán Chavesti - Top 3 Supercomputadoras", align="L")
            self.cell(0, 10, f"Página {self.page_no()}", align="C")
            self.cell(0, 10, "Django & SQLite Web CRUD", align="R")

    def chapter_title(self, num_str, title_str):
        self.set_font("ArialUnicode", "B", 15)
        self.set_text_color(15, 23, 42)
        self.set_fill_color(241, 245, 249)
        self.ln(3)
        self.cell(0, 9, f"  {num_str} {title_str}", fill=True, new_x="LMARGIN", new_y="NEXT")
        self.ln(3)

    def section_title(self, title_str):
        self.set_font("ArialUnicode", "B", 12)
        self.set_text_color(30, 58, 138)
        self.ln(2)
        self.cell(0, 7, title_str, new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

    def body_paragraph(self, text):
        self.set_font("ArialUnicode", "", 10)
        self.set_text_color(51, 65, 85)
        self.multi_cell(0, 5.5, text)
        self.ln(2)

    def add_screenshot(self, img_filename, caption_text, width=160):
        img_path = os.path.join(IMG_DIR, img_filename)
        if os.path.exists(img_path):
            if self.get_y() > 200:
                self.add_page()
            self.image(img_path, x=(self.w - width) / 2, w=width)
            self.ln(2)
            self.set_font("ArialUnicode", "I", 8.5)
            self.set_text_color(100, 116, 139)
            self.cell(0, 5, caption_text, align="C", new_x="LMARGIN", new_y="NEXT")
            self.ln(4)
        else:
            self.set_font("ArialUnicode", "I", 9)
            self.set_text_color(220, 38, 38)
            self.cell(0, 6, f"[Imagen no encontrada: {img_filename}]", new_x="LMARGIN", new_y="NEXT")
            self.ln(2)


def generar_pdf():
    pdf = PDFReporte(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=True, margin=18)
    pdf.set_margins(18, 18, 18)

    # =========================================================================
    # PORTADA
    # =========================================================================
    pdf.add_page()
    pdf.set_fill_color(15, 23, 42) # Slate Dark 900
    pdf.rect(0, 0, 210, 16, style="F")

    pdf.set_y(26)
    pdf.set_font("ArialUnicode", "B", 16)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(0, 7, "LICENCIATURA EN CIENCIA DE DATOS", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("ArialUnicode", "B", 13)
    pdf.set_text_color(30, 58, 138)
    pdf.cell(0, 6, "COMPUTACIÓN CONCURRENTE", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(8)

    pdf.set_draw_color(13, 110, 253)
    pdf.set_line_width(1.5)
    pdf.line(20, pdf.get_y(), 190, pdf.get_y())
    pdf.ln(10)

    pdf.set_font("ArialUnicode", "B", 20)
    pdf.set_text_color(15, 23, 42)
    pdf.multi_cell(0, 9, "PROYECTO FINAL:\nCreación de una Base de Datos con Acceso Web usando Django en Python", align="C")
    pdf.ln(6)

    pdf.set_draw_color(226, 232, 240)
    pdf.set_line_width(0.5)
    pdf.line(40, pdf.get_y(), 170, pdf.get_y())
    pdf.ln(12)

    # Cuadro informativo institucional
    pdf.set_fill_color(248, 250, 252)
    pdf.set_draw_color(203, 213, 225)
    box_y = pdf.get_y()
    pdf.rect(20, box_y, 170, 72, style="DF")

    pdf.set_y(box_y + 6)
    pdf.set_font("ArialUnicode", "B", 10.5)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(85, 6, "   Docente Asignado:", align="L")
    pdf.cell(85, 6, "Entrega y Exposición:   ", align="R", new_x="LMARGIN", new_y="NEXT")

    pdf.set_font("ArialUnicode", "", 10)
    pdf.set_text_color(51, 65, 85)
    pdf.cell(85, 5.5, "   Esp. Adrián Durán Chavesti", align="L")
    pdf.cell(85, 5.5, "Jueves 26 de Noviembre   ", align="R", new_x="LMARGIN", new_y="NEXT")

    pdf.ln(4)
    pdf.set_font("ArialUnicode", "B", 10.5)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(85, 6, "   Materia:", align="L")
    pdf.cell(85, 6, "Valor de la Evaluación:   ", align="R", new_x="LMARGIN", new_y="NEXT")

    pdf.set_font("ArialUnicode", "", 10)
    pdf.set_text_color(51, 65, 85)
    pdf.cell(85, 5.5, "   Computación Concurrente", align="L")
    pdf.cell(85, 5.5, "10 puntos (Exposición y Pruebas)   ", align="R", new_x="LMARGIN", new_y="NEXT")

    pdf.ln(4)
    pdf.set_font("ArialUnicode", "B", 10.5)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(0, 6, "   Tema del Proyecto:", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("ArialUnicode", "", 10)
    pdf.set_text_color(51, 65, 85)
    pdf.cell(0, 5.5, "   Base de Datos SQLite de las 3 Computadoras más Rápidas del Mundo (CRUD)", new_x="LMARGIN", new_y="NEXT")

    pdf.set_y(box_y + 82)
    pdf.set_fill_color(238, 242, 255)
    pdf.set_draw_color(199, 210, 254)
    pdf.rect(20, pdf.get_y(), 170, 28, style="DF")
    pdf.set_y(pdf.get_y() + 4)
    pdf.set_font("ArialUnicode", "B", 9.5)
    pdf.set_text_color(30, 58, 138)
    pdf.cell(0, 5, "Objetivo Oficial del Proyecto:", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("ArialUnicode", "I", 9)
    pdf.set_text_color(51, 65, 85)
    pdf.multi_cell(0, 4.8, '"Con ayuda del framework Django crear y gestionar una base de datos SQLite con el lenguaje de programación Python, verificando las funciones de Agregar, Editar, Borrar y Visualizar."', align="C")

    pdf.set_y(260)
    pdf.set_font("ArialUnicode", "B", 10)
    pdf.set_text_color(100, 116, 139)
    pdf.cell(0, 5, "CICLO ACADÉMICO 2026 - DOCUMENTACIÓN TÉCNICA OFICIAL", align="C")

    # =========================================================================
    # SECCIÓN 1: INTRODUCCIÓN Y REQUISITOS
    # =========================================================================
    pdf.add_page()
    pdf.chapter_title("1.", "Introducción y Alcance del Proyecto")
    pdf.body_paragraph(
        "En la disciplina de Ciencia de Datos y Cómputo Concurrente, las supercomputadoras representan "
        "los sistemas distribuidos y paralelos de mayor capacidad en la historia de la informática. "
        "Para gestionar eficazmente las especificaciones de estos macro-sistemas, este proyecto implementa "
        "una solución web integral basada en Django y SQLite que permite almacenar, consultar, auditar y manipular "
        "los registros de las 3 computadoras más potentes de la tierra."
    )
    pdf.body_paragraph(
        "El sistema cumple rigurosamente con los 7 parámetros solicitados en la consigna de trabajo:\n"
        "  1. Nombre de la supercomputadora\n"
        "  2. País de origen\n"
        "  3. Número de cores (concurrencia de núcleos de procesamiento)\n"
        "  4. Cantidad de memoria RAM (expresada en Terabytes)\n"
        "  5. Capacidad de almacenamiento masivo (expresada en Terabytes)\n"
        "  6. Rendimiento de cálculo en TeraFLOPS\n"
        "  7. Sistema operativo\n\n"
        "Asimismo, se han desarrollado e integrado las 4 operaciones CRUD fundamentales: Agregar, Editar, Borrar y Visualizar, "
        "además del panel administrativo oficial de Django."
    )

    pdf.chapter_title("2.", "Especificaciones de las 3 Computadoras más Rápidas")
    pdf.body_paragraph(
        "De acuerdo con los registros oficiales del ranking internacional TOP500 de supercómputo de exaescala, "
        "los tres primeros lugares globales corresponden a los siguientes sistemas concurrentes:"
    )

    # Tabla en PDF
    pdf.set_font("ArialUnicode", "B", 8)
    pdf.set_fill_color(30, 41, 59)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(32, 7, "Parámetro", border=1, fill=True)
    pdf.cell(46, 7, "#1 El Capitan (EE.UU.)", border=1, fill=True)
    pdf.cell(46, 7, "#2 Frontier (EE.UU.)", border=1, fill=True)
    pdf.cell(46, 7, "#3 Aurora (EE.UU.)", border=1, fill=True, new_x="LMARGIN", new_y="NEXT")

    tabla_datos = [
        ("Institución", "Lawrence Livermore Lab", "Oak Ridge Nat. Lab", "Argonne Nat. Lab"),
        ("Núcleos (Cores)", "11,340,000 cores", "9,066,176 cores", "9,264,128 cores"),
        ("RAM (TB)", "5,437 TB (~5.44 PB)", "9,200 TB (~9.2 PB)", "10,900 TB (~10.9 PB)"),
        ("Almacenamiento (TB)", "40,000 TB (40 PB)", "70,000 TB (70 PB Orion)", "220,000 TB (220 PB DAOS)"),
        ("TeraFLOPS", "1,809,000.00 TFLOPS", "1,353,000.00 TFLOPS", "1,012,000.00 TFLOPS"),
        ("ExaFLOPS (Rmax)", "1.809 ExaFLOPS", "1.353 ExaFLOPS", "1.012 ExaFLOPS"),
        ("Sistema Operativo", "TOSS (RHEL-based)", "HPE Cray OS (SUSE)", "SUSE Linux Enterprise"),
        ("Arquitectura / HW", "HPE Cray EX / MI300A", "HPE Cray EX / MI250X", "Intel Max Blades"),
    ]

    pdf.set_font("ArialUnicode", "", 7.8)
    pdf.set_text_color(30, 41, 59)
    alt = False
    for fila in tabla_datos:
        pdf.set_fill_color(248, 250, 252) if alt else pdf.set_fill_color(255, 255, 255)
        pdf.cell(32, 6, f" {fila[0]}", border=1, fill=True)
        pdf.cell(46, 6, f" {fila[1]}", border=1, fill=True)
        pdf.cell(46, 6, f" {fila[2]}", border=1, fill=True)
        pdf.cell(46, 6, f" {fila[3]}", border=1, fill=True, new_x="LMARGIN", new_y="NEXT")
        alt = not alt

    pdf.ln(5)

    # =========================================================================
    # SECCIÓN 3: PASO A PASO CON CAPTURAS DE TERMINAL
    # =========================================================================
    pdf.add_page()
    pdf.chapter_title("3.", "Paso a Paso de Instalación y Comandos Ejecutados")
    pdf.body_paragraph(
        "A continuación se presenta la secuencia completa de comandos ejecutados en la consola de comandos de Windows "
        "para inicializar, estructurar, migrar y desplegar la solución tecnológica."
    )

    pdf.section_title("Paso 1: Verificación del Intérprete Python y Pip")
    pdf.body_paragraph("Se constató la presencia del runtime de Python y el gestor de paquetes pip en el sistema operativo.")
    pdf.add_screenshot("01_verificar_entorno.png", "Figura 1: Verificación de versiones de Python y pip en consola PowerShell.")

    pdf.section_title("Paso 2: Instalación de Django mediante Pip")
    pdf.body_paragraph("Se ejecutó la instalación de Django junto a sus dependencias asgiref y sqlparse.")
    pdf.add_screenshot("02_instalacion_django.png", "Figura 2: Instalación de Django mediante py -m pip install django.")

    pdf.add_page()
    pdf.section_title("Paso 3: Creación del Proyecto y la Aplicación de Django")
    pdf.body_paragraph("Se inicializó el proyecto base 'supercomputadoras_project' y la aplicación interna 'computadoras'.")
    pdf.add_screenshot("03_creacion_proyecto.png", "Figura 3: Ejecución de startproject y startapp.")

    pdf.section_title("Paso 4: Creación de Migraciones (makemigrations)")
    pdf.body_paragraph("El ORM de Django tradujo el modelo Supercomputadora en el archivo de migración computadoras/migrations/0001_initial.py.")
    pdf.add_screenshot("04_makemigrations.png", "Figura 4: Detección y creación del archivo de migración inicial.")

    pdf.add_page()
    pdf.section_title("Paso 5: Aplicación de Migraciones a SQLite (migrate)")
    pdf.body_paragraph("El comando migrate creó de forma física las tablas en la base de datos db.sqlite3.")
    pdf.add_screenshot("05_migrate.png", "Figura 5: Creación exitosa de las tablas relacionales en SQLite.")

    pdf.section_title("Paso 6: Poblado Automático de las 3 Supercomputadoras")
    pdf.body_paragraph("Se ejecutó el comando de gestión personalizado para cargar automáticamente los registros de El Capitan, Frontier y Aurora.")
    pdf.add_screenshot("06_poblar_datos.png", "Figura 6: Ejecución del comando de gestión poblar_datos.")

    pdf.add_page()
    pdf.section_title("Paso 7: Creación de la Cuenta de Administrador (Superusuario)")
    pdf.body_paragraph("Se dio de alta el superusuario 'admin' para permitir el acceso al panel administrativo integrado de Django.")
    pdf.add_screenshot("07_crear_superusuario.png", "Figura 7: Creación del superusuario administrativo.")

    pdf.section_title("Paso 8: Batería de Pruebas Unitarias Automatizadas")
    pdf.body_paragraph("Se desarrollaron 7 pruebas automatizadas que verifican la creación de modelos, validaciones numéricas y todas las vistas del CRUD.")
    pdf.add_screenshot("08_ejecutar_pruebas.png", "Figura 8: Resultado 100% satisfactorio (OK) de las 7 pruebas unitarias del proyecto.")

    pdf.add_page()
    pdf.section_title("Paso 9: Arranque del Servidor de Desarrollo")
    pdf.body_paragraph("Se puso en ejecución el servidor local HTTP en el puerto 8000 para habilitar la interfaz de navegación web.")
    pdf.add_screenshot("09_arranque_servidor.png", "Figura 9: Servidor de desarrollo Django escuchando en http://127.0.0.1:8000/.")

    # =========================================================================
    # SECCIÓN 4: VERIFICACIÓN DEL CRUD WEB CON CAPTURAS DE NAVEGADOR
    # =========================================================================
    pdf.add_page()
    pdf.chapter_title("4.", "Verificación y Pruebas de Funcionamiento Web (CRUD)")
    pdf.body_paragraph(
        "Se procedió a validar cada una de las 4 funciones obligatorias especificadas en el proyecto "
        "(Visualizar, Agregar, Editar y Borrar) a través de la interfaz web responsiva construida con Bootstrap 5."
    )

    pdf.section_title("4.1. Función: Visualizar (Dashboard Principal y Tabla SQLite)")
    pdf.body_paragraph(
        "Muestra el resumen ejecutivo con tarjetas de métricas agregadas (total de equipos, suma concurrente de núcleos cores, "
        "TeraFLOPS acumulados y almacenamiento en TB), el podio de honor de los tres primeros lugares mundiales y la tabla de registros completa."
    )
    pdf.add_screenshot("10_web_dashboard.png", "Figura 10: Interfaz Web - Dashboard general y tabla de supercomputadoras en SQLite.", width=170)

    pdf.add_page()
    pdf.section_title("4.2. Función: Visualizar (Ficha Técnica Detallada)")
    pdf.body_paragraph(
        "Al presionar el botón 'Visualizar', el usuario accede a una vista pormenorizada con las métricas del sistema, "
        "conversiones automáticas a PetaFLOPS y ExaFLOPS, y los metadatos de auditoría almacenados en SQLite."
    )
    pdf.add_screenshot("11_web_detalle.png", "Figura 11: Interfaz Web - Ficha técnica completa de una supercomputadora.", width=170)

    pdf.add_page()
    pdf.section_title("4.3. Función: Agregar (Formulario de Registro)")
    pdf.body_paragraph(
        "El formulario de captura permite registrar nuevos sistemas de cómputo validando tipos de datos, valores numéricos mínimos "
        "y campos obligatorios con retroalimentación visual inmediata."
    )
    pdf.add_screenshot("12_web_agregar_formulario.png", "Figura 12: Interfaz Web - Formulario para agregar una nueva supercomputadora.", width=170)

    pdf.add_page()
    pdf.section_title("4.4. Función: Editar (Actualización de Especificaciones)")
    pdf.body_paragraph(
        "Permite modificar en cualquier momento las características de un equipo existente (p. ej. ampliación de RAM, almacenamiento o actualización de SO) "
        "sin perder la consistencia relacional en SQLite."
    )
    pdf.add_screenshot("13_web_editar_formulario.png", "Figura 13: Interfaz Web - Formulario de edición con datos precargados.", width=170)

    pdf.add_page()
    pdf.section_title("4.5. Función: Borrar (Confirmación Segura de Eliminación)")
    pdf.body_paragraph(
        "Para evitar borrados accidentales de información crítica, el sistema solicita confirmación explícita antes de ejecutar "
        "la eliminación permanente del registro en SQLite."
    )
    pdf.add_screenshot("14_web_confirmar_eliminar.png", "Figura 14: Interfaz Web - Ventana de confirmación previa a la eliminación física.", width=150)

    pdf.section_title("4.6. Panel Administrativo Oficial de Django (/admin/)")
    pdf.body_paragraph(
        "Se personalizó el panel de administración con capacidades de búsqueda, filtrado por país y sistema operativo, "
        "y agrupación lógica de campos técnicos."
    )
    pdf.add_screenshot("16_web_admin_listado.png", "Figura 15: Interfaz Web - Panel administrativo con filtros y listado.", width=170)

    # =========================================================================
    # SECCIÓN 5: CONCLUSIONES Y ENLACES
    # =========================================================================
    pdf.add_page()
    pdf.chapter_title("5.", "Conclusiones y Enlaces de Interés")
    pdf.body_paragraph(
        "Conclusiones del Proyecto:\n"
        "1. Concurrencia y Supercómputo: El modelado de sistemas con más de 11 millones de núcleos concurrentes en una base de datos relacional "
        "evidencia la importancia de diseñar estructuras de datos robustas y tipos numéricos adecuados (BigIntegerField y DecimalField) para evitar desbordamientos.\n"
        "2. Productividad del Framework Django: El patrón MVT (Modelo-Vista-Template) aceleró la construcción del CRUD completo, proveyendo seguridad nativa contra inyecciones SQL y CSRF.\n"
        "3. Calidad y Verificación: Las pruebas unitarias automatizadas y las capturas integrales garantizan que el sistema satisface al 100% los requerimientos de la asignatura.\n"
    )

    pdf.section_title("Enlaces de Interés Citados en la Consigna:")
    enlaces = [
        ("Visual Studio Code", "https://code.visualstudio.com/"),
        ("¿Qué es Django y por qué importa? - Django y DRF", "https://www.youtube.com/watch?v=B8OlRdYwNlA"),
        ("Django Portafolio, Ejemplo Práctico", "https://www.youtube.com/watch?v=zBjMF6je24U"),
        ("Django REST Framework y React CRUD", "https://www.youtube.com/watch?v=38XWpyEK8IY"),
        ("Crea una agenda virtual con Django", "https://www.youtube.com/watch?v=EQ-kqDmfUoM"),
        ("TOP500 List (Supercomputadoras Globales)", "https://top500.org/"),
    ]
    pdf.set_font("ArialUnicode", "", 9)
    for nombre, url in enlaces:
        pdf.set_text_color(15, 23, 42)
        pdf.cell(80, 5.5, f"- {nombre}: ", align="L")
        pdf.set_text_color(13, 110, 253)
        pdf.cell(0, 5.5, url, align="L", new_x="LMARGIN", new_y="NEXT")

    pdf.output(OUTPUT_PDF)
    print(f"[OK] Reporte PDF compilado y generado con éxito: {OUTPUT_PDF}")


if __name__ == "__main__":
    generar_pdf()
