from django import forms

class Miembros_formulario(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=35)
    edad=forms.IntegerField()
    mail=forms.EmailField(max_length=100)
    telefono=forms.IntegerField()

class Empleados_formulario(forms.Form):
    nombre=forms.CharField(max_length=35)
    apellido=forms.CharField(max_length=35)
    edad=forms.IntegerField()
    profesion=forms.CharField(max_length=30)
    telefono=forms.IntegerField()

class Clases_formulario(forms.Form):
    nombre=forms.CharField(max_length=35)
    horario=forms.IntegerField()

class Busco_Empleados(forms.Form):
    nombre = forms.CharField()
