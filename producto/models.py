from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return f'Producto: {self.nombre}'