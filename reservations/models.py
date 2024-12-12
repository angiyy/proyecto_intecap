from django.db import models

class Habitacion(models.Model):
    TIPO_HABITACION = [
        ('SIMPLE', 'Simple'),
        ('DOBLE', 'Doble'),
        ('SUITE', 'Suite'),
    ]
    tipo = models.CharField(max_length=50, choices=TIPO_HABITACION)
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.tipo} - ${self.precio_por_noche}"

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    numero_huespedes = models.PositiveIntegerField()

    def __str__(self):
        return f"Reserva de {self.cliente.nombre} para {self.habitacion.tipo}"
