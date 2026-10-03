from django.db import models
from django.contrib.auth.models import User


class Region(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Comuna(models.Model):
    nombre = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class TipoInmueble(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Inmueble(models.Model):

    arrendador = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="inmuebles"
    )

    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    m2_construidos = models.FloatField()
    m2_totales = models.FloatField()
    estacionamientos = models.IntegerField()
    habitaciones = models.IntegerField()
    banos = models.IntegerField()
    direccion = models.CharField(max_length=200)

    comuna = models.ForeignKey(
        Comuna,
        on_delete=models.CASCADE
    )

    tipo_inmueble = models.ForeignKey(
        TipoInmueble,
        on_delete=models.CASCADE
    )

    precio_mensual = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return self.nombre
    
class PerfilUsuario(models.Model):

    TIPOS_USUARIO = [
        ("arrendatario", "Arrendatario"),
        ("arrendador", "Arrendador"),
    ]

    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    nombre = models.CharField(
        max_length=100
    )

    apellido = models.CharField(
        max_length=100
    )

    tipo_usuario = models.CharField(
        max_length=20,
        choices=TIPOS_USUARIO
    )

    def __str__(self):
        return f"{self.nombre} {self.apellido}"