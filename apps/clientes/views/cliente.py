
from django.utils import timezone
from django.shortcuts import render
from django.views.generic.list import ListView
from apps.clientes.models import Cliente

""" class ClienteList(ListView):
    template_name = 'clientes/vista_clientes.html'
    model = Cliente
    queryset: Cliente.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Jorge'] = timezone.now()
        return context """
        
def bienvenido(request):
    no_personas_var = Cliente.objects.count()
    cliente = Cliente.objects.all()
    return render(request, 'clientes/vista_clientes.html', {'nro_personas': no_personas_var, 'cliente': cliente})

    
    
