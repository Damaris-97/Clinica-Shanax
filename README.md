#Clínica Shanax
Proyecto: Sistema de control de contagios de dengue
Alumnas: Melisa Marchesi, Damaris Videla

#Descripción
Clínica Shanax es una aplicación web diseñada para registrar y gestionar los casos de contagio de dengue, ofreciendo una interfaz intuitiva para la administración de pacientes y el monitoreo de estadísticas a través de gráficos interactivos.

#Estructura del Proyecto
Backend: Flask (Python) para la gestión del servidor y conexión a MySQL.
Frontend: HTML, CSS, JavaScript.
Base de Datos: MySQL para el almacenamiento de información sobre pacientes y estadísticas.
Archivos Principales:
server.py: Configuración de Flask y rutas de la aplicación.
.env: Variables de entorno para la configuración de MySQL.
static/: Archivos estáticos (CSS, JavaScript, imágenes).
templates/: Vistas HTML para la interfaz del usuario.
Funcionalidades Clave
Gestión de Pacientes: Registro, edición y eliminación de pacientes.
Estadísticas: Visualización de datos de contagios mediante gráficos.
Autenticación de Usuarios: Sistema de login seguro para acceso al sistema.
Instalación y Ejecución
Clona el repositorio:
git clone https://github.com/usuario/clinica-shanax.git

Instala las dependencias:
pip install -r requirements.txt

Configura las variables de entorno en .env.

Ejecuta la aplicación:
python server.py

#Tecnologías
Flask (Python)
MySQL
HTML, CSS, JavaScript
