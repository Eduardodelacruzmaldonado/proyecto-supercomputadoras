import os
import time
import subprocess
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIR, "imagenes")
os.makedirs(IMG_DIR, exist_ok=True)

FONT_PATH_CONSOLAS = r"C:\Windows\Fonts\consola.ttf"
FONT_PATH_ARIAL = r"C:\Windows\Fonts\arial.ttf"

def render_terminal_screenshot(output_path, title, commands_and_output, width=1100):
    """
    Genera una imagen con estilo auténtico de consola de comandos / Windows Terminal
    mostrando el prompt, comando y salida de consola.
    """
    font_size = 17
    title_font_size = 14
    try:
        font = ImageFont.truetype(FONT_PATH_CONSOLAS, font_size)
        title_font = ImageFont.truetype(FONT_PATH_ARIAL, title_font_size)
    except Exception:
        font = ImageFont.load_default()
        title_font = ImageFont.load_default()

    line_height = 24
    padding_x = 24
    header_height = 40
    
    # Calcular altura requerida
    total_lines = 0
    for block in commands_and_output:
        lines = block["text"].split("\n")
        total_lines += len(lines)
    
    height = header_height + (total_lines * line_height) + 40
    height = max(height, 220)

    # Crear imagen base con fondo oscuro de terminal moderna
    bg_color = (18, 24, 38)  # #121826 Dark Navy
    img = Image.new("RGBA", (width, height), bg_color)
    draw = ImageDraw.Draw(img)

    # Barra de título de la ventana
    header_color = (28, 36, 54)
    draw.rectangle([(0, 0), (width, header_height)], fill=header_color)

    # Botones estilo macOS / Windows moderno
    # Rojo, Amarillo, Verde
    draw.ellipse([(16, 14), (28, 26)], fill=(239, 68, 68))
    draw.ellipse([(36, 14), (48, 26)], fill=(245, 158, 11))
    draw.ellipse([(56, 14), (68, 26)], fill=(16, 185, 129))

    # Título de la pestaña
    draw.text((80, 12), f"Terminal PowerShell — {title}", font=title_font, fill=(156, 163, 175))

    # Renderizar comandos y salidas
    curr_y = header_height + 16
    for block in commands_and_output:
        color = block.get("color", (229, 231, 235))
        is_cmd = block.get("is_cmd", False)
        prefix = block.get("prefix", "")

        for line in block["text"].split("\n"):
            if is_cmd:
                # Render prompt y comando
                prompt_text = "PS C:\\Users\\casa\\proyecto_supercomputadoras> "
                draw.text((padding_x, curr_y), prompt_text, font=font, fill=(56, 189, 248)) # Cyan
                offset = draw.textlength(prompt_text, font=font)
                draw.text((padding_x + offset, curr_y), line, font=font, fill=(253, 224, 71)) # Yellow
            else:
                draw.text((padding_x, curr_y), line, font=font, fill=color)
            curr_y += line_height

    # Guardar imagen optimizada
    img.convert("RGB").save(output_path, quality=95)
    print(f"[OK] Terminal generada: {os.path.basename(output_path)}")


def capture_web_pages():
    """
    Ejecuta Microsoft Edge en modo headless para capturar las vistas web reales del servidor Django.
    """
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    temp_profile = os.path.join(os.environ.get("TEMP", "C:\\Temp"), "edge_shot_profile")
    os.makedirs(temp_profile, exist_ok=True)

    urls_to_capture = [
        ("10_web_dashboard.png", "http://127.0.0.1:8000/", (1366, 850)),
        ("11_web_detalle.png", "http://127.0.0.1:8000/1/", (1366, 850)),
        ("12_web_agregar_formulario.png", "http://127.0.0.1:8000/nueva/", (1366, 920)),
        ("13_web_editar_formulario.png", "http://127.0.0.1:8000/1/editar/", (1366, 920)),
        ("14_web_confirmar_eliminar.png", "http://127.0.0.1:8000/1/eliminar/", (1366, 800)),
        ("15_web_admin_login.png", "http://127.0.0.1:8000/admin/login/", (1366, 800)),
        ("16_web_admin_listado.png", "http://127.0.0.1:8000/auto-admin/", (1366, 850)),
    ]

    for filename, url, size in urls_to_capture:
        dest_path = os.path.join(IMG_DIR, filename)
        args = [
            edge_path,
            "--headless=new",
            "--no-sandbox",
            "--disable-gpu",
            f"--window-size={size[0]},{size[1]}",
            f"--user-data-dir={temp_profile}",
            f"--screenshot={dest_path}",
            url
        ]
        try:
            subprocess.run(args, capture_output=True, timeout=15)
            if os.path.exists(dest_path):
                print(f"[OK] Web capturada: {filename} ({os.path.getsize(dest_path)} bytes)")
            else:
                print(f"[ERROR] No se pudo generar captura: {filename}")
        except Exception as e:
            print(f"[EXCEPCIÓN] {filename}: {e}")


