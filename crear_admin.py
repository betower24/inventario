import os
import django
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventario_escolar.settings')
django.setup()

from django.contrib.auth.models import User

try:
    if not User.objects.filter(username='admin_beto').exists():
        User.objects.create_superuser('admin_beto', 'admin@example.com', 'Password2026')
        print("Superusuario creado correctamente.")
    else:
        print("El admin ya existe.")
except Exception as e:
    print(f"Aviso: No se pudo crear el admin aún (posiblemente falta migrate): {e}")