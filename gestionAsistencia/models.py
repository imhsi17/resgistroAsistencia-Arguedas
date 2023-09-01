from django.db import models

# Create your models here.
class Alumnos(models.Model):
    
    nombre = models.CharField(max_length=75)
    DNI =models.CharField(max_length=8)
    contraseña = models.CharField(max_length=9)
    grado = models.IntegerField()
    seccion = models.CharField(max_length=1)
    
    def __str__(self):
        return self.nombre
    
class Puntual(models.Model):
    
    DNI = models.CharField(max_length=8)
    fecha_ingreso = models.DateField()
    hora_ingreso = models.TimeField()
        
    def __str__(self):
        return "El día %s ingresó a las %s. " %(self.fecha_ingreso, self.hora_ingreso)
           
class Atrasado(models.Model):
    
    DNI = models.CharField(max_length=8)
    fecha_ingreso = models.DateField()
    hora_ingreso = models.TimeField()
    
    def __str__(self):
        return "El día %s ingresó a las %s. " %(self.fecha_ingreso, self.hora_ingreso)
