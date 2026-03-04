from django.contrib import admin
from django.urls import path
from reportes import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # --- RUTAS DE REDIRECCIÓN Y LOGIN ---
    path('', views.redireccionar_usuario, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='reportes/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # --- RUTAS DEL PROFESOR ---
    path('nuevo-reporte/', views.crear_reporte, name='crear_reporte'),
    path('lista-reportes/', views.lista_reportes, name='lista_reportes'),

    # --- RUTAS DEL ADMINISTRADOR (BETO) ---
    path('admin-dashboard/', views.dashboard_admin, name='dashboard_admin'),
    path('gestionar-ciclos/', views.gestionar_ciclos, name='gestionar_ciclos'),
    path('resolver/<str:reporte_id>/', views.resolver_reporte, name='resolver_reporte'),
    path('panel-admin/', views.menu_admin, name='menu_admin'),
]