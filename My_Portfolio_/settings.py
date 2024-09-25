# import os
# import sys
#
# from dotenv import load_dotenv
#
# # Cargar variables de entorno desde .env
# load_dotenv()
#
# # Definir la ruta base del proyecto
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#
# # Añadir la carpeta 'Apps' al path para que sea detectada como módulo de Python
# sys.path.append(os.path.join(BASE_DIR, 'Apps'))
#
# # Definir el entorno actual (desarrollo o producción)
# ENVIRONMENT = os.getenv('ENVIRONMENT', '')
#
# # Definir un valor para el entorno de desarrollo
# VALID_ENVIRONMENT = os.getenv('VALIDATORS', '')
#
# # Configuración de DEBUG: Activo solo en desarrollo
# DEBUG = ENVIRONMENT == VALID_ENVIRONMENT and os.getenv('DEBUG', 'False') == 'True'
#
# # Configuración de seguridad: Clave secreta
# # SECRET_KEY = os.getenv('SECRET_KEY', "django-insecure-x0737*32^!g&+qpncfgc9l2x45*+^lm%ks34omoc9r%#^n)2(-")
# SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-default-key')
#
# # Hosts permitidos
# ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')
#
# # Aplicaciones instaladas
# INSTALLED_APPS = [
#   'django.contrib.admin',
#   'django.contrib.auth',
#   'django.contrib.contenttypes',
#   'django.contrib.sessions',
#   'django.contrib.messages',
#   'django.contrib.staticfiles',
#
#   # @JavicSoftCode
#   # Mis Aplicaciones
#   'Apps.My_Blogs',
#   'Apps.My_Portfolio',
# ]
#
# # Middleware
# MIDDLEWARE = [
#   'django.middleware.security.SecurityMiddleware',
#   'django.contrib.sessions.middleware.SessionMiddleware',
#   'django.middleware.common.CommonMiddleware',
#   'django.middleware.csrf.CsrfViewMiddleware',
#   'django.contrib.auth.middleware.AuthenticationMiddleware',
#   'django.contrib.messages.middleware.MessageMiddleware',
#   'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]
#
# # URL principal
# ROOT_URLCONF = 'My_Portfolio_.urls'
#
# # @JavicSoftCode
# # Configuración de las plantillas
# TEMPLATES = [
#   {
#     'BACKEND': 'django.template.backends.django.DjangoTemplates',
#     'DIRS': [os.path.join(BASE_DIR, 'FrontEnd/templates')],  # Ruta de las plantillas
#     #     'DIRS': [
#     #       os.path.join(BASE_DIR, 'FrontEnd/templates'),  # Carpeta de plantillas del frontend
#     #       os.path.join(BASE_DIR, 'Apps/My_Blogs/templates'),  # Carpeta de plantillas de My_Blogs
#     #       os.path.join(BASE_DIR, 'Apps/My_Portfolio/templates'),  # Carpeta de plantillas de My_Portfolio
#     #     ],
#     'APP_DIRS': True,
#     'OPTIONS': {
#       'context_processors': [
#         'django.template.context_processors.debug',
#         'django.template.context_processors.request',
#         'django.contrib.auth.context_processors.auth',
#         'django.contrib.messages.context_processors.messages',
#       ],
#     },
#   },
# ]
#
# # Configuración WSGI
# WSGI_APPLICATION = 'My_Portfolio_.wsgi.application'
#
# # @JavicSoftCode
# # Configuración de la base de datos
# DATABASES = {
#   'default': {
#     'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.postgresql'),
#     'NAME': os.getenv('DB_NAME_DATABASE', ''),
#     'USER': os.getenv('DB_USERNAME_DATABASE', ''),
#     'PASSWORD': os.getenv('DB_PASSWORD_DATABASE', ''),
#     'HOST': os.getenv('DB_HOST_DATABASE', ''),
#     'PORT': os.getenv('DB_PORT_DATABASE', '5432'),
#   }
# }
#
# # Validación de contraseñas
# AUTH_PASSWORD_VALIDATORS = [
#   {
#     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#   },
#   {
#     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#   },
#   {
#     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#   },
#   {
#     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#   },
# ]
#
# # @JavicSoftCode
# # Configuración de localización
# LANGUAGE_CODE = 'es-ec'  # Cambiar a español
# TIME_ZONE = 'America/Guayaquil'  # Zona horaria de Ecuador
# USE_I18N = True  # Habilitar internacionalización
# USE_TZ = True  # Usar zonas horarias
#
# # @JavicSoftCode
# # Configuración de la URL base para archivos estáticos (CSS, JavaScript, imágenes) accesibles públicamente
# # En producción, estos archivos serán servidos desde un servidor web como Nginx o Apache.
# STATIC_URL = '/static/'
#
# # @JavicSoftCode
# # Configuración de directorios estáticos en el entorno de desarrollo.
# # Aquí indicamos a Django que también busque archivos estáticos (CSS, JS, etc.) en la carpeta especificada.
# # En este caso, 'FrontEnd/static' dentro de tu directorio base del proyecto.
# # Esto es útil para manejar archivos estáticos propios durante el desarrollo.
# STATICFILES_DIRS = [
#   os.path.join(BASE_DIR, 'FrontEnd/static'),
# ]
#
# # @JavicSoftCode
# # Configuración de la URL base para archivos de medios subidos por los usuarios (imágenes, videos, etc.).
# # MEDIA_URL especifica el prefijo de URL para acceder a archivos subidos desde el navegador.
# # Ejemplo: Si un usuario sube una imagen, esta será accesible desde '/public/nombre_imagen.jpg'.
# MEDIA_URL = '/public/'
#
# # @JavicSoftCode
# # Definición de la ruta en el sistema de archivos donde se guardarán los archivos de medios subidos por los usuarios.
# # MEDIA_ROOT define la carpeta local dentro del proyecto donde se almacenan los archivos de medios.
# # En este caso, será la carpeta 'media' dentro del directorio base del proyecto.
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
#
# # Tipo de campo de clave primaria por defecto
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

