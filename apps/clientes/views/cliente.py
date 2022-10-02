
from django.forms import modelform_factory
from pyexpat import model
from urllib import request
from django.utils import timezone
from django.shortcuts import render
from django.views.generic.list import ListView
from apps.clientes.models.cliente import Cliente
from django.shortcuts import redirect


""" class ClienteList(ListView):
    template_name = 'clientes/vista_clientes.html'
    model = Cliente
    queryset: Cliente.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Jorge'] = timezone.now()
        return context """
        
        
ClienteForm = modelform_factory(Cliente, exclude=[])

def nuevoCliente(request):
    if request.method == 'POST':
        formCliente = ClienteForm(request.POST)
        if formCliente.is_valid():
            formCliente.save()
            return redirect('../clientes/')
    else:
        formCliente = ClienteForm() 
        
    return render(request, 'clientes/formulario_cliente.html', {'formCliente': formCliente})

def bienvenido(request):
    no_personas_var = Cliente.objects.count()
    cliente = Cliente.objects.all()
    return render(request, 'clientes/vista_clientes.html', {'nro_personas': no_personas_var, 'cliente': cliente})

def detalleCliente(request, id):
    #clienteDetalle = Cliente.objects.get(pk=id)
    restaurante = Cliente.objects.get(pk=id).restaurante
    return render(request, 'clientes/detalle_cliente.html', {'restaurante': restaurante})

    
    
