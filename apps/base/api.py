from rest_framework import generics

class GeneralListAPIView(generics.ListAPIView):
    serializer_class = None
    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.filter(estado=True)