from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Empresa, Equipo, Tecnico, PlanMantencion, OrdenTrabajo
from .serializers import (
    EmpresaSerializer,
    EquipoSerializer,
    TecnicoSerializer,
    PlanMantencionSerializer,
    OrdenTrabajoSerializer,
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    instruction_classes = [IsAuthenticatedOrReadOnly]

class EquipoViewSet(viewsets.ModelViewSet):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer
    instruction_classes = [IsAuthenticatedOrReadOnly]

class TecnicoViewSet(viewsets.ModelViewSet):
    queryset = Tecnico.objects.all()
    serializer_class = TecnicoSerializer
    instruction_classes = [IsAuthenticatedOrReadOnly]

class PlanMantencionViewSet(viewsets.ModelViewSet):
    queryset = PlanMantencion.objects.all()
    serializer_class = PlanMantencionSerializer
    instruction_classes = [IsAuthenticatedOrReadOnly]

class OrdenTrabajoViewSet(viewsets.ModelViewSet):
    queryset = OrdenTrabajo.objects.all()
    serializer_class = OrdenTrabajoSerializer
    instruction_classes = [IsAuthenticatedOrReadOnly]
