from django.db import models

# Create your models here.

class Planta(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='plantas/', null=True, blank=True)

    def __str__(self):
        return self.nombre

    def delete(self, *args, **kwargs):
        self.imagen.delete()
        super().delete(*args, **kwargs)