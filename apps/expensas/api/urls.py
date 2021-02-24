
from django.contrib import admin
from django.urls import path
from apps.expensas.api.views.expensas_views import ExpensasListCreateAPIView,ExpensasRetrieveUpdateDestroyAPIView
from apps.expensas.api.views.general_views import GeneratePDF


urlpatterns = [
    path('list-create/', ExpensasListCreateAPIView.as_view(),name ="list-create"),
    path('retrieve-update-destroy/<int:pk>/',ExpensasRetrieveUpdateDestroyAPIView.as_view(),name ="retrieve-update-destroy"),
    path('pdf/',GeneratePDF.as_view(), name = "pdf")
    
]
