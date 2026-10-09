from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre=models.CharField(max_length=40)
    camada= models.IntegerField()
    def __str__(self) -> str:
        return f"{self.nombre} - {self.camada}"

class Estudiante(models.Model):
    nombre=models.CharField(max_length=40)
    email=models.EmailField()
    profesion=models.CharField(max_length=40)
    def __str__(self) -> str:
        return f"{self.nombre} - {self.profesion} | {self.email}"

class Profesor(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.EmailField()
    profesion=models.CharField(max_length=40)
    def __str__(self) -> str:
        return f"{self.nombre} - {self.apellido} | {self.profesion}"
class Entregable(models.Model):
    nombre=models.CharField(max_length=40)
    fecha_entrega=models.DateField(max_length=40)
    entregado=models.BooleanField(default=False)
    def __str__(self) -> str: #fixeamos el bug cursos object 1
        return f"{self.nombre} - {self.fecha_entrega} | {self.entregado}"