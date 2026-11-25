# Proyecto Final: Base de Datos SQLite con Acceso Web en Django

**Licenciatura en Ciencia de Datos**  
**Asignatura:** Computación Concurrente  
**Docente:** Esp. Adrián Durán Chavesti  
**Ponderación:** 10 puntos (Exposición y Pruebas)

---

## 1. Descripción del Proyecto

Este proyecto consiste en el desarrollo de una aplicación web construida con el framework **Django** y base de datos relacional **SQLite**, diseñada para registrar, gestionar y consultar las especificaciones técnicas de las **3 computadoras más rápidas del mundo** registradas en el ranking global TOP500:

1. **El Capitan** (Estados Unidos — 1.809 ExaFLOPS / 11,340,000 cores concurrentes)
2. **Frontier** (Estados Unidos — 1.353 ExaFLOPS / 9,066,176 cores concurrentes)
3. **Aurora** (Estados Unidos — 1.012 ExaFLOPS / 9,264,128 cores concurrentes)

El proyecto aborda la computación concurrente desde dos perspectivas complementarias:
- **Concurrencia en la arquitectura de hardware:** Estudio de sistemas distribuidos a exaescala donde millones de núcleos (CPU y aceleradores GPU) computan simultáneamente mediante modelos híbridos de memoria (MPI + OpenMP / HIP / SYCL).
- **Concurrencia en el software y persistencia:** Análisis del comportamiento del motor SQLite y del servidor Django ante múltiples peticiones HTTP, el uso de cerrojos compartidos y exclusivos, y la implementación completa de las operaciones de persistencia **CRUD** (Crear, Leer, Actualizar y Eliminar).

---

## 2. Requerimientos de la Base de Datos

El modelo de datos relacional almacena los **7 campos obligatorios** solicitados en la rúbrica de evaluación:

| Campo | Tipo de Dato en Django | Justificación Técnica |
| :--- | :--- | :--- |
| **Nombre** | `CharField(max_length=120, unique=True)` | Identificador unívoco del sistema de supercómputo. |
| **País de origen** | `CharField(max_length=100)` | País donde se encuentra instalado el centro de cómputo. |
| **Número de cores** | `PositiveBigIntegerField` | Conteo total de núcleos concurrentes (CPU + aceleradores). Se usa un entero de 64 bits para soportar valores de exaescala (más de 11 millones de núcleos) sin desbordamiento. |
| **Cantidad de RAM (TB)** | `DecimalField(max_digits=12, decimal_places=2)` | Memoria RAM distribuida en Terabytes. Se emplea DecimalField para evitar errores de coma flotante binaria. |
| **Almacenamiento (TB)** | `DecimalField(max_digits=14, decimal_places=2)` | Capacidad total de almacenamiento paralelo en Terabytes. |
| **TeraFLOPS** | `DecimalField(max_digits=16, decimal_places=2)` | Rendimiento medido en billones de operaciones de punto flotante por segundo (FP64 Linpack). |
| **Sistema operativo** | `CharField(max_length=150)` | Distribución Linux especializada para computación concurrente (TOSS, HPE Cray OS, SUSE). |

Adicionalmente, el modelo incluye campos complementarios opcionales (`fabricante`, `institucion`, `ranking_posicion`, `fecha_registro`, `fecha_actualizacion`) y propiedades calculadas dinámicamente en memoria (`petaflops`, `exaflops`, `ram_petabytes`, `almacenamiento_petabytes`) para convertir automáticamente las magnitudes a órdenes de escala superiores.

---

## 3. Funcionalidades del Sistema Web (CRUD)

La aplicación implementa las cuatro operaciones fundamentales mediante vistas genéricas basadas en clases (*Class-Based Views*):

- **Visualizar (Read):**
  - **Listado general:** Tabla con todos los sistemas registrados y cálculo agregado en tiempo real mediante `aggregate()` (total de cores concurrentes, TeraFLOPS acumulados y almacenamiento en disco).
  - **Ficha técnica:** Vista de detalle individual con la conversión de unidades y datos de auditoría de la base de datos.
- **Agregar (Create):** Formulario web validado tanto en el cliente como en el servidor (`ModelForm`), con protección CSRF y estilos de Bootstrap 5.
- **Editar (Update):** Modificación de las especificaciones de cualquier supercomputadora con los datos existentes precargados.
- **Borrar (Delete):** Eliminación física del registro en SQLite requiriendo confirmación expresa mediante petición HTTP POST.
- **Panel Administrativo Oficial:** Mapeo del modelo en el administrador de Django (`/admin/`), con filtros laterales, buscador y auditoría de cambios.

---

## 4. Instrucciones de Instalación y Ejecución

### 1. Requisitos Previos
- Python 3.10 o superior instalado.
- Visual Studio Code o terminal de comandos.

### 2. Instalación del framework Django
Desde la raíz del proyecto, ejecuta:
```bash
py -m pip install django
```

### 3. Aplicar las migraciones a la base de datos SQLite
```bash
py manage.py migrate
```

### 4. Cargar los datos iniciales de las 3 supercomputadoras
Se incluye un comando personalizado de Django que puebla la tabla con los datos reales del TOP500:
```bash
py manage.py poblar_datos
```

### 5. Ejecutar la suite de pruebas automatizadas
Para comprobar que los modelos, conversiones y rutas del CRUD responden correctamente:
```bash
py manage.py test
```

### 6. Iniciar el servidor web de desarrollo
```bash
py manage.py runserver
```
Abre tu navegador en: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### 7. Acceso al Panel de Administración
- URL: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
- **Usuario:** `admin`
- **Contraseña:** `admin123`

---

## 5. Estructura del Directorio

```text
proyecto_supercomputadoras/
├── manage.py
├── db.sqlite3
├── requirements.txt
├── README.md
├── supercomputadoras_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── computadoras/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── management/
│   │   └── commands/
│   │       └── poblar_datos.py
│   └── templates/
│       └── computadoras/
│           ├── base.html
│           ├── lista.html
│           ├── detalle.html
│           ├── formulario.html
│           └── confirmar_eliminar.html
├── static/
│   └── css/
│       └── style.css
└── documentacion_latex/
    ├── reporte_proyecto.tex
    ├── Proyecto_Final_Computacion_Concurrente_Django.pdf
    └── imagenes/
        ├── 01_verificar_entorno.png
        ├── ...
        └── 16_web_admin_listado.png
```

---

## 6. Documentación Adicional

En la carpeta `documentacion_latex/` se incluye:
- `reporte_proyecto.tex`: Documento fuente en formato LaTeX generado directamente, estructurado con marco teórico de computación concurrente, bitácora de terminal y código fuente.
- `Proyecto_Final_Computacion_Concurrente_Django.pdf`: Documento final compilado con la bitácora de terminal y capturas de pantalla de la aplicación web.

---

## 7. Referencias y Enlaces de Interés

- [TOP500 The List: Ranking Oficial de Supercomputadoras](https://top500.org/)
- [Documentación Oficial de Django](https://docs.djangoproject.com/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [¿Qué es Django y por qué importa? - Django y DRF](https://www.youtube.com/watch?v=B8OlRdYwNlA)
- [Django Portafolio, Ejemplo Práctico](https://www.youtube.com/watch?v=zBjMF6je24U)
- [Django REST Framework y React CRUD](https://www.youtube.com/watch?v=38XWpyEK8IY)
- [Crea una agenda virtual con Django](https://www.youtube.com/watch?v=EQ-kqDmfUoM)
