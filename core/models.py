from django.db import models
from django.contrib.auth.models import User

class Empresa(models.Model):
    nombre = models.CharField(max_length=150)
    direccion = models.CharField(max_length=250)
    rut = models.CharField(max_length=12, unique=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    

class Equipo(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='equipos')
    nombre = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100, unique=True)
    criticalidad = models.BooleanField(default=False)
    instalado_en = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.numero_serie})"
    

class Tecnico(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='tecnico_profile')
    nombre_completo = models.CharField(max_length=150)
    especialidad = models.CharField(max_length=150)
    telefono = models.CharField(max_length=20)

    def __str__(self): 
        return self.nombre_completo


class PlanMantencion(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete = models.CASCADE, related_name='planes_mantencion')
    nombre = models.CharField(max_length=150)
    dias_frecuencia = models.PositiveIntegerField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} - {self.equipo}"
    
class OrdenTrabajo(models.Model):
    STATUS_CHOICES = [
        ("programada", "Programada"),
        ("en_progreso", "En_Progreso"),
        ("completada", "Completada"),
        ("cancelada", "Cancelada"),
    ]

    plan = models.ForeignKey(PlanMantencion, on_delete=models.CASCADE, related_name='ordenes_trabajo')
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='ordenes_trabajo')
    tecnico = models.ForeignKey(Tecnico, on_delete=models.SET_NULL, null=True, related_name='ordenes_trabajo')
    estatus = models.CharField(max_length=20, choices=STATUS_CHOICES, default="programada")
    fecha_programada = models.DateField()
    completado_en =models.DateTimeField(null=True, blank=True)
    notas = models.TextField(blank=True)

    def __str__(self):
        return f"OT {self.id} - {self.estatus}"
    
