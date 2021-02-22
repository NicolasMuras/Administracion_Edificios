from rest_framework import serializers

from apps.expensas.models import Expensas


class ExpensasSerializer(serializers.ModelSerializer):
    status= serializers.BooleanField()
    total_gastos = serializers.FloatField()


    class Meta:
        model = Expensas
        exclude = ('created_date','modified_date')
        
    def validate_status(self,value):
        if value == False:
            raise serializers.ValidationError('Error,El Total no puede ser 0')
        return value
    
    def validate_total_gastos(self,value):
        if value <0:
            raise serializers.ValidationError()
        return value
    def validate(self, data):
        return data