from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.core.validators import RegexValidator
from django_countries.fields import CountryField


from PIL import Image


from .resizer import ResizeImageMixin
from .constants import (
   PRODUCTOS_SERVICIOS,
   PYME, EMP_FIJOS,
   EMP_EVENT, VOL_FACT,
   FREQ_EXPORT,
)


# REGEX to handle Phones fields.
regex_phone = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="EL numero de telefono debe ser en el formato de: +9999999999.")




class Provincia(models.Model):
   """
      Representa una provincia, dentro
      de España.
   """
   nombre = models.CharField(max_length=100)


   def __str__(self):
      return self.nombre
   

class Municipio(models.Model):
   """
      Representa un municipio, de una
      provincia en especifica.
   """
   nombre = models.CharField(max_length=100)
   provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)


   def __str__(self):
      return self.nombre


class Marca(models.Model):
   """
      Representa una marca en especifica,
      que una empresa exporta.
   """
   name = models.CharField(max_length=100)


   def __str__(self):
      return self.name
   

class Product(models.Model):
   """
      Representa un producto en especifico,
      que exporta una empresa.
   """
   name = models.CharField(max_length=100)
   taric = models.IntegerField()
   marca = models.ForeignKey('Marca', on_delete=models.SET_NULL, null=True)
   empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE, related_name="productos_servicios")


   def __str__(self):
      return f"{self.taric} - {self.name}"


class Empresa(models.Model, ResizeImageMixin):
   """   
      Representa un registro de una empresa en la base de datos.
      Con todas sus descripciones; actividades, datos generales,
      persona de contacto, datos economicos, datos sonre exportacion,
      productos y servicios. 
   """


   # Datos Actividad
   sector_actividad = models.CharField(max_length=5, choices=PRODUCTOS_SERVICIOS)
   otro_producto_servicio = models.CharField(max_length=150, null=True, blank=True)

   # Datos Generales.
   logo = models.ImageField(blank=True, upload_to='images/')
   name = models.CharField(max_length=250)
   cif = models.CharField(max_length=10)
   pyme = models.IntegerField(choices=PYME)
   direccion_fiscal = models.CharField(max_length=250)
   direccion_actividad = models.ManyToManyField(Municipio, related_name="direccion")
   phone_empresa = models.CharField(validators=[regex_phone], max_length=17)
   email_empresa = models.EmailField(max_length=254)

   # Persona de contacto.
   nombre_persona_contacto = models.CharField(max_length=150, help_text="Nombre de Persona de contacto.")
   cargo_persona_contacto = models.CharField(max_length=150, help_text="Cargo de persona de contacto.")
   email_persona_contacto = models.EmailField(max_length=254, help_text="Email de la persona de contacto.")
   phone_persona_contacto = models.CharField(validators=[regex_phone], max_length=17)
   ceo_nombre = models.CharField(max_length=150, help_text="Nombre de CEO or Gerente.", null=True, blank=True)
   ceo_email = models.EmailField(max_length=254, help_text="Email de CEO or Gerente.", null=True, blank=True)
   ceo_phone = models.CharField(validators=[regex_phone], max_length=17, null=True, blank=True)

   # Redes Sociales.
   web = models.URLField(null=True, blank=True)
   instagram = models.URLField(null=True, blank=True)
   linkedin = models.URLField(null=True, blank=True)
   otro_redes = models.URLField(null=True, blank=True)

   # Datos economicos.
   empleados_fijos = models.CharField(max_length=2, choices=EMP_FIJOS)
   empleados_eventuales = models.CharField(max_length=3, choices=EMP_EVENT)
   volumen_facturacion = models.CharField(max_length=3, choices=VOL_FACT)

   # Datos sobre exportacion.
   export_frecuencia = models.CharField(max_length=2, choices=FREQ_EXPORT)
   export_relativa = models.CharField(max_length=3, choices=VOL_FACT)
   export_vol = models.PositiveSmallIntegerField()
   export_destino = CountryField(multiple=True)



   class Meta:
      ordering = ('name',)
      indexes = [
         models.Index(fields=['cif'], name="empresa_idx")
      ]
   

   def save(self, *args, **kwargs):
      if self.pk is None and self.logo:
         self.resize(self.logo, (200, 200), self.name)
      super().save(*args, **kwargs)

   def __str__(self):
      return self.name

   def get_absolute_url(self):
      return reverse('empresa_detail', kwargs={'pk': self.pk})