
from django.db import models
from django.contrib.auth.models import User
from django.forms import ImageField
from distutils.command.upload import upload
from AppCoder import admin



class Estudiante(models.Model):
    nombreEstudiante= models.CharField(max_length=40)
    programa= models.IntegerField()
    fecha= models.DateField()
    def __str__(self):
        return f"Nombre: {self.nombreEstudiante} - Edad: {self.edad} - Tipo: {self.tipo} - Motivo: {self.motivo} - Fecha: {self.fecha} - Costo: {self.costo} "

admin.site.register(Estudiante)

class Tutor(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    telefono= models.IntegerField()
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Telefono: {self.telefono} "

admin.site.register(Tutor)

class Programa(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=40)
    codigo = models.CharField(max_length=40)
    def __str__(self):
        return f"Nombre: {self.apellido} - Apellido: {self.apellido} - Codigo: {self.codigo} "
    
admin.site.register(Programa)    

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares',null=True, blank = True)
    
    
class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
