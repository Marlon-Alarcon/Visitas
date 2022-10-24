from rest_framework import serializers
from .models import Visita


class VisitaSerializers(serializers.ModelSerializer):

    class Meta:
        model = Visita
        fields = ['id','visi_h_ingreso','visi_h_salida','visi_fecha','visitante','estudiante']

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'visi_h_ingreso' : instance.visi_h_ingreso,
            'visi_h_salida' : instance.visi_h_salida,
            'visi_fecha' : instance.visi_fecha,
            'visitante' : instance.visitante.persona.pers_nombre,
            'estudiante' : instance.estudiante.persona.pers_nombre,
        }