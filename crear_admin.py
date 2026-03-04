import os
import django
import sys

# Parche para la librería 'six' que pide Djongo
try:
    import six
    sys.modules['django.utils.six'] = six
except ImportError:
    pass

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventario_escolar.settings')
django.setup()

from django.contrib.auth.models import User
from django.utils import timezone

username = 'admin_beto'
email = 'admin@example.com'
password = 'Password2026'

try:
    if not User.objects.filter(username=username).exists():
        user = User(
            username=username,
            email=email,
            is_staff=True,
            is_superuser=True,
            is_active=True,
            date_joined=timezone.now()
        )
        user.set_password(password)
        user.save()
        print(f"¡Éxito! Superusuario '{username}' creado.")
    else:
        print(f"El usuario '{username}' ya existe.")
except Exception as e:
    print(f"Error: {e}")