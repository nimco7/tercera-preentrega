from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()
    anio = models.IntegerField()
    
    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.descripcion}"
    
    
    
class Categoria(models.Model):
    categoria = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.categoria}"
    
    
class Resenia(models.Model):
    resenia = models.CharField(max_length=250)
    
    def __str__(self):
        return f"{self.resenia}"