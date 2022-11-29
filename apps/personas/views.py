from rest_framework import viewsets


from .models import Estudiante, Persona, Visitante, Actualizando
from .serializer import EstudianteSerializers, PersonaSerializers, VisitanteSerializers, ActualizandoSerializers


# Estudiante.
class EstudianteViewsets(viewsets.ModelViewSet):
    queryset=Estudiante.objects.all()
    serializer_class = EstudianteSerializers

#Persona
from django_filters.rest_framework import DjangoFilterBackend
class PersonaViewsets(viewsets.ModelViewSet):
    queryset=Persona.objects.all()
    serializer_class = PersonaSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['pers_nombre']

#Visitante
class VisitanteViewsets(viewsets.ModelViewSet):
    queryset=Visitante.objects.all()
    serializer_class = VisitanteSerializers

#Actualizando
class ActualizandoViewsets(viewsets.ModelViewSet):
    queryset=Actualizando.objects.all()
    serializer_class = ActualizandoSerializers



    
