from django.db import models



class Contactos(models.Model):
    nombre = models.CharField(max_length=100, null= False, verbose_name="Nombre")
    telefono = models.CharField(max_length=15, null=True, blank=True, verbose_name="Telefono")
    celular = models.CharField(max_length=15, null= False, verbose_name="Celular")
    correo = models.CharField(max_length=254, null=False, verbose_name="Correo Eletronico")
    direccion = models.CharField(max_length=255, null=True, blank=True, verbose_name="Direccion")
    nacimiento = models.DateField(null=True, blank=True, verbose_name="Nacimiento")



