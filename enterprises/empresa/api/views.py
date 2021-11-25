from rest_framework.generics import ListAPIView
from django.db.models import Q

from .pagination import CustomPagination
from .serializers import EmpresaSerializer
from empresa.models import Empresa

from django.db import connection



class ApiEmpresaList(ListAPIView):

   serializer_class = EmpresaSerializer
   pagination_class = CustomPagination

   def dispatch(self, *args, **kwargs):
      response = super().dispatch(*args, **kwargs)
      print('Queries Counted: {}'.format(len(connection.queries)))
      return response

   def get_queryset(self):
      queryset = self.get_filter_queryset()

      return queryset

   def get_filter_queryset(self):
      query = self.request.GET.get('query')
      sector_actividad = self.request.GET.get('sector_actividad')
      direccion_actividad = self.request.GET.getlist('direccion_actividad')
      empleados_fijos = self.request.GET.get('empleados_fijos')
      empleados_eventuales = self.request.GET.get('empleados_eventuales')
      volumen_facturacion = self.request.GET.get('volumen_facturacion')
      export_frecuencia = self.request.GET.get('export_frecuencia')
      export_relativa = self.request.GET.get('export_relativa')
      export_destino = self.request.GET.getlist('export_destino')

      queryset = Empresa.objects.all()
      

      if query is not None and query != '':
         queryset = queryset.filter(
            Q(name__icontains=query) | 
            Q(productos_servicios__name__icontains=query) | 
            Q(productos_servicios__taric__icontains=query)| 
            Q(marcas_comerciales__name__icontains=query)
         ).distinct()

      if sector_actividad and sector_actividad != '':
         queryset = queryset.filter(
            sector_actividad=sector_actividad
         )
      
      if direccion_actividad and direccion_actividad != []:
         queryset = queryset.filter(
            direccion_actividad__in=direccion_actividad)

      if empleados_fijos and empleados_fijos != '':
         queryset = queryset.filter(
            empleados_fijos=empleados_fijos)

      if empleados_eventuales and empleados_eventuales != '':
         queryset = queryset.filter(
            empleados_eventuales=empleados_eventuales)

      if volumen_facturacion and volumen_facturacion != '':
         queryset = queryset.filter(
            volumen_facturacion=volumen_facturacion)

      if export_frecuencia and export_frecuencia != '':
         queryset = queryset.filter(
            export_frecuencia=export_frecuencia)

      if export_relativa and export_relativa != '':
         queryset = queryset.filter(
            export_relativa=export_relativa)

      if export_destino and export_destino != ['']:
         queryset = queryset.filter(
            export_destino__in=export_destino)

      return queryset