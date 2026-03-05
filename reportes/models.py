from django.db import models
from django.contrib.auth.models import User


class CicloEscolar(models.Model):
    nombre = models.CharField(max_length=20, unique=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Reporte(models.Model):
    docente = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    edificio = models.CharField(max_length=50)

    ciclo = models.ForeignKey(CicloEscolar, on_delete=models.SET_NULL, null=True)

    grupo = models.CharField(max_length=10)
    carrera = models.CharField(max_length=100)
    turno = models.CharField(max_length=15)
    no_maquina = models.CharField(max_length=20)
    falla_observacion = models.TextField()

    atencion_prestada = models.TextField(blank=True, null=True)
    encargado_lab = models.CharField(max_length=100, blank=True, null=True)
    estatus = models.BooleanField(default=False)

    def __str__(self):
        return f"Reporte {self.no_maquina} - {self.docente.username}"
