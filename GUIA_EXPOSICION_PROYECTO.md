# Guía Completa de Exposición: Proyecto Final de Base de Datos Web con Django

**Licenciatura en Ciencia de Datos**  
**Asignatura:** Computación Concurrente  
**Docente:** Esp. Adrián Durán Chavesti  
**Ponderación:** 10 puntos (Exposición y Pruebas)

---

## Estructura de la Presentación para el Equipo (7 Expositores)

Esta guía explica detalladamente cada uno de los 7 temas para que cada integrante comprenda a fondo su parte, entienda el código y pueda exponerlo ante el profesor con total seguridad y claridad.

---

### Integrante 1: Propósito del Proyecto, Rúbrica y Datos a Ingresar

#### 1. ¿Qué debe explicar?
* **El contexto académico:** Este proyecto corresponde a la evaluación práctica de la materia *Computación Concurrente*.
* **El objetivo oficial:** Construir una base de datos relacional usando **SQLite** y gestionarla desde la web a través del framework **Django** en Python.
* **El conjunto de datos elegido:** La rúbrica solicita registrar la información técnica de las **3 computadoras más rápidas del mundo** (*El Capitan*, *Frontier* y *Aurora*). Es fundamental aclarar que el proyecto no consiste en dar una clase de historia de supercomputadoras; estos tres sistemas nos sirven como un conjunto de datos realistas con valores numéricos muy grandes (millones de núcleos, miles de Terabytes y TeraFLOPS) para demostrar cómo una base de datos almacena, consulta y actualiza información técnica compleja.
* **Los requerimientos de la consigna:**
  1. Guardar obligatoriamente 7 campos técnicos por computadora.
  2. Implementar las 4 operaciones del CRUD: Agregar, Editar, Borrar y Visualizar.
  3. Verificar el buen funcionamiento del sistema en vivo.

#### 2. Guion sugerido para hablar:
> *"Buenos días profesor y compañeros. Nuestro proyecto consiste en la creación y administración de una base de datos relacional SQLite con acceso web utilizando Django en Python. Para poner a prueba el sistema, la consigna nos pidió registrar las 3 supercomputadoras más potentes del planeta según el ranking oficial TOP500: El Capitan, Frontier y Aurora. Estos sistemas nos sirven como datos de entrada de gran escala para demostrar que la base de datos almacena correctamente los 7 campos obligatorios y permite las 4 funciones básicas: visualizar, agregar, editar y borrar registros."*

---

### Integrante 2: Framework Django, Patrón MVT y Seguridad (ORM)

#### 1. ¿Qué debe explicar?
* **¿Por qué usamos Django?** Django es uno de los frameworks web más robustos y populares de Python. Sigue la filosofía de *"baterías incluidas"*, lo que significa que ya trae integradas herramientas de seguridad, motor de plantillas, panel de administración y conexión a bases de datos sin tener que instalar componentes externos.
* **El Patrón MVT (Modelo - Vista - Template):**
  * **M (Modelo - `models.py`):** Define la estructura de las tablas de la base de datos en código Python.
  * **V (Vista - `views.py`):** Contiene la lógica del sistema. Recibe las peticiones del navegador, consulta o guarda datos en el modelo y decide qué respuesta enviar. En nuestro proyecto usamos *Class-Based Views* (`ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView`) para que el código sea limpio y reutilizable.
  * **T (Template - `templates/`):** Son las plantillas HTML que renderizan los datos para que el usuario los vea en su pantalla.
* **¿Qué es el ORM y cómo nos protege de Inyecciones SQL?**
  * El **ORM** (*Object-Relational Mapping*) permite interactuar con la base de datos usando objetos y métodos de Python en lugar de escribir comandos SQL a mano.
  * *Prevención de Inyección SQL:* En aplicaciones tradicionales donde se escribe `SELECT * FROM tabla WHERE nombre = '...'`, un usuario malicioso podría escribir código SQL en un campo de texto para borrar o robar la base de datos. Django soluciona esto automáticamente: su ORM parametriza y limpia todas las entradas del usuario antes de que toquen el motor de base de datos, haciendo imposible la inyección de SQL.

