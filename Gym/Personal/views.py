from django.shortcuts import render
from django.http import HttpResponse
from .models import Empleados, Miembros, Clases
from .forms import Empleados_formulario, Miembros_formulario, Clases_formulario, Busco_Empleados

def index (request):
    return render(request, 'main/index.html')

def Empleados_form(request):
    if request.method == "POST":
        myform = Empleados_formulario(request.POST)
        print(myform)
        if myform.is_valid:
            informacion = myform.cleaned_data
            empleados = Empleados(nombre=informacion['nombre'], apellido=informacion['apellido'], edad=informacion['edad'], profesion=informacion['profesion'], telefono=informacion['telefono'])
            empleados.save()
            return render(request, 'main/index.html')
    return render(request, 'main/Empleados.html')

def Miembros_form(request):
    if request.method == "POST":
        myform = Miembros_formulario(request.POST)
        print(myform)
        if myform.is_valid:
            informacion = myform.cleaned_data
            miembros = Miembros(nombre=informacion['nombre'], apellido=informacion['apellido'], edad=informacion['edad'], mail=informacion['mail'], telefono=informacion['telefono'])
            miembros.save()
            return render(request, 'main/index.html')
    return render(request, 'main/Miembros.html')

def Clases_form(request):
    if request.method == "POST":
        myform = Clases_formulario(request.POST)
        print(myform)
        if myform.is_valid:
            informacion = myform.cleaned_data
            clases = Clases(nombre=informacion['nombre'], horario=informacion['horario'])
            clases.save()
            return render(request, 'main/index.html')
    return render(request, 'main/Clases.html')

def buscar(request):
    if request.method == "POST":
        myform = Busco_Empleados(request.POST)
        if myform.is_valid():
            info= myform.cleaned_data
            nombre= Empleados.objects.filter(nombre__icontains=info["nombre"])
            return render(request, 'main/mostrar.html',{"nombre": nombre})
        else:
            print("false")
    else:
        print("something")
        myform = Busco_Empleados()

    return render(request, "main/buscar.html", {"myform": myform})

