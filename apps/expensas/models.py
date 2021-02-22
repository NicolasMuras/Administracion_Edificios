from django.db import models
from apps.base.models import BaseModel

# Create your models here.
class Edificio(BaseModel):
    nombre = models.CharField(max_length = 50 ,verbose_name="Edificio")
    class Meta:
        verbose_name ="Edificio"
        verbose_name_plural = "Edificios"
    def __str__(self):
        return self.nombre

class Departamento(BaseModel):
    descipcion = models.CharField(max_length=50, verbose_name="Descripcion")
    porcentaje = models.FloatField(verbose_name="Porcentaje")
    class Meta:
        verbose_name ="Departamento"
        verbose_name_plural ="Departamentos"
    
    def __str__(self):
        return self.descipcion
    
    
class Expensas(BaseModel):
    nombre = models.CharField(max_length=50,verbose_name="Nombre",default ="Expensa")
    edificio_expensa= models.ForeignKey(Edificio,on_delete=models.CASCADE,verbose_name="Edificio")
    expensas_puras = models.FloatField(verbose_name="Expensas Puras",blank = True, null = True)
    intereses_mora = models.FloatField(verbose_name="Intereses por Mora",blank = True, null = True)
    materiales_limpieza = models.FloatField(verbose_name="materiales de limpieza",blank = True, null = True)
    servicios_luz= models.FloatField(verbose_name="servicios electricidad",blank = True, null = True)
    sueldo_administrador = models.FloatField(verbose_name="Sueldo Administrador",blank = True, null = True)
    ascensores = models.FloatField(verbose_name="Gasto Ascensores",blank = True, null = True)
    aportes_encargado_limpieza = models.FloatField(verbose_name="Aportes Encargado Limpieza",blank = True, null = True)
    sueldo_encargado_limpieza = models.FloatField(verbose_name="Sueldo Encargado Limpieza",blank = True, null = True)
    seguro_edificio = models.FloatField(verbose_name="Seguro Edificio",blank = True, null = True)
    sueldo_anual_complementario = models.FloatField(verbose_name="Sueldo Anual Complementario",blank = True, null = True)
    total_gastos = models.FloatField(verbose_name="Total")
    departamento_expensa = models.ForeignKey(Departamento, on_delete= models.CASCADE,verbose_name="Departamento",blank = True, null = True)
    
    
    class Meta:
        verbose_name = "Expensas"
        verbose_name_plural = "Expensas"
        
    def __str__(self):
        return self.nombre
        