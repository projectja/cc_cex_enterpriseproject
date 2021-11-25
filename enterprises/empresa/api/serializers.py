from rest_framework import serializers

from empresa.models import (
   Empresa, Municipio, 
   Product, Marca, Countries
)



class ActividadEmpresaSerializer(serializers.StringRelatedField):

   class Meta:
      model = Municipio
      fields = (
         'nombre',
      )


class CountriesEmpresaSerializer(serializers.StringRelatedField):

   class Meta:
      model = Countries
      fields = (
         'name',
      )


class EmpresaSerializer(serializers.ModelSerializer):

   export_destino = CountriesEmpresaSerializer(many=True, read_only=True)
   direccion_actividad = ActividadEmpresaSerializer(many=True, read_only=True)
   sector_actividad = serializers.CharField(source='get_sector_actividad_display')
   export_frecuencia = serializers.CharField(source='get_export_frecuencia_display')
   volumen_facturacion = serializers.CharField(source='get_volumen_facturacion_display')
   empleados_fijos = serializers.CharField(source='get_empleados_fijos_display')


   class Meta:
      model = Empresa
      fields = (
         'id',
         'export_destino',
         'name', 'sector_actividad', 
         'direccion_actividad',  'empleados_fijos', 
         'volumen_facturacion', 'export_frecuencia',
         'productos_servicios', 'marcas_comerciales'
      )
      read_only_fields = fields