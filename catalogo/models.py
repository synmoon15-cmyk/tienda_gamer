from django.db import models


class Plataforma(models.Model):
    """Modelo PADRE (clasificador). Solo se gestiona desde Django Admin."""
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Videojuego(models.Model):
    """Modelo HIJO (operativo). Tiene el CRUD web completo."""
    plataforma = models.ForeignKey(Plataforma, on_delete=models.PROTECT)
    titulo = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    fecha_lanzamiento = models.DateField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
