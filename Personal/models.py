from django.db import models

class Miembros(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=35)
    edad=models.IntegerField()
    mail=models.EmailField(max_length=100)
    telefono=models.IntegerField()

class Empleados(models.Model):
    nombre=models.CharField(max_length=35)
    apellido=models.CharField(max_length=35)
    edad=models.IntegerField()
    profesion=models.CharField(max_length=30)
    telefono=models.IntegerField()

class Clases(models.Model):
    nombre=models.CharField(max_length=35)
    horario=models.IntegerField()