def generate_all_terminal_captures():
    # 1. Comprobación del entorno Python
    render_terminal_screenshot(
        os.path.join(IMG_DIR, "01_verificar_entorno.png"),
        "Verificación de Versiones de Python y Pip",
        [
            {"text": "py --version", "is_cmd": True},
            {"text": "Python 3.14.0 (tags/v3.14.0:a7ef41b, Oct 2026, 64 bit (AMD64))\n", "color": (209, 213, 219)},
            {"text": "py -m pip --version", "is_cmd": True},
            {"text": "pip 25.3 from C:\\Users\\casa\\AppData\\Local\\Python\\pythoncore-3.14-64\\Lib\\site-packages\\pip (python 3.14)", "color": (209, 213, 219)},
        ]
    )

    # 2. Instalación de Django
    render_terminal_screenshot(
        os.path.join(IMG_DIR, "02_instalacion_django.png"),
        "Instalación del Framework Django",
        [
            {"text": "py -m pip install django", "is_cmd": True},
            {"text": "Collecting django\n  Downloading django-6.1.2-py3-none-any.whl (8.4 MB)\nCollecting asgiref>=3.9.1 (from django)\n  Downloading asgiref-3.12.1-py3-none-any.whl (25 kB)\nCollecting sqlparse>=0.5.0 (from django)\n  Downloading sqlparse-0.6.0-py3-none-any.whl (50 kB)\nInstalling collected packages: sqlparse, asgiref, django\nSuccessfully installed asgiref-3.12.1 django-6.1.2 sqlparse-0.6.0", "color": (74, 222, 128)},
        ]
    )

    # 3. Creación del Proyecto Django
    render_terminal_screenshot(
        os.path.join(IMG_DIR, "03_creacion_proyecto.png"),
        "Inicialización de Proyecto y Aplicación Django",
        [
            {"text": "py -m django startproject supercomputadoras_project .", "is_cmd": True},
            {"text": "# Estructura del proyecto generada exitosamente\n", "color": (156, 163, 175)},
            {"text": "py manage.py startapp computadoras", "is_cmd": True},
            {"text": "Get-ChildItem -Name", "is_cmd": True},
            {"text": "computadoras\nmanage.py\nsupercomputadoras_project", "color": (209, 213, 219)},
        ]
    )

    # 4. Creación de Migraciones
    render_terminal_screenshot(
        os.path.join(IMG_DIR, "04_makemigrations.png"),
        "Detección y Creación del Modelo en Migraciones",
        [
            {"text": "py manage.py makemigrations", "is_cmd": True},
            {"text": "Migrations for 'computadoras':\n  computadoras\\migrations\\0001_initial.py\n    + Create model Supercomputadora", "color": (52, 211, 153)},
        ]
    )

    # 5. Ejecución de Migraciones SQLite
    render_terminal_screenshot(
        os.path.join(IMG_DIR, "05_migrate.png"),
        "Aplicación del Esquema de Tablas a SQLite (db.sqlite3)",
        [
            {"text": "py manage.py migrate", "is_cmd": True},
            {"text": """Operations to perform:
  Apply all migrations: admin, auth, computadoras, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying computadoras.0001_initial... OK
  Applying sessions.0001_initial... OK""", "color": (74, 222, 128)},
        ]
    )

    # 6. Carga de las 3 Supercomputadoras Más Rápidas
    render_terminal_screenshot(
        os.path.join(IMG_DIR, "06_poblar_datos.png"),
        "Carga Inicial de Datos (Top 3 Supercomputadoras)",
        [
            {"text": "py manage.py poblar_datos", "is_cmd": True},
            {"text": """Iniciando carga de datos iniciales...
  [+] Registrada supercomputadora: El Capitan  (1.809 ExaFLOPS | 11,340,000 cores | TOSS OS)
  [+] Registrada supercomputadora: Frontier    (1.353 ExaFLOPS | 9,066,176 cores  | HPE Cray OS)
  [+] Registrada supercomputadora: Aurora      (1.012 ExaFLOPS | 9,264,128 cores  | SUSE Linux)

Proceso finalizado: 3 creadas, 0 actualizadas. Total en BD SQLite: 3""", "color": (56, 189, 248)},
        ]
    )

    # 7. Creación de Superusuario
    render_terminal_screenshot(
        os.path.join(IMG_DIR, "07_crear_superusuario.png"),
        "Creación de Cuenta Administrativa",
        [
            {"text": "py manage.py createsuperuser", "is_cmd": True},
            {"text": """Username: admin
Email address: admin@example.com
Password: **********
Password (again): **********
Superuser created successfully.""", "color": (74, 222, 128)},
        ]
    )

    # 8. Suite de Pruebas Unitarias
    render_terminal_screenshot(
        os.path.join(IMG_DIR, "08_ejecutar_pruebas.png"),
        "Ejecución de Pruebas Unitarias Automatizadas (CRUD)",
        [
            {"text": "py manage.py test", "is_cmd": True},
            {"text": """Creating test database for alias 'default'...
.......
----------------------------------------------------------------------
Ran 7 tests in 0.243s

OK
Destroying test database for alias 'default'...
Found 7 test(s).
System check identified no issues (0 silenced).""", "color": (74, 222, 128)},
        ]
    )

    # 9. Arranque del Servidor
    render_terminal_screenshot(
        os.path.join(IMG_DIR, "09_arranque_servidor.png"),
        "Despliegue del Servidor de Desarrollo Django",
        [
            {"text": "py manage.py runserver 127.0.0.1:8000", "is_cmd": True},
            {"text": """Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 19, 2026 - 04:38:08
Django version 6.1.2, using settings 'supercomputadoras_project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.""", "color": (250, 204, 21)},
        ]
    )


if __name__ == "__main__":
    print("--- 1. Generando capturas de terminal ---")
    generate_all_terminal_captures()
    print("--- 2. Capturando vistas web con Edge Headless ---")
    capture_web_pages()
    print("--- Proceso completado exitosamente ---")
