from rest_framework import viewsets
from rest_framework.response import Response

from django.http import JsonResponse

from apps.personas.models import Estudiante, Visitante

from .models import Visita
from .serializer import VisitaSerializers

# Visita.
class VisitaViewsets(viewsets.ModelViewSet):
    queryset=Visita.objects.all()
    serializer_class = VisitaSerializers


class Consulta(viewsets.ViewSet):
    def list(self, request):
        queryset =  Visita.objects.values('id', 'visi_h_ingreso','visi_h_salida','visi_fecha','visitante__persona__pers_nombre', 'visitante__visit_procedencia','estudiante__persona__pers_nombre','estudiante__estu_edad','estudiante__tipo_estado__maes_nombre')
        return Response(queryset)
    #queryset = Visita.objects.values('id', 'visi_h_ingreso','visi_h_salida', 'visitante__visit_procedencia','estudiante__estu_edad').filter(visi_fecha__range=['2022-10-07', '2022-10-23'])

    def create(self, request, *args, **kwargs):
        fecha1 = request.data['fecha1']
        fecha2 = request.data['fecha2']

        visitas = Visita.objects.filter(
            visi_fecha__range=[fecha1, fecha2]).values('id', 'visi_h_ingreso','visi_h_salida','visi_fecha','visitante__persona__pers_nombre', 'visitante__visit_procedencia','estudiante__persona__pers_nombre','estudiante__estu_edad','estudiante__tipo_estado__maes_nombre')

        response = {
            "data": list(visitas)
        }

        return JsonResponse(response, safe=False)

class Consulta2(viewsets.ViewSet):
    def list(self, request):
        queryset =  Visitante.objects.values('id','persona__pers_nombre', 'persona__pers_apellido', 'tipo_parentesco__maes_nombre','tipo_sexo__maes_nombre','tipo_visitante__maes_nombre')
        return Response(queryset)

    def create(self, request, *args, **kwargs):
        regis = request.data['regis']

        visitantes = Visitante.objects.filter(tipo_visitante__maes_nombre= regis ).values('id','persona__pers_nombre','persona__pers_apellido','tipo_parentesco__maes_nombre','tipo_sexo__maes_nombre','tipo_visitante__maes_nombre')
        response = {
            "data": list(visitantes)
        }
        return JsonResponse(response, safe=False)

class Consulta3(viewsets.ViewSet):
    def list(self, request):
        queryset = Estudiante.objects.values('id','persona__pers_nombre','persona__pers_apellido','estu_edad' ,'tipo_estado__maes_nombre')

        return Response(queryset)

    def create(self, request, *args, **kwargs):
        edad = request.data['edad']

        estudiantes = Estudiante.objects.filter(estu_edad__gt=edad).values('id','persona__pers_nombre','persona__pers_apellido','estu_edad' ,'tipo_estado__maes_nombre')

        response = {
            "data": list(estudiantes)
        }
        return JsonResponse(response, safe=False)


class Consulta4(viewsets.ViewSet):
    def list(self, request):
        queryset = Estudiante.objects.values('id','estu_edad','persona__pers_nombre','persona__pers_identificacion','persona__tipo_identificacion__maes_valor')

        return Response(queryset)