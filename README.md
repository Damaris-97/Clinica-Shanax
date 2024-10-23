Clínica Shanax
Proyecto: Control de Contagios de Dengue
Alumnas: Melisa Marchesi, Damaris Videla

Descripción
Clínica Shanax es una aplicación web diseñada para gestionar el control de contagios de dengue. Permite el registro de pacientes, seguimiento de casos, y generación de estadísticas a través de gráficos interactivos. La aplicación está desarrollada usando Flask, MySQL, HTML, CSS, y JavaScript.

Estructura del Proyecto
Carpeta Principal: Clinica_salud

Contiene todos los archivos y carpetas del proyecto.
Archivos y Configuración Inicial

README: Documenta los cambios y el progreso del proyecto.
server.py: Configuración del servidor Flask, conexión a la base de datos MySQL, definición de rutas y funcionalidades.
.env: Variables de entorno para las credenciales de la base de datos y configuración sensible.
.gitignore: Excluye archivos sensibles como .env del control de versiones.
Estructura de Carpetas

static/: Archivos estáticos.
CSS: index.css, login.css, style.css, inicio.css.
Imágenes: imagen.png.
JS: script.js.
templates/: Archivos HTML.
add_paciente.html, base.html, edit_paciente.html, graph.html, index.html, inicio.html, login.html, paciente.html.
Funcionalidades
Registro de Pacientes: Permite agregar, editar y eliminar información de pacientes.
Estadísticas: Visualización de datos de contagios mediante gráficos.
Autenticación: Sistema de inicio de sesión y gestión de usuarios.
Sistema de Base de Datos: Conexión a MySQL para almacenar información.
Instrucciones de Uso
Clona el repositorio:

bash
Copiar código
git clone https://github.com/usuario/clinica-shanax.git
Instala las dependencias:

bash
Copiar código
pip install -r requirements.txt
Configura las variables de entorno en el archivo .env.

Inicia la aplicación:

bash
Copiar código
python server.py
Accede a la aplicación en tu navegador en http://localhost:5000.

Tecnologías Utilizadas
Frontend: HTML, CSS, JavaScript (Flask Templates)
Backend: Flask (Python)
Base de Datos: MySQL
Control de Versiones: Git
Progreso y Tareas
Crear rutas para el manejo de pacientes.
Integrar gráficos estadísticos.
Implementar autenticación de usuarios.
Contribuciones
Si deseas contribuir al proyecto, por favor realiza un fork y envía un pull request con una breve descripción de los cambios propuestos.
