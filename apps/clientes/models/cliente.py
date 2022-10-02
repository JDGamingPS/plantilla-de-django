
from django.db import models

class Cliente(models.Model):
    nombres = models.CharField(
        verbose_name = 'Nombre',
        help_text = 'Nombres del cliente',
        max_length=200
    )

    apellidos = models.CharField(
        verbose_name = 'Apellidos',
        help_text = 'Apellidos del cliente',
        max_length = 254
    )

    numero_identidad = models.CharField(
        verbose_name = 'Numero de Idnetidad',
        help_text='Numero de identidad del cliente',
        max_length = 10
    )

    fecha_nacimiento = models.DateField(
        verbose_name = 'fecha de nacimiento',
        help_text = 'fecha de nacimiento del cliente',
        blank=True, null=True
    )

    ingreso_mensual = models.DecimalField(
        verbose_name = 'monto de ingresos',
        help_text = 'Monto de ingresos',
        decimal_places = 2,
        max_digits = 10,
        blank = True, null=True
    )


    def __str__(self):
        return self.nombres
    

    class Meta:
        app_label = 'clientes'
        db_table = 'cliente'
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
