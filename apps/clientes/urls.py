from django.urls import path
from apps import clientes
from apps.clientes import views
from apps.clientes.views.cliente import bienvenido, detalleCliente, nuevoCliente

app_name = 'cliente'

urlpatterns = [
    #path('clientes/', ClienteList.as_view(), name='cliente_lista'),
    path('clientes/', bienvenido, name='lista'),
    path('clientes/formulario_cliente', nuevoCliente),
    path('clientes/detalle_cliente/<int:id>', detalleCliente)
]