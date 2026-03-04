import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SEGURIDAD: En Render usamos una variable de entorno, si no existe, usa la de desarrollo.
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-pco@$3d5**k8^e(+q8*8dp#8xg+y(+^vq(b$tn&pj813vtk*#c')

# DEBUG: Se apaga automáticamente en Render
DEBUG = 'RENDER' not in os.environ

# Permitir el dominio de Render
ALLOWED_HOSTS = []
render_external_hostname = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if render_external_hostname:
    ALLOWED_HOSTS.append(render_external_hostname)


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'reportes', # No olvides registrar tu app aquí
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # INDISPENSABLE para Render
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'inventario_escolar.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'inventario_escolar.wsgi.application'


# DATABASE: Configurada para MongoDB Atlas
# En Render, deberás crear una variable de entorno llamada MONGO_URI
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'inventario_escolar',
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            # Reemplaza 'TuNuevaContraseña' con la que acabas de poner en Atlas
            'host': 'mongodb+srv://juan:Escuela2026@cluster0.akryjlv.mongodb.net/?appName=Cluster0',
        }
    }
}
# Busca esta línea y cámbiala:
 # O mejor: ['tu-app.onrender.com', 'localhost', '127.0.0.1']

# Asegúrate de que tu base de datos apunte a MongoDB Atlas (no a localhost)




# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Internationalization
LANGUAGE_CODE = 'es-mx' # Cambiado a español
TIME_ZONE = 'America/Mexico_City' # Ajustado a tu zona
USE_I18N = True
USE_TZ = True


# STATIC FILES: Configuración para WhiteNoise y Render
STATIC_URL = 'static/'

if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'crear_reporte'  # A donde va el profe al entrar
LOGOUT_REDIRECT_URL = 'login'
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'login'