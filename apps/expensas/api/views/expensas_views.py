from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from apps.expensas.api.serializers.expensas_serializer import ExpensasSerializer


class ExpensasListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ExpensasSerializer
    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.filter(status = True)
    def post(self,request):
        post = self.serializer_class(data= request.data)
        if post.is_valid():
            post.save()
            return Response({'message':'Elemento creado correctamente'},status = status.HTTP_201_CREATED )
        return Response ({'message' : 'Error al crear elemento'},status = status.HTTP_400_BAD_REQUEST)
    
    
class ExpensasRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExpensasSerializer
    
    def get_queryset(self,pk=None):
        
        if pk is None:
            return self.serializer_class.Meta.model.objects.filter(status = True)
        else:
            return self.serializer_class.Meta.model.objects.filter(status = True).filter(id = pk).first()
        
    def patch(self,request,pk=None):
        if self.get_queryset(pk):
            post_serializer = self.serializer_class(self.get_queryset(pk))
            return Response(post_serializer.data,status = status.HTTP_200_OK)
        return Response({'message':'No se encuentra un elemento con ese id'},status =status.HTTP_409_CONFLICT)
    def put(self,request,pk=None):
        if self.get_queryset(pk):
            post_serializer_update =self.serializer_class(self.get_queryset(pk),data = request.data)
            if post_serializer_update.is_valid():
                post_serializer_update.save()
                return Response(post_serializer_update.data,status =status.HTTP_200_OK) 
            return Response({'message':'Error al editar'},status = status.HTTP_404_NOT_FOUND)       
    def delete(self,request,pk=None):
        post = self.get_queryset(pk)
        if post:
            post.status =False
            post.save()
            return Response({'message' : 'Elemento eliminado correctamente'},status = status.HTTP_202_ACCEPTED)
        return Response({'message':'Error al eliminar '},status=status.HTTP_404_NOT_FOUND)        
    