import os
import sys

# pip install python-dotenv
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Definir la ruta base del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Añadir la carpeta 'Apps' al path para que sea detectada como módulo de Python
sys.path.append(os.path.join(BASE_DIR, 'Apps'))

# Definir el entorno actual (desarrollo o producción)
ENVIRONMENT = os.getenv('ENVIRONMENT', '')
VALID_ENVIRONMENT = os.getenv('VALID_ENVIRONMENT', '')  # Asegúrate de que esta variable esté bien definida

# Configuración de DEBUG: Activo solo en desarrollo
DEBUG = ENVIRONMENT == VALID_ENVIRONMENT and os.getenv('DEBUG', 'False').lower() == 'true'

# Configuración de seguridad: Clave secreta
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-default-key')

# Hosts permitidos
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')

# Aplicaciones instaladas
INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  # Aplicaciones personalizadas
  'Apps.My_Blogs',
  'Apps.My_Portfolio',
]

# Middleware
MIDDLEWARE = [
  'django.middleware.security.SecurityMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL principal
ROOT_URLCONF = 'My_Portfolio_.urls'

# Configuración de las plantillas
TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, 'FrontEnd/templates')],
    'APP_DIRS': True,
    'OPTIONS': {
      'context_processors': [
        'django.template.context_processors.debug',
        'django.template.context_processors.request',
        'django.contrib.auth.context_processors.auth',
        'django.contrib.messages.context_processors.messages',
      ],
    },
  },
]

# Configuración WSGI
WSGI_APPLICATION = 'My_Portfolio_.wsgi.application'

# Configuración de la base de datos
DATABASES = {
  'default': {
    'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.postgresql'),
    'NAME': os.getenv('DB_NAME_DATABASE', ''),
    'USER': os.getenv('DB_USERNAME_DATABASE', ''),
    'PASSWORD': os.getenv('DB_PASSWORD_DATABASE', ''),
    'HOST': os.getenv('DB_HOST_DATABASE', ''),
    'PORT': os.getenv('DB_PORT_DATABASE', '5432'),
  }
}

# Validación de contraseñas
AUTH_PASSWORD_VALIDATORS = [
  {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
  {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
  {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
  {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Configuración de localización
LANGUAGE_CODE = 'es-EC'  # Cambiar a español de Ecuador
TIME_ZONE = 'America/Guayaquil'  # Zona horaria de Ecuador
USE_I18N = True  # Habilitar internacionalización
USE_TZ = True  # Usar zonas horarias

# Configuración de archivos estáticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'FrontEnd/static')]

# Configuración de archivos de medios
MEDIA_URL = '/public/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Tipo de campo de clave primaria por defecto
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
