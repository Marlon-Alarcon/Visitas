from rest_framework import routers
from .views import EstudianteViewsets, PersonaViewsets,VisitanteViewsets

router=routers.DefaultRouter()
router.register('estudiante',EstudianteViewsets)
router.register('persona',PersonaViewsets)
router.register('visitante',VisitanteViewsets)

#from django.urls import path, include
#urlpatterns = [
#    path('api/', include(router.urls)),
#]

urlpatterns = router.urls