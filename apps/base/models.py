from django.db import models


# Create your models here.
class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.BooleanField(verbose_name="Estado",default = True)
    created_date = models.DateField(verbose_name="fecha creacion",auto_now= True,auto_now_add=False)
    modified_date = models.DateField(verbose_name="fecha modificacion",auto_now=False,auto_now_add=True)
    class Meta:
        verbose_name ="Modelo Base"
    
    def __str__(self):
        pass
    