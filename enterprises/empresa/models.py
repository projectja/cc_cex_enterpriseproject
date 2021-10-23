from django.db import models
from django.forms import model_to_dict



class Poblacion(models.Model):
   nombre = models.CharField(max_length=250)


   def __str__(self):
      return self.nombre

   def to_JSON(self):
      item = model_to_dict(self)

      return item

class Sector(models.Model):
   nombre = models.CharField(max_length=250)
   direccion = models.CharField(max_length=250)


   def __str__(self):
      return self.nombre

   def to_JSON(self):
      item = model_to_dict(self)

      return item


class Empresa(models.Model):
   nombre = models.CharField(max_length=250)
   poblacion = models.ForeignKey(Poblacion, on_delete=models.CASCADE)
   sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
   partidas = models.CharField(max_length=100)


   def __str__(self):
      return self.nombre

   
   def to_JSON(self):
      item = model_to_dict(self)
      item['poblacion'] = self.poblacion.to_JSON()
      item['sector'] = self.poblacion.to_JSON()


      return item