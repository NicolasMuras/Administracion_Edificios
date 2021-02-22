from rest_framework import serializers
from apps.expensas.models import Edificio,Expensas,Departamento

class EdificioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edificio
        exclude = ('created_date','modified_date')
    

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        exclude = ('created_date','modified_date')
    