#### 2. Guion sugerido para hablar:
> *"Para construir esta solución elegimos Django debido a su arquitectura MVT: Modelo, Vista y Template. El Modelo define la estructura de las tablas, la Vista procesa la lógica de negocio y el Template genera el HTML que ve el usuario. Un aspecto fundamental de Django es su ORM, que traduce objetos de Python a consultas de base de datos. Esto nos brinda una gran capa de seguridad, ya que parametriza automáticamente todas las consultas, evitando por completo los ataques de Inyección SQL que ocurren cuando se concatena texto directamente en las sentencias de base de datos."*

---

### Integrante 3: Base de Datos SQLite Integrada y Código del Modelo (`models.py`)

#### 1. ¿Qué debe explicar?
* **¿Cómo opera SQLite en Django?** SQLite es una base de datos relacional completa que no necesita instalar un servidor pesado (como MySQL o PostgreSQL). Se guarda directamente en un archivo dentro del proyecto llamado `db.sqlite3`, lo cual permite portabilidad absoluta y cero configuración.
* **Los 7 campos obligatorios estipulados por el profesor:**
  1. `nombre`: Identificador de la supercomputadora.
  2. `pais_origen`: País sede del laboratorio.
  3. `numero_cores`: Conteo total de núcleos de procesamiento.
  4. `ram_tb`: Memoria RAM en Terabytes.
  5. `almacenamiento_tb`: Capacidad en disco en Terabytes.
  6. `teraflops`: Rendimiento de cálculo en punto flotante.
  7. `sistema_operativo`: Plataforma de software base.
* **Explicación del código real de `models.py`:**
  * Debe proyectar o señalar el código de la clase `Supercomputadora`:

```python
from django.db import models
from django.core.validators import MinValueValidator

class Supercomputadora(models.Model):
    # Los 7 campos obligatorios
    nombre = models.CharField(max_length=120, unique=True, verbose_name="Nombre")
    pais_origen = models.CharField(max_length=100, verbose_name="País de origen")
    numero_cores = models.PositiveBigIntegerField(
        verbose_name="Número de cores",
        validators=[MinValueValidator(1)]
    )
    ram_tb = models.DecimalField(
        max_digits=12, decimal_places=2,
        verbose_name="RAM (TB)",
        validators=[MinValueValidator(0.01)]
    )
    almacenamiento_tb = models.DecimalField(
        max_digits=14, decimal_places=2,
        verbose_name="Almacenamiento (TB)",
        validators=[MinValueValidator(0.01)]
    )
    teraflops = models.DecimalField(
        max_digits=16, decimal_places=2,
        verbose_name="Rendimiento (TeraFLOPS)",
        validators=[MinValueValidator(0.01)]
    )
    sistema_operativo = models.CharField(max_length=150, verbose_name="Sistema operativo")

    # Campos complementarios y auditoria
    fabricante = models.CharField(max_length=150, blank=True)
    institucion = models.CharField(max_length=180, blank=True)
    ranking_posicion = models.PositiveIntegerField(null=True, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
```

#### 2. Guion sugerido para hablar:
> *"La base de datos que utilizamos es SQLite, la cual viene integrada en Django en el archivo local db.sqlite3. En este archivo models.py que ven en pantalla declaramos exactamente los 7 campos obligatorios solicitados en la rúbrica. Usamos CharField para textos como el nombre, país y sistema operativo; PositiveBigIntegerField para los cores; y DecimalField con dos decimales para la memoria RAM, almacenamiento y TeraFLOPS. Además, incluimos validadores para garantizar que ningún usuario pueda guardar números negativos o vacíos."*

---

### Integrante 4: Maquetación Frontend, HTML5 y Modularidad (`base.html`)

#### 1. ¿Qué debe explicar?
* **Diseño web limpio y responsivo:** La aplicación está diseñada con HTML5 estándar y el framework **Bootstrap 5**. Esto permite que la página se vea ordenada, con tablas legibles y que se adapte automáticamente si se abre desde una computadora, tablet o celular.
* **El concepto clave de Modularidad y Herencia con `base.html`:**
  * En una página web tradicional sin frameworks, si tienes 5 páginas diferentes, tendrías que copiar y pegar el menú de navegación, los enlaces de estilos y el pie de página 5 veces. Si cambias algo en el menú, tendrías que modificar los 5 archivos.
  * Django resuelve esto mediante la **herencia de plantillas**:
    * Se creó un archivo maestro llamado `base.html` que contiene el `<!DOCTYPE html>`, la barra de navegación superior y el pie de página institucional.
    * En el centro de `base.html` se define un bloque vacío: `{% block content %}{% endblock %}`.
    * Cada pantalla secundaria (`lista.html`, `formulario.html`, `detalle.html`, etc.) solo inicia con `{% extends "computadoras/base.html" %}` y rellena únicamente lo que le corresponde.
  * Esto reduce el código a la mitad, evita errores y mantiene una apariencia consistente en toda la aplicación.

#### 2. Guion sugerido para hablar:
> *"En la parte visual utilizamos HTML5 y Bootstrap 5 para lograr una presentación clara, institucional y adaptable a cualquier pantalla. Lo más importante de nuestra arquitectura web es la herencia de plantillas de Django. En lugar de repetir la barra de navegación y el pie de página en cada archivo HTML, creamos una plantilla maestra llamada base.html. Todas las demás pantallas simplemente heredan de ella y rellenan su contenido específico mediante la etiqueta block content. Esto hace que el código sea limpio, modular y fácil de mantener."*

---

### Integrante 5: Demostración en Vivo del CRUD (Parte 1: Visualizar y Agregar)

#### 1. ¿Qué debe explicar y mostrar en pantalla?
* **Función Visualizar (Listado y Métricas):**
  * Abrir la página principal (`/`).
  * Mostrar el panel superior con los totales acumulados de núcleos, TeraFLOPS y almacenamiento que Django calcula directamente con la función `aggregate()` sobre SQLite.
  * Mostrar la tabla donde aparecen las computadoras registradas con sus 7 campos en columnas claras.
  * Pulsar el botón **"Ver"** en cualquiera de ellas (`/<id>/`) para mostrar la **Ficha Técnica Detallada**, donde el sistema convierte los valores automáticamente a Petabytes y ExaFLOPS.
* **Función Agregar (Crear Registro):**
  * Hacer clic en el botón superior **"+ Agregar Supercomputadora"** (`/nueva/`).
  * Mostrar el formulario generado con `SupercomputadoraForm`.
  * Explicar que el formulario valida los datos: si intentas enviar el formulario vacío, el navegador y Django impiden el envío y señalan los campos obligatorios.
  * Rellenar un ejemplo de prueba y presionar *"Guardar Registro"*. Mostrar cómo redirige al catálogo y muestra un mensaje de éxito notificando que se guardó en `db.sqlite3`.

#### 2. Guion sugerido para hablar:
> *"Ahora pasamos a la demostración práctica de las primeras dos funciones del CRUD: Visualizar y Agregar. En la pantalla principal pueden observar el catálogo general. En la parte superior tenemos un resumen con las sumatorias totales calculadas directamente desde SQLite, y abajo la tabla con cada equipo. Si damos clic en 'Ver', accedemos a la ficha técnica con todas las especificaciones y conversiones a PetaFLOPS y Petabytes. Ahora, si vamos a 'Agregar Supercomputadora', se nos despliega el formulario web. Este formulario cuenta con validación de campos requeridos; al llenarlo y presionar 'Guardar', la información se inserta de inmediato en SQLite y volvemos a la lista con el registro añadido."*

---

### Integrante 6: Demostración en Vivo del CRUD (Parte 2: Editar y Borrar)

#### 1. ¿Qué debe explicar y mostrar en pantalla?
* **Función Editar:**
  * Elegir uno de los registros y presionar el botón **"Editar"** (`/<id>/editar/`).
  * Mostrar que los datos existentes se cargan automáticamente en las casillas correspondientes.
  * Modificar un valor (por ejemplo, aumentar el almacenamiento o cambiar la versión del sistema operativo) y hacer clic en *"Guardar Cambios"*.
  * Comprobar que en la tabla principal el dato se actualizó en tiempo real.
* **Función Borrar y Mecanismo de Seguridad:**
  * Elegir un registro de prueba y pulsar el botón **"Borrar"** (`/<id>/eliminar/`).
  * **Punto clave a explicar:** Explicar al profesor que por buenas prácticas de ingeniería de software, un sistema web profesional **nunca debe borrar información con una petición GET directa o con un solo clic**, porque un usuario podría equivocarse o un bot podría activar enlaces de borrado accidentalmente.
  * Django nos lleva a una pantalla de confirmación expresa. Al pulsar *"Sí, Eliminar"*, el formulario envía una petición HTTP **POST** que viaja protegida con un token criptográfico `{% csrf_token %}` (*Cross-Site Request Forgery*), garantizando que la orden fue autorizada conscientemente por el usuario actual.
