from rest_framework import viewsets

from .models import Estudiante, Persona, Visitante
from .serializer import EstudianteSerializers, PersonaSerializers, VisitanteSerializers


# Estudiante.
class EstudianteViewsets(viewsets.ModelViewSet):
    queryset=Estudiante.objects.all()
    serializer_class = EstudianteSerializers

#Persona
class PersonaViewsets(viewsets.ModelViewSet):
    queryset=Persona.objects.all()
    serializer_class = PersonaSerializers

#Visitante
class VisitanteViewsets(viewsets.ModelViewSet):
    queryset=Visitante.objects.all()
    serializer_class = VisitanteSerializers