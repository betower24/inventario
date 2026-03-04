from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Reporte, CicloEscolar
from bson import ObjectId

@login_required
def redireccionar_usuario(request):
    """Punto de entrada: Si es admin va al Menú Principal, si no al Formulario"""
    if request.user.is_staff:
        return redirect('menu_admin') # Ahora redirige al nuevo menú
    return redirect('crear_reporte')

# --- VISTAS DEL ADMINISTRADOR (BETO) ---

@staff_member_required
def menu_admin(request):
    """Interfaz principal para el administrador con botones de acceso rápido"""
    return render(request, 'reportes/menu_admin.html')

@staff_member_required
def dashboard_admin(request):
    """Beto ve la tabla de todos los reportes"""
    try:
        todos = list(Reporte.objects.all().order_by('-fecha'))
        pendientes = len([r for r in todos if not r.estatus])
    except:
        todos = []
        pendientes = 0
    return render(request, 'reportes/admin_dashboard.html', {
        'reportes': todos, 
        'pendientes': pendientes
    })

@staff_member_required
def gestionar_ciclos(request):
    """Interfaz para crear nuevos periodos escolares"""
    if request.method == 'POST':
        CicloEscolar.objects.create(nombre=request.POST.get('nombre_ciclo'))
        return redirect('gestionar_ciclos')
    
    # Obtenemos todos los ciclos y los ordenamos con Python para evitar fallos de Djongo
    ciclos = list(CicloEscolar.objects.all().order_by('-nombre'))
    return render(request, 'reportes/gestionar_ciclos.html', {'ciclos': ciclos})

@staff_member_required
def resolver_reporte(request, reporte_id):
    """Interfaz para que el admin dé solución a una falla"""
    reporte = get_object_or_404(Reporte, _id=ObjectId(reporte_id))
    if request.method == 'POST':
        reporte.atencion_prestada = request.POST.get('solucion')
        reporte.encargado_lab = request.user.username
        reporte.estatus = True
        reporte.save()
        return redirect('dashboard_admin')
    return render(request, 'reportes/resolver.html', {'reporte': reporte})


# --- VISTAS DEL PROFESOR ---

@login_required
def crear_reporte(request):
    """Formulario para que el docente reporte una falla"""
    if request.method == 'POST':
        ciclo_id = request.POST.get('ciclo')
        ciclo_obj = CicloEscolar.objects.get(_id=ObjectId(ciclo_id))
        
        Reporte.objects.create(
            docente=request.user,
            edificio=request.POST.get('edificio'),
            ciclo=ciclo_obj,
            grupo=request.POST.get('grupo'),
            carrera=request.POST.get('carrera'),
            turno=request.POST.get('turno'),
            no_maquina=request.POST.get('no_maquina'),
            falla_observacion=request.POST.get('falla_observacion')
        )
        return redirect('lista_reportes')
    
    # CORRECCIÓN DE ERROR DJONGO: Evitamos filter(activo=True) directo
    try:
        todos_los_ciclos = CicloEscolar.objects.all()
        ciclos_activos = [c for c in todos_los_ciclos if c.activo]
    except:
        ciclos_activos = []
        
    return render(request, 'reportes/formulario.html', {'ciclos': ciclos_activos})

@login_required
def lista_reportes(request):
    """El profesor ve su historial personal"""
    reportes = list(Reporte.objects.filter(docente=request.user).order_by('-fecha'))
    return render(request, 'reportes/lista.html', {'reportes': reportes})