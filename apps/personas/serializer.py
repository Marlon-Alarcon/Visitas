from rest_framework import serializers
from .models import Estudiante, Persona, Visitante, Actualizando


class PersonaSerializers(serializers.ModelSerializer):

    #tipo_identificacion = serializers.StringRelatedField()
    #tipo_identificacion = serializers.StringRelatedField()

    class Meta:
        model = Persona
        fields = ['id','pers_nombre','pers_apellido','pers_identificacion','tipo_identificacion']

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'pers_nombre' : instance.pers_nombre,
            'pers_apellido' : instance.pers_apellido,
            'pers_identificacion' : instance.pers_identificacion,
            'tipo_identificacion' : instance.tipo_identificacion.maes_nombre,
        }



#Estudiante       
class EstudianteSerializers(serializers.ModelSerializer):
    
    #persona = PersonaSerializers(allow_null=True)
    class Meta:
        model = Estudiante
        fields = ['id','estu_edad','persona','tipo_estado']

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'estu_edad': instance.estu_edad,
            'persona': instance.persona.pers_nombre,
            'tipo_estado': instance.tipo_estado.maes_nombre,
        }

#Visitante
class VisitanteSerializers(serializers.ModelSerializer):

    #persona = PersonaSerializers(allow_null=True)
    #estudiante = EstudianteSerializers(allow_null=True)
    class Meta:
        model = Visitante
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'visit_telefono' : instance.visit_telefono,
            'visit_procedencia' : instance.visit_procedencia,
            'persona' : instance.persona.pers_nombre,
            'tipo_parentesco' : instance.tipo_parentesco.maes_nombre,
            'tipo_sexo' : instance.tipo_sexo.maes_nombre,
            'tipo_visitante' : instance.tipo_visitante.maes_nombre,
        }

class ActualizandoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Actualizando
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'fecha' : instance.fecha,
            'accion' : instance.accion,
            'pers' : instance.pers.pers_nombre,
        }
