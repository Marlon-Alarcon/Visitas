from rest_framework import serializers
from .models import Maestra

#Maestra
class MaestraSerializers(serializers.ModelSerializer):

    #persona = serializers.StringRelatedField()
    #tipo_estado = serializers.StringRelatedField()
    
    class Meta:
        model = Maestra
        fields = '__all__'