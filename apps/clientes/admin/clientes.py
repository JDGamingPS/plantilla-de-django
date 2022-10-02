from django.contrib import admin 
from apps.clientes.models.cliente import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = [
        'nombres',
        'apellidos',
        'numero_identidad',
        'fecha_nacimiento',
        'ingreso_mensual'
    ]