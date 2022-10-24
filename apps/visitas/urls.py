from rest_framework import routers
from .views import VisitaViewsets

router=routers.DefaultRouter()
router.register('Visita',VisitaViewsets)

#from django.urls import path, include
#urlpatterns = [
#    path('api/', include(router.urls)),
#]

urlpatterns = router.urls