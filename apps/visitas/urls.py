from rest_framework import routers
from .views import VisitaViewsets,Consulta, Consulta2, Consulta3, Consulta4


router=routers.DefaultRouter()
router.register('Visita',VisitaViewsets)
router.register('consulta', Consulta, basename="consulta")
router.register('consulta2', Consulta2, basename="consulta2")
router.register('consulta3', Consulta3, basename="consulta3")
router.register('consulta4', Consulta4, basename="consulta4")

#from django.urls import path, include
#urlpatterns = [
#    path('api/', include(router.urls)),
#]

urlpatterns = router.urls