
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (EmpresaViewSet, EquipoViewSet, TecnicoViewSet,
                    PlanMantencionViewSet, OrdenTrabajoViewSet)

router = DefaultRouter()
router.register(r"companies", EmpresaViewSet, basename="company")
router.register(r"equipments", EquipoViewSet, basename="equipment")
router.register(r"technicians", TecnicoViewSet, basename="technician")
router.register(r"plans", PlanMantencionViewSet, basename="plan")
router.register(r"work-orders", OrdenTrabajoViewSet, basename="workorder")

urlpatterns = router.urls
