from django.db import models

class Restaurante(models.Model):
    nombre = models.CharField(
        verbose_name = 'Nombre',
        help_text = 'Nombre del restaurante',
        max_length = 200
    )
    
    ubicacion = models.CharField(
        verbose_name = 'Ubicacion',
        help_text = 'Ubicacion del restaurante',
        max_length = 200
    )
    
    pais = models.CharField(
        verbose_name = 'pais',
        help_text = 'Pais',
        max_length = 50
    )
    
    class Meta:
        app_label = 'clientes'
        db_table = 'restaurante'
        verbose_name = "Restaurante"
        verbose_name_plural = "Restaurantes" 
        
    def __str__(self):
        return self.nombre