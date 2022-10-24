from django.shortcuts import render
from rest_framework import viewsets
from .models import Maestra
from .serializer import MaestraSerializers
# Create your views here.

class MaestraViewsets(viewsets.ModelViewSet):
    queryset=Maestra.objects.all()
    serializer_class = MaestraSerializers