from django.db import models




class Poblacion(models.Model):
   nombre = models.CharField(max_length=250)


   def __str__(self):
      return self.nombre


class Sector(models.Model):
   nombre = models.CharField(max_length=250)
   direccion = models.CharField(max_length=250)


   def __str__(self):
      return self.nombre


class Empresa(models.Model):
   nombre = models.CharField(max_length=250)
   poblacion = models.ForeignKey(Poblacion, on_delete=models.CASCADE)
   sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
   partidas = models.CharField(max_length=100)


   def __str__(self):
      return self.nombre
