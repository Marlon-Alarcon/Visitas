from rest_framework import routers
from .views import MaestraViewsets

router=routers.DefaultRouter()
router.register('maestra',MaestraViewsets)

from django.urls import path, include
urlpatterns = [
    path('api-m/', include(router.urls)),
]