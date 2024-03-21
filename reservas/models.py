from django.db import models
from django.contrib.auth.models import User

class Habitacion(models.Model):
    TIPO_CHOICES = (
        ('individual', 'Individual'),
        ('doble', 'Doble'),
        ('suite', 'Suite'),
    )
    numero = models.CharField(max_length=50, unique=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    descripcion = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.numero
    
class Reserva(models.Model):
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Reserva de {self.habitacion} por {self.usuario}"

