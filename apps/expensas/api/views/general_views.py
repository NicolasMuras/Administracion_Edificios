from apps.base.api import GeneralListAPIView
from apps.expensas.api.serializers.general_serializer import EdificioSerializer, DepartamentoSerializer


class EdificioSerializerListAPIVIew(GeneralListAPIView):
    serializer_class = EdificioSerializer
    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.filter(status = True)

class DepartamentoSerializerListAPIView(GeneralListAPIView):
    serializer_class = DepartamentoSerializer
    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.filter(status = True)
    
    