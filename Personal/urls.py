from . import views
from django.urls import path

app_name= "Personal"

urlpatterns =[
    path('', views.index, name='index'),
    path('Empleados', views.Empleados_form, name="Empleados"),
    path('Miembros', views.Miembros_form, name="Miembros"),
    path('Clases', views.Clases_form, name="Clases"),
    path('buscar', views.buscar, name="Buscar"),
]