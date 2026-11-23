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
            self.set_text_color(71, 85, 105)
            self.cell(0, 8, "COMPUTACIÓN CONCURRENTE | PROYECTO FINAL", align="L")
            self.cell(0, 8, "LICENCIATURA EN CIENCIA DE DATOS", align="R")
            self.ln(9)
            self.set_draw_color(203, 213, 225)
            self.set_line_width(0.3)
            self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
            self.ln(4)

    def footer(self):
        if self.page_no() > 1:
            self.set_y(-15)
            self.set_font("ArialUnicode", "I", 8)
            self.set_text_color(148, 163, 184)
            self.cell(0, 10, "Prof. Adrián Durán Chavesti - Base de Datos Web", align="L")
            self.cell(0, 10, f"Página {self.page_no()}", align="C")
            self.cell(0, 10, "Django & SQLite (CRUD)", align="R")

    def chapter_title(self, num_str, title_str):
        self.set_font("ArialUnicode", "B", 13.5)
        self.set_text_color(24, 76, 120)
        self.set_fill_color(241, 245, 249)
        self.ln(3)
        self.cell(0, 8.5, f"  {num_str} {title_str}", fill=True, new_x="LMARGIN", new_y="NEXT")
        self.ln(3)

    def section_title(self, title_str):
        self.set_font("ArialUnicode", "B", 11)
        self.set_text_color(15, 23, 42)
        self.ln(2)
        self.cell(0, 6.5, title_str, new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

    def subsection_title(self, title_str):
        self.set_font("ArialUnicode", "B", 9.8)
        self.set_text_color(30, 41, 59)
        self.ln(1.5)
        self.cell(0, 5.5, title_str, new_x="LMARGIN", new_y="NEXT")
        self.ln(0.5)

    def body_paragraph(self, text):
        self.set_font("ArialUnicode", "", 9.2)
        self.set_text_color(51, 65, 85)
        self.multi_cell(0, 5.0, text)
        self.ln(2)

    def add_screenshot(self, img_filename, caption_text, width=160):
        img_path = os.path.join(IMG_DIR, img_filename)
        if os.path.exists(img_path):
            if self.get_y() > 205:
                self.add_page()
            self.image(img_path, x=(self.w - width) / 2, w=width)
            self.ln(2)
            self.set_font("ArialUnicode", "I", 8.0)
            self.set_text_color(100, 116, 139)
            self.cell(0, 4.5, caption_text, align="C", new_x="LMARGIN", new_y="NEXT")
            self.ln(3)
        else:
            self.set_font("ArialUnicode", "I", 9)
            self.set_text_color(220, 38, 38)
            self.cell(0, 6, f"[Captura pendiente: {img_filename}]", new_x="LMARGIN", new_y="NEXT")
            self.ln(2)


def generar_pdf():
    pdf = PDFReporte(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=True, margin=18)
    pdf.set_margins(18, 18, 18)

    # =========================================================================
    # PORTADA
    # =========================================================================
    pdf.add_page()
    pdf.set_fill_color(30, 41, 59)
    pdf.rect(0, 0, 210, 14, style="F")

    pdf.set_y(24)
    pdf.set_font("ArialUnicode", "B", 14.5)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(0, 7, "LICENCIATURA EN CIENCIA DE DATOS", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("ArialUnicode", "B", 12.0)
    pdf.set_text_color(24, 76, 120)
    pdf.cell(0, 6, "COMPUTACIÓN CONCURRENTE", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)

    pdf.set_draw_color(24, 76, 120)
    pdf.set_line_width(1.2)
    pdf.line(20, pdf.get_y(), 190, pdf.get_y())
    pdf.ln(8)

    pdf.set_font("ArialUnicode", "B", 16)
    pdf.set_text_color(15, 23, 42)
    pdf.multi_cell(
        0, 7.5,
        "PROYECTO FINAL:\nDiseño y Gestión de una Base de Datos SQLite con Acceso Web usando Django en Python",
        align="C"
    )
    pdf.ln(2)
    pdf.set_font("ArialUnicode", "", 10.5)
    pdf.set_text_color(71, 85, 105)
    pdf.cell(0, 5.5, "Modelado de Supercomputadoras a Exaescala y Operaciones CRUD", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)

    pdf.set_draw_color(203, 213, 225)
    pdf.set_line_width(0.5)
    pdf.line(40, pdf.get_y(), 170, pdf.get_y())
    pdf.ln(8)

    # Cuadro institucional
    pdf.set_fill_color(248, 250, 252)
    pdf.set_draw_color(203, 213, 225)
    box_y = pdf.get_y()
    pdf.rect(20, box_y, 170, 72, style="DF")

    pdf.set_y(box_y + 5)
    pdf.set_font("ArialUnicode", "B", 9.5)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(85, 5.5, "   Docente:", align="L")
    pdf.cell(85, 5.5, "Fecha de Entrega:   ", align="R", new_x="LMARGIN", new_y="NEXT")

    pdf.set_font("ArialUnicode", "", 9.0)
    pdf.set_text_color(51, 65, 85)
    pdf.cell(85, 5.0, "   Esp. Adrián Durán Chavesti", align="L")
    pdf.cell(85, 5.0, "Jueves 26 de Noviembre   ", align="R", new_x="LMARGIN", new_y="NEXT")

    pdf.ln(2)
    pdf.set_font("ArialUnicode", "B", 9.5)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(85, 5.5, "   Asignatura:", align="L")
    pdf.cell(85, 5.5, "Evaluación:   ", align="R", new_x="LMARGIN", new_y="NEXT")

    pdf.set_font("ArialUnicode", "", 9.0)
    pdf.set_text_color(51, 65, 85)
    pdf.cell(85, 5.0, "   Computación Concurrente", align="L")
    pdf.cell(85, 5.0, "10 puntos (Exposición y Pruebas)   ", align="R", new_x="LMARGIN", new_y="NEXT")

    pdf.ln(2)
    pdf.set_font("ArialUnicode", "B", 9.5)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(0, 5.5, "   Tema de Investigación:", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("ArialUnicode", "", 9.0)
    pdf.set_text_color(51, 65, 85)
    pdf.cell(0, 5.0, "   Las 3 Supercomputadoras más Rápidas del Mundo: Arquitectura Concurrente y Persistencia Web", new_x="LMARGIN", new_y="NEXT")

    pdf.set_y(box_y + 82)
    pdf.set_fill_color(241, 245, 249)
    pdf.set_draw_color(203, 213, 225)
    pdf.rect(20, pdf.get_y(), 170, 26, style="DF")
    pdf.set_y(pdf.get_y() + 3.0)
    pdf.set_font("ArialUnicode", "B", 8.8)
    pdf.set_text_color(24, 76, 120)
    pdf.cell(0, 4.8, "Objetivo General Planteado en la Rúbrica:", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("ArialUnicode", "I", 8.5)
    pdf.set_text_color(51, 65, 85)
    pdf.multi_cell(
        0, 4.3,
        '"Con ayuda del framework Django crear y gestionar una base de datos SQLite con el lenguaje de programación Python, '
        'registrando la información relevante de las 3 computadoras más rápidas del mundo y habilitando las funciones de Agregar, Editar, Borrar y Visualizar."',
        align="C"
    )

    pdf.set_y(260)
    pdf.set_font("ArialUnicode", "B", 9.0)
    pdf.set_text_color(100, 116, 139)
    pdf.cell(0, 5, "LICENCIATURA EN CIENCIA DE DATOS - SEMESTRE ACADÉMICO 2026-II", align="C")

    # =========================================================================
    # SECCIÓN 1: INTRODUCCIÓN Y FUNDAMENTOS
    # =========================================================================
    pdf.add_page()
    pdf.chapter_title("1.", "Introducción y Marco de Computación Concurrente")
    pdf.body_paragraph(
        "En la formación de Ciencia de Datos, el procesamiento paralelo y concurrente es un conocimiento esencial. "
        "El entrenamiento de modelos fundacionales de aprendizaje profundo, el análisis genómico a gran escala y "
        "las simulaciones de fluidos magnéticos requieren infraestructuras distribuidas que superan los límites de cualquier "
        "procesador secuencial individual. Por esta razón, el estudio de la concurrencia abarca desde el silicio de los aceleradores "
        "hasta los protocolos de persistencia en bases de datos relacionales."
    )
    pdf.body_paragraph(
        "Este proyecto final integra ambas dimensiones de la materia:\n"
        "  1. Concurrencia a nivel de arquitectura física (Supercómputo a Exaescala): Se modelan y registran las especificaciones "
        "técnicas de los 3 sistemas informáticos más veloces del planeta según el ranking oficial TOP500, cuyos clústeres coordinan "
        "más de 11.3 millones de núcleos de procesamiento concurrentes bajo modelos de memoria híbrida (MPI + OpenMP/HIP/SYCL).\n"
        "  2. Concurrencia a nivel de software y persistencia (Django y SQLite): Se construye una aplicación web bajo el patrón MVT, "
        "evaluando cómo el motor relacional SQLite gestiona las operaciones concurrentes de lectura y escritura mediante cerrojos a nivel de archivo "
        "(SHARED, RESERVED, EXCLUSIVE) y modo WAL (Write-Ahead Logging), garantizando la consistencia ACID en operaciones CRUD."
    )

    pdf.section_title("Los 7 Parámetros Requeridos en la Base de Datos")
    pdf.body_paragraph(
        "Para dar cumplimiento estricto a las especificaciones de la consigna, la tabla relacional se estructuró con los siguientes 7 campos:\n"
        "  - Nombre: Identificador formal del sistema de supercómputo (ej. El Capitan, Frontier, Aurora).\n"
        "  - País de origen: Centro o laboratorio internacional sede.\n"
        "  - Número de cores: Total de núcleos concurrentes (CPU tradicionales + aceleradores GPU).\n"
        "  - Cantidad de RAM (TB): Memoria principal distribuida en Terabytes.\n"
        "  - Almacenamiento (TB): Capacidad total del sistema de archivos paralelo en Terabytes.\n"
        "  - TeraFLOPS: Capacidad de cómputo en precisión doble FP64 (Linpack HPL).\n"
        "  - Sistema operativo: Distribución Unix/Linux especializada para clústeres masivos."
    )

    # =========================================================================
    # SECCIÓN 2: LAS 3 SUPERCOMPUTADORAS MÁS RÁPIDAS
    # =========================================================================
    pdf.chapter_title("2.", "Las 3 Supercomputadoras más Rápidas del Mundo (TOP500)")
    pdf.body_paragraph(
        "De acuerdo con los datos oficiales de la lista TOP500, los tres primeros puestos a nivel mundial operan "
        "en la frontera de la Exaescala (superando 10^18 operaciones de punto flotante por segundo sostenidas):"
    )

    # Tabla comparativa
    pdf.set_font("ArialUnicode", "B", 7.5)
    pdf.set_fill_color(30, 41, 59)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(32, 6.0, "Parámetro", border=1, fill=True)
    pdf.cell(46, 6.0, "#1 El Capitan (EE.UU.)", border=1, fill=True)
    pdf.cell(46, 6.0, "#2 Frontier (EE.UU.)", border=1, fill=True)
    pdf.cell(46, 6.0, "#3 Aurora (EE.UU.)", border=1, fill=True, new_x="LMARGIN", new_y="NEXT")

    tabla_datos = [
        ("Institución", "Lawrence Livermore Lab", "Oak Ridge Nat. Lab", "Argonne Nat. Lab"),
        ("Núcleos (Cores)", "11,340,000 cores", "9,066,176 cores", "9,264,128 cores"),
        ("Memoria RAM", "5,437 TB (~5.44 PB)", "9,200 TB (~9.20 PB)", "10,900 TB (~10.90 PB)"),
        ("Almacenamiento", "40,000 TB (40 PB)", "70,000 TB (70 PB Orion)", "220,000 TB (220 PB DAOS)"),
        ("TeraFLOPS (Rmax)", "1,809,000.00 TFLOPS", "1,353,000.00 TFLOPS", "1,012,000.00 TFLOPS"),
        ("Rendimiento ExaFLOPS", "1.809 EFLOPS Rmax", "1.353 EFLOPS Rmax", "1.012 EFLOPS Rmax"),
        ("Rendimiento Pico", "2.746 EFLOPS Rpeak", "2.054 EFLOPS Rpeak", "1.980 EFLOPS Rpeak"),
        ("Sistema Operativo", "TOSS (Tri-Lab / RHEL)", "HPE Cray OS (SUSE)", "SUSE Linux Enterprise"),
        ("Arquitectura Paralela", "HPE Cray EX / MI300A APU", "HPE Cray EX / MI250X GPU", "Intel Xeon Max + GPUs Max"),
        ("Red de Interconexión", "Slingshot-11 (200 Gbps)", "Slingshot-11 (200 Gbps)", "Slingshot-11 (200 Gbps)"),
    ]

    pdf.set_font("ArialUnicode", "", 7.3)
    pdf.set_text_color(30, 41, 59)
    alt = False
    for fila in tabla_datos:
        pdf.set_fill_color(248, 250, 252) if alt else pdf.set_fill_color(255, 255, 255)
        pdf.cell(32, 5.0, f" {fila[0]}", border=1, fill=True)
        pdf.cell(46, 5.0, f" {fila[1]}", border=1, fill=True)
        pdf.cell(46, 5.0, f" {fila[2]}", border=1, fill=True)
        pdf.cell(46, 5.0, f" {fila[3]}", border=1, fill=True, new_x="LMARGIN", new_y="NEXT")
        alt = not alt

    pdf.ln(3)
    pdf.subsection_title("Arquitectura y Aspectos Técnicos Destacados")
    pdf.body_paragraph(
        "• El Capitan: Desarrollado para el Laboratorio Lawrence Livermore, implementa la APU AMD Instinct MI300A, "
        "la cual integra 24 núcleos CPU Zen 4 y 228 núcleos GPU CDNA 3 sobre un único encapsulado con 128 GB de memoria HBM3 "
        "unificada (5.3 TB/s de ancho de banda). Esto elimina por completo el cuello de botella PCIe en la comunicación concurrente CPU-GPU.\n"
        "• Frontier: Ubicado en Oak Ridge, utiliza el sistema de almacenamiento paralelo Orion basado en Lustre con 700 PB brutos "
        "(70 PB flash) y un ancho de banda sostenido de 5 TB/s, permitiendo a millones de hilos escribir checkpoints en paralelo.\n"
        "• Aurora: Ubicado en Argonne, opera con 10,624 nodos equipados con CPUs Intel Xeon Max (con HBM2e integrado) y GPUs Intel Data Center Max. "
        "Emplea el modelo de concurrencia Intel oneAPI / SYCL y el sistema de almacenamiento de objetos asíncrono DAOS (220 PB flash)."
    )

    # =========================================================================
    # SECCIÓN 3: CONCURRENCIA EN BASE DE DATOS Y EN DJANGO
    # =========================================================================
    pdf.add_page()
    pdf.chapter_title("3.", "Manejo de Concurrencia en SQLite y Django")
    pdf.body_paragraph(
        "Durante la fase de diseño e implementación del software, se profundizaron los siguientes aspectos de concurrencia y persistencia:\n"
        "  1. Cerrojos de SQLite: SQLite utiliza un bloqueo a nivel de archivo. Admite lecturas simultáneas mediante cerrojos compartidos (SHARED locks). "
        "Al ejecutar una inserción o actualización, solicita un cerrojo exclusivo (EXCLUSIVE lock). Si otro hilo está escribiendo, los demás escritores "
        "deben esperar a que se libere el cerrojo o se agote el timeout (busy_timeout).\n"
        "  2. Modo WAL (Write-Ahead Logging): Al habilitar el modo WAL en SQLite, las modificaciones se escriben en un archivo auxiliar (.sqlite3-wal) "
        "en lugar de sobreescribir inmediatamente la base de datos principal, permitiendo que múltiples lectores consulten la base de datos "
        "mientras un hilo escribe en el registro auxiliar sin bloquearse mutuamente.\n"
        "  3. Prevención de Desbordamiento de Enteros: La cantidad de núcleos de El Capitan (11,340,000) requirió el uso de PositiveBigIntegerField "
        "en lugar de IntegerField estándar de 32 bits, garantizando que el almacenamiento de 64 bits soporte futuras ampliaciones de exaescala.\n"
        "  4. Precisión Numérica vs Float: Se seleccionó DecimalField(max_digits=16, decimal_places=2) para TeraFLOPS y Terabytes, evitando "
        "los errores de redondeo de punto flotante binario (IEEE 754) que suelen presentarse con FloatField en cálculos agregados."
    )

    pdf.section_title("Arquitectura MVT y Vistas Genéricas")
    pdf.body_paragraph(
        "El proyecto adoptó vistas basadas en clases (CBVs) de Django: ListView para el catálogo general con agregaciones en SQL (Sum, Count), "
        "DetailView para la ficha técnica, CreateView para la inserción, UpdateView para la modificación y DeleteView para el borrado seguro. "
        "Todas las transacciones POST cuentan con protección nativa contra ataques CSRF mediante tokens criptográficos."
    )

    # =========================================================================
    # SECCIÓN 4: BITÁCORA DE LABORATORIO
    # =========================================================================
    pdf.chapter_title("4.", "Bitácora de Laboratorio: Comandos Ejecutados")
    pdf.body_paragraph(
        "A continuación se presenta el registro secuencial de los comandos ejecutados en consola de PowerShell para inicializar, "
        "configurar, migrar y verificar el proyecto, junto con sus capturas de pantalla de terminal."
    )

    pdf.section_title("Paso 1: Verificación de Versiones de Python y Pip")
    pdf.body_paragraph("Comprobamos la versión del entorno del intérprete Python y la disponibilidad del instalador de paquetes pip.")
    pdf.add_screenshot("01_verificar_entorno.png", "Figura 1: Comprobación del intérprete Python y gestor pip en consola.")

    pdf.section_title("Paso 2: Instalación de Dependencias con Pip")
    pdf.body_paragraph("Descargamos e instalamos el framework Django junto a sus librerías de soporte asíncrono y consultas SQL.")
    pdf.add_screenshot("02_instalacion_django.png", "Figura 2: Instalación de paquetes con py -m pip install django.")

    pdf.add_page()
    pdf.section_title("Paso 3: Creación del Proyecto y la Aplicación")
    pdf.body_paragraph("Inicializamos la estructura base con startproject y creamos la aplicación interna computadoras con startapp.")
    pdf.add_screenshot("03_creacion_proyecto.png", "Figura 3: Creación del proyecto supercomputadoras_project y la app computadoras.")

    pdf.section_title("Paso 4: Detección del Modelo y Generación de Migraciones")
    pdf.body_paragraph("El ORM analizó models.py y generó el archivo de migración 0001_initial.py para estructurar la tabla en SQLite.")
    pdf.add_screenshot("04_makemigrations.png", "Figura 4: Detección del modelo y creación del archivo de migración inicial.")

    pdf.add_page()
    pdf.section_title("Paso 5: Aplicación de Migraciones a SQLite (migrate)")
    pdf.body_paragraph("Ejecutamos migrate para materializar el esquema relacional en el archivo físico db.sqlite3.")
    pdf.add_screenshot("05_migrate.png", "Figura 5: Aplicación de las migraciones sobre la base de datos db.sqlite3.")

    pdf.section_title("Paso 6: Poblado Automático de las 3 Supercomputadoras")
    pdf.body_paragraph("Diseñamos un comando de gestión personalizado (poblar_datos.py) para sembrar los registros del TOP500 de forma idempotente.")
    pdf.add_screenshot("06_poblar_datos.png", "Figura 6: Ejecución del comando personalizado para poblar la base de datos.")

    pdf.add_page()
    pdf.section_title("Paso 7: Creación de la Cuenta de Administrador")
    pdf.body_paragraph("Generamos la cuenta del usuario admin para acceder al panel de administración oficial provisto por Django.")
    pdf.add_screenshot("07_crear_superusuario.png", "Figura 7: Creación de credenciales del superusuario en consola.")

    pdf.section_title("Paso 8: Batería de Pruebas Unitarias Automatizadas")
    pdf.body_paragraph("Ejecutamos 7 pruebas automatizadas que verifican cálculos de conversiones, validación de campos y respuestas HTTP 200/302 del CRUD.")
    pdf.add_screenshot("08_ejecutar_pruebas.png", "Figura 8: Suite de pruebas unitarias ejecutadas con éxito (100% OK).")

    pdf.add_page()
    pdf.section_title("Paso 9: Arranque del Servidor de Desarrollo Local")
    pdf.body_paragraph("Iniciamos el servidor de pruebas en el puerto 8000 mediante runserver, dejándolo listo para atender solicitudes en el navegador.")
    pdf.add_screenshot("09_arranque_servidor.png", "Figura 9: Servidor de desarrollo Django escuchando en http://127.0.0.1:8000/.")

    # =========================================================================
    # SECCIÓN 5: PRUEBAS DEL CRUD WEB
    # =========================================================================
    pdf.add_page()
    pdf.chapter_title("5.", "Pruebas de Funcionamiento de la Aplicación Web (CRUD)")
    pdf.body_paragraph(
        "Se comprobó el correcto funcionamiento de cada una de las 4 operaciones requeridas en la práctica (Visualizar, Agregar, Editar y Borrar) "
        "a través de la interfaz web responsiva construida con Bootstrap 5."
    )

    pdf.section_title("5.1. Función: Visualizar (Catálogo General y Métricas Agregadas)")
    pdf.body_paragraph(
        "La vista inicial (/) calcula de forma agregada los recursos de concurrencia: total de núcleos cores, "
        "TeraFLOPS acumulados y almacenamiento en Terabytes, junto a tarjetas destacadas del podio y la tabla general de registros en SQLite."
    )
    pdf.add_screenshot("10_web_dashboard.png", "Figura 10: Catálogo general con métricas de concurrencia agregada y tabla de datos.", width=170)

    pdf.add_page()
    pdf.section_title("5.2. Función: Visualizar (Ficha Técnica Detallada)")
    pdf.body_paragraph(
        "Al seleccionar 'Ficha Técnica', se despliegan las especificaciones completas del sistema seleccionado, "
        "calculando dinámicamente PetaFLOPS, ExaFLOPS y Petabytes, junto a los datos de auditoría de SQLite."
    )
    pdf.add_screenshot("11_web_detalle.png", "Figura 11: Ficha técnica individual de una supercomputadora con conversiones automáticas.", width=170)

    pdf.add_page()
    pdf.section_title("5.3. Función: Agregar (Formulario de Registro)")
    pdf.body_paragraph(
        "Permite registrar nuevos sistemas de cómputo validando campos requeridos, rangos numéricos positivos "
        "y la unicidad del nombre en la base de datos."
    )
    pdf.add_screenshot("12_web_agregar_formulario.png", "Figura 12: Formulario web para registrar una nueva supercomputadora.", width=170)

    pdf.add_page()
    pdf.section_title("5.4. Función: Editar (Actualización de Especificaciones)")
    pdf.body_paragraph(
        "Permite modificar en cualquier momento las especificaciones técnicas de un equipo existente con los datos precargados, "
        "preservando la integridad en SQLite."
    )
    pdf.add_screenshot("13_web_editar_formulario.png", "Figura 13: Formulario de edición con precarga de especificaciones.", width=170)

    pdf.add_page()
    pdf.section_title("5.5. Función: Borrar (Confirmación Segura de Eliminación)")
    pdf.body_paragraph(
        "Para prevenir la eliminación accidental de registros, el sistema solicita confirmación explícita mediante "
        "petición HTTP POST antes de ejecutar la sentencia DELETE en SQLite."
    )
    pdf.add_screenshot("14_web_confirmar_eliminar.png", "Figura 14: Vista de confirmación previa a la eliminación física de un registro.", width=150)

    pdf.section_title("5.6. Panel Administrativo Integrado de Django (/admin/)")
    pdf.body_paragraph(
        "Panel administrativo oficial con filtros por país, sistema operativo, caja de búsqueda en tiempo real y vista tabular de registros."
    )
    pdf.add_screenshot("16_web_admin_listado.png", "Figura 15: Panel administrativo de Django con filtros y listado.", width=170)

    # =========================================================================
    # SECCIÓN 6: CONCLUSIONES Y ENLACES
    # =========================================================================
    pdf.add_page()
    pdf.chapter_title("6.", "Conclusiones y Referencias Consultadas")
    pdf.body_paragraph(
        "Conclusiones del Proyecto:\n"
        "1. Concurrencia Masiva y Escalabilidad: El estudio de sistemas como El Capitan evidenció que la frontera del supercómputo "
        "exige arquitecturas de memoria unificada (APUs) y tipos de datos en software (PositiveBigIntegerField y DecimalField) "
        "diseñados para evitar desbordamientos numéricos y pérdida de precisión en aritmética de punto flotante.\n"
        "2. Comportamiento Concurrente de SQLite: SQLite demostró ser un motor eficiente para entornos de laboratorio y aplicaciones departamentales. "
        "Su modelo de cerrojos compartidos asegura lecturas concurrentes sin sobrecarga, mientras que su modo WAL reduce la contención de escritores.\n"
        "3. Mantenibilidad del Patrón MVT en Django: El uso de vistas genéricas basadas en clases (CBVs) simplificó la implementación de las 4 "
        "operaciones CRUD, garantizando protección nativa contra inyecciones SQL y ataques CSRF sin redundancia de código."
    )

    pdf.section_title("Enlaces de Interés Citados en la Práctica:")
    enlaces = [
        ("TOP500 List (Ranking Oficial de Supercomputadoras)", "https://top500.org/"),
        ("Documentación Oficial de Django", "https://docs.djangoproject.com/"),
        ("Visual Studio Code", "https://code.visualstudio.com/"),
        ("¿Qué es Django y por qué importa? - Django y DRF", "https://www.youtube.com/watch?v=B8OlRdYwNlA"),
        ("Django Portafolio, Ejemplo Práctico", "https://www.youtube.com/watch?v=zBjMF6je24U"),
        ("Django REST Framework y React CRUD", "https://www.youtube.com/watch?v=38XWpyEK8IY"),
        ("Crea una agenda virtual con Django", "https://www.youtube.com/watch?v=EQ-kqDmfUoM"),
    ]
    pdf.set_font("ArialUnicode", "", 8.5)
    for nombre, url in enlaces:
        pdf.set_text_color(15, 23, 42)
        pdf.cell(75, 5.0, f"- {nombre}: ", align="L")
        pdf.set_text_color(13, 110, 253)
        pdf.cell(0, 5.0, url, align="L", new_x="LMARGIN", new_y="NEXT")

    pdf.output(OUTPUT_PDF)
    print(f"[OK] Reporte PDF compilado y generado con éxito: {OUTPUT_PDF}")


if __name__ == "__main__":
    generar_pdf()
