from django.db import models


class Destino(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    dias = models.PositiveIntegerField()
    imagen = models.URLField()

    ciudad = models.CharField(max_length=100, blank=True)
    destacado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre}, {self.pais}"