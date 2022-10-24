from rest_framework import viewsets

from .models import Visita
from .serializer import VisitaSerializers

# Visita.
class VisitaViewsets(viewsets.ModelViewSet):
    queryset=Visita.objects.all()
    serializer_class = VisitaSerializers