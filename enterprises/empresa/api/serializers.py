from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin
from django_countries.serializer_fields import CountryField
from django_countries import countries

from empresa.models import (
   Empresa, Municipio, 
   Product, Marca
)



class ActividadEmpresaSerializer(serializers.StringRelatedField):

   class Meta:
      model = Municipio
      fields = (
         'nombre',
      )


class EmpresaSerializer(CountryFieldMixin, serializers.ModelSerializer):
   logo = serializers.ImageField(use_url=True)
   direccion_actividad = ActividadEmpresaSerializer(many=True, read_only=True)
   sector_actividad = serializers.CharField(source='get_sector_actividad_display')
   export_frecuencia = serializers.CharField(source='get_export_frecuencia_display')
   volumen_facturacion = serializers.CharField(source='get_volumen_facturacion_display')
   empleados_fijos = serializers.CharField(source='get_empleados_fijos_display')
   obj_absolute_url = serializers.SerializerMethodField()


   class Meta:
      model = Empresa
      fields = (
         'id', 'logo',
         'export_destino',
         'name', 'sector_actividad', 
         'direccion_actividad', 'empleados_fijos', 
         'volumen_facturacion', 'export_frecuencia',
         'obj_absolute_url',
      )
      read_only_fields = fields

   def to_representation(self, instance):
      """Return 'export_destino' as a full name country representation"""
      ret = super().to_representation(instance)
      ret['export_destino'] = [dict(countries)[code] for code in ret['export_destino'] if code != '']
      return ret

   def get_obj_absolute_url(self, obj):
      return obj.get_absolute_url()