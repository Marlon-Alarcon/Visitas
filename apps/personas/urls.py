from rest_framework import routers
from .views import EstudianteViewsets, PersonaViewsets,VisitanteViewsets, ActualizandoViewsets

router=routers.DefaultRouter()
router.register('estudiante',EstudianteViewsets)
router.register('persona',PersonaViewsets)
router.register('visitante',VisitanteViewsets)
router.register('actupersona', ActualizandoViewsets)

#from django.urls import path, include
#urlpatterns = [
#    path('api/', include(router.urls)),
#]

urlpatterns = router.urls