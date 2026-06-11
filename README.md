# Gestor de Usuarios - Veterinaria

Este es un sistema de gestión y autenticación de usuarios desarrollado con el framework Django. El proyecto cuenta con un modelo de usuario personalizado, control de sesiones seguro, manejo dinámico de notificaciones mediante Bootstrap y una interfaz administrativa limpia basada en la plantilla AdminLTE.

El desarrollo se ha estructurado siguiendo las mejores prácticas de la arquitectura MVT (Modelo-Vista-Plantilla) de Django, manteniendo una estricta separación de responsabilidades entre el enrutamiento (`urls.py`) y la lógica de negocio (`views.py`).

##  Características

- **Autenticación de Usuarios:** Sistema completo de inicio y cierre de sesión protegido con el hashing nativo de Django y limpieza de caché del navegador al cerrar sesión.
- **Modelo de Usuario Personalizado:** Extensión del modelo base utilizando `AbstractUser` para permitir una relación dinámica de roles (`Tipo`) por usuario.
- **Panel de Gestión:** Interfaz protegida mediante el decorador `@login_required` para la visualización y registro seguro de nuevos usuarios en el sistema.
- **Notificaciones Dinámicas:** Mensajes de éxito, advertencia o error integrados con los componentes de alerta de Bootstrap que se desvanecen automáticamente tras unos segundos mediante JavaScript.
- **Seguridad y Variables de Entorno:** Exclusión de credenciales críticas (como la `SECRET_KEY` de Django y la contraseña de MySQL) del código fuente mediante el uso de la librería `python-dotenv`.

## Tecnologías Utilizadas

- **Backend:** Python, Django 6.x
- **Base de Datos:** MySQL
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap (Plantilla AdminLTE)
- **Control de Versiones:** Git & GitHub

## Instalación y Configuración Local

Para ejecutar este proyecto en tu entorno local, asegúrate de tener instalado Python y MySQL Server, y luego sigue estos pasos:

1. **Clonar el repositorio:**
   ```bash
    git clone https://github.com/keving259/django-proyecto-veterinaria.git
    cd django-proyecto-veterinaria
   ```

2. **Crear y activar el entorno virtual:**
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Mac/Linux:
source venv/bin/activate

3. **Instalar dependencias:**
    ```bash
    pip install django mysqlclient python-dotenv
    ```

4. **Configurar las variables de entorno:**
Crea un archivo llamado .env en la raíz del proyecto (al mismo nivel que manage.py) utilizando como referencia el archivo .env.example:
SECRET_KEY=tu_secret_key_de_django_aqui
DB_PASSWORD=tu_contraseña_real_de_mysql

5 **Ejecutar las migraciones para preparar la base de datos:**
python manage.py migrate

6. **Iniciar el servidor**
python manage.py runserver

## Créditos y Agradecimientos
Este proyecto fue desarrollado con fines educativos y de aprendizaje práctico, siguiendo la guía y el contenido del curso de Django disponible en el canal de YouTube de @elvisjosepavonzeas819. Un agradecimiento especial al creador por compartir el material base que sirvió como pilar fundamental para esta aplicación.