from django.db import models
from django.forms.models import model_to_dict
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
   FREQ_EXPORT, STATUS_SOLICITUD
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


class EmpresaManager(models.Manager):

   def get_data_rows(self, list_pk, *args):
      """Return a tuple that represent a data row of each model fields to be presented in an excel table."""
      rows = list()

      # TODO Improve: as know if these fields name is part of one incoming fields.
      choices_fields_name = [
         "sector_actividad", "pyme", 
         "empleados_fijos", "empleados_eventuales",
         "volumen_facturacion", "export_frecuencia",
         "export_relativa",
      ]

      queryset = self.get_queryset().filter(pk__in=list_pk).values(*args)

      for obj in queryset:
         for value in obj.keys():
            if value in choices_fields_name:
               key_option = obj[value]
               human_redable_option = self.get_human_redable_option(key_option, value)
               obj[value] = human_redable_option

         rows.append(tuple(obj.values()))
      return rows

   def get_map_choice_options(self, field):
      # Return a dict for a choices options.
      return dict((k, v) for k, v in self.model._meta.get_field(field).choices)

   def get_human_redable_option(self, key, field_name):
      # Return a human redable option of a
      # choice.
      choices = self.get_map_choice_options(field_name)

      return choices[key] 


class Empresa(models.Model, ResizeImageMixin):
   """   
      Representa un registro de una empresa en la base de datos.
      Con todas sus descripciones; actividades, datos generales,
      persona de contacto, datos economicos, datos sonre exportacion,
      productos y servicios. 
   """


   # Datos Actividad
   sector_actividad = models.CharField(max_length=100, choices=PRODUCTOS_SERVICIOS)
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


   objects = EmpresaManager()




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



class Solicitud(models.Model):
   """
      Representa una solicitud de informacion del detalle
      de una o varias empresas, seleccionadas en la tabla
      de empresas, por parte de un usuario.
   """

   request_email = models.EmailField(max_length=254)
   request_f_name = models.CharField(max_length=250)
   request_l_name = models.CharField(max_length=250)
   empresas = models.ManyToManyField(Empresa)
   status = models.IntegerField(default=0, choices=STATUS_SOLICITUD)
   request_date = models.DateTimeField(auto_now_add=True)


   def __str__(self):
      return self.request_email