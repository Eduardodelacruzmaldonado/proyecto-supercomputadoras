# Proyecto Final: Creación de una Base de Datos con Acceso Web usando Django en Python
**Licenciatura en Ciencia de Datos**  
**Materia:** Computación Concurrente  
**Docente:** Esp. Adrián Durán Chavesti  
**Valor:** 10 puntos  

---

## 🚀 Descripción del Proyecto
Este proyecto implementa una aplicación web con el framework **Django** y base de datos relacional **SQLite**, destinada a la gestión y visualización de las especificaciones técnicas de las **3 computadoras más rápidas del mundo** (sistemas de computación concurrente a exaescala según el ranking TOP500):
1. **El Capitan** (Estados Unidos - 1.809 ExaFLOPS / 11.34 millones de cores)
2. **Frontier** (Estados Unidos - 1.353 ExaFLOPS / 9.06 millones de cores)
3. **Aurora** (Estados Unidos - 1.012 ExaFLOPS / 9.26 millones de cores)

---

## 📋 Requerimientos y Cumplimiento de la Consigna

### 1. Parámetros de la Base de Datos SQLite (7 campos obligatorios):
- **Nombre:** Identificador del supercomputador (p. ej. *El Capitan*).
- **País de origen:** País sede del centro de supercómputo.
- **Número de cores:** Concurrencia masiva de núcleos de procesamiento (CPU + GPUs/Aceleradores).
- **Cantidad de RAM (TB):** Memoria principal en Terabytes (con cálculo automático en Petabytes).
- **Almacenamiento (TB):** Capacidad en Terabytes.
- **TeraFLOPS:** Rendimiento de cálculo en coma flotante (con conversión a PFLOPS y EFLOPS).
- **Sistema operativo:** Plataforma de software base (ej. *TOSS / RHEL*, *HPE Cray OS*, *SUSE Linux*).

### 2. Funcionalidades CRUD Implementadas:
- [x] **a. Agregar:** Formulario web con validaciones y estilos Bootstrap 5 para dar de alta nuevos registros.
- [x] **b. Editar:** Actualización en tiempo real de cualquier especificación técnica.
- [x] **c. Borrar:** Eliminación física en SQLite con diálogo de confirmación previa para prevenir pérdidas accidentales.
- [x] **d. Visualizar:** Dashboard interactivo con tarjetas de podio, métricas agregadas globales y ficha técnica detallada por supercomputadora.
- [x] **e. Panel de Administración Django:** Acceso a `/admin/` para auditoría, búsqueda y filtros avanzados.

---

## 🛠️ Instrucciones de Instalación y Ejecución

### 1. Clonar o abrir el directorio en VS Code
Abre la carpeta `proyecto_supercomputadoras` en Visual Studio Code.

### 2. Instalar dependencias
```bash
py -m pip install django
```

### 3. Aplicar migraciones a SQLite
```bash
py manage.py migrate
```

### 4. Cargar las 3 supercomputadoras más rápidas del mundo
Ejecuta el comando personalizado incluido en el proyecto:
```bash
py manage.py poblar_datos
```

### 5. Iniciar el servidor web
```bash
py manage.py runserver
```
Abre en tu navegador: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### 6. Acceso al Panel de Administración
- URL: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
- **Usuario:** `admin`
- **Contraseña:** `admin123`

### 7. Ejecutar las pruebas unitarias automatizadas
Para comprobar que el 100% de las funciones operan correctamente:
```bash
py manage.py test
```

---

## 📄 Documentación en LaTeX y PDF Generado
En la carpeta `documentacion_latex/` encontrarás:
- `reporte_proyecto.tex`: Código fuente en formato LaTeX listo para compilar o abrir en Overleaf.
- `Proyecto_Final_Computacion_Concurrente_Django.pdf`: Documento de 14 páginas compilado con todas las capturas de pantalla de terminales y vistas web.
- `imagenes/`: Carpeta con las 16 capturas de pantalla de alta resolución (comandos, migraciones, pruebas y vistas web).
- `generar_capturas.py`: Script para regenerar todas las capturas de pantalla de forma automatizada.
- `generar_pdf_reporte.py`: Script generador del PDF con tipografía Unicode.

---

## 🔗 Enlaces de Interés
- [Visual Studio Code](https://code.visualstudio.com/)
- [¿Qué es Django y por qué importa? - Django y DRF](https://www.youtube.com/watch?v=B8OlRdYwNlA)
- [Django Portafolio, Ejemplo Práctico](https://www.youtube.com/watch?v=zBjMF6je24U)
- [Django REST Framework y React CRUD](https://www.youtube.com/watch?v=38XWpyEK8IY)
- [Crea una agenda virtual con Django](https://www.youtube.com/watch?v=EQ-kqDmfUoM)
- [TOP500 List](https://top500.org/)
