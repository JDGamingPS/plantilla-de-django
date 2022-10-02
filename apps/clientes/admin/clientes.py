from django.contrib import admin 
from apps.clientes.models.cliente import Cliente
from apps.clientes.models.restaurante import Restaurante

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = [
        'nombres',
        'apellidos',
        'numero_identidad',
        'fecha_nacimiento',
        'ingreso_mensual'
    ]

@admin.register(Restaurante)
class RestauranteAdmin(admin.ModelAdmin):
    list_display = [
        'nombre',
        'ubicacion',
        'pais',
        
    ]