* *(Opcional)*: Mostrar en la barra de navegación el acceso al **Panel de Administración** (`/admin/`), indicando que Django provee un panel integrado con filtros y buscador para auditar la base de datos.

#### 2. Guion sugerido para hablar:
> *"Continuando con el CRUD, la función de Editar nos permite modificar cualquier especificación. Al hacer clic en 'Editar', el formulario precarga los datos actuales del registro; modificamos cualquier valor, guardamos y el cambio se aplica al instante en la base de datos. Por su parte, la función Borrar implementa una medida de seguridad esencial: no borra directamente con un clic, sino que solicita confirmación previa mediante una petición HTTP POST protegida con un token CSRF. Esto previene borrados accidentales y protege la aplicación contra ataques de falsificación de peticiones. Finalmente, el proyecto también cuenta con el panel de administración oficial de Django en la ruta /admin/ para gestionar la base de datos con filtros y buscador."*

---

### Integrante 7: Despliegue en la Nube con Render y Conclusiones

#### 1. ¿Qué debe explicar?
* **¿Cómo está publicado en internet?** La aplicación está desplegada en la plataforma en la nube **Render**, vinculada de forma continua con nuestro repositorio de **GitHub**.
* **Los 2 archivos clave de despliegue:**
  1. `build.sh`: Es el script que Render ejecuta cada vez que subimos cambios. Se encarga de:
     * Instalar las librerías necesarias (`pip install -r requirements.txt`).
     * Recopilar los archivos estáticos de CSS (`collectstatic`).
     * Aplicar las migraciones a la base de datos SQLite (`migrate`).
  2. `Procfile`: Es el archivo que le indica al servidor en la nube cómo iniciar la aplicación en producción utilizando el servidor WSGI de alto rendimiento **Gunicorn**:
     ```text
     web: gunicorn supercomputadoras_project.wsgi --log-file -
     ```
* **Conclusiones del Proyecto:**
  * Se cumplió estrictamente con cada uno de los puntos exigidos en la rúbrica oficial (10 puntos).
  * El sistema es completamente funcional tanto en local como en la nube pública.
  * Demostramos cómo se conecta la teoría de bases de datos relacionales, la seguridad web y la programación en Python mediante Django.

#### 2. Guion sugerido para hablar:
> *"Para finalizar, nuestra aplicación no solo funciona de manera local, sino que se encuentra desplegada en la nube en la plataforma Render. Esto se logra conectando nuestro repositorio de GitHub con Render. Mediante el archivo build.sh se automatiza la instalación de dependencias y las migraciones de SQLite, mientras que el archivo Procfile inicia el servidor web de producción utilizando Gunicorn. En conclusión, el proyecto cumple al cien por ciento con los requerimientos planteados por el docente Adrián Durán Chavesti: base de datos SQLite en Python, los 7 campos técnicos obligatorios, las 4 operaciones CRUD plenamente funcionales y una arquitectura web segura y modular. Muchas gracias por su atención, quedamos atentos a sus preguntas o pruebas que desee realizar."*

---

## Resumen de los Datos Técnicos Registrados (TOP500)

| Campo Obligatorio | #1 El Capitan (EE.UU.) | #2 Frontier (EE.UU.) | #3 Aurora (EE.UU.) |
| :--- | :--- | :--- | :--- |
| **1. Nombre** | El Capitan | Frontier | Aurora |
| **2. País de origen** | Estados Unidos | Estados Unidos | Estados Unidos |
| **3. Número de cores** | 11,340,000 cores | 9,066,176 cores | 9,264,128 cores |
| **4. Cantidad de RAM** | 5,437 TB (~5.44 PB) | 9,200 TB (~9.20 PB) | 10,900 TB (~10.90 PB) |
| **5. Almacenamiento** | 40,000 TB (40 PB) | 70,000 TB (70 PB) | 220,000 TB (220 PB) |
| **6. TeraFLOPS** | 1,809,000.00 TFLOPS | 1,353,000.00 TFLOPS | 1,012,000.00 TFLOPS |
| **7. Sistema operativo** | TOSS (RHEL-based) | HPE Cray OS | SUSE Linux Enterprise |
