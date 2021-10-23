import pprint

from django.shortcuts import render

from django.views.generic import TemplateView, View

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse

from .models import Empresa
from .forms import Filter



class IndexView(TemplateView):
   template_name = 'index.html'


class ListaEmpresaView(View):
   template_name = 'empresa/lista.html'
   
   @method_decorator(csrf_exempt)
   def dispatch(self, request, *args, **kwargs):
      return super().dispatch(request, *args, **kwargs)
   
   def get(self, *args, **kwargs):
      form = Filter()
      context = {
         'form': form
      } 
      return render(self.request, self.template_name, context)

   def post(self, *args , **kwargs):
      data = dict()
      try:

         data = list()
         filter_fields = dict()

         poblacion = self.request.POST.get('poblacion', None)
         sector = self.request.POST.get('sector', None)
         alpha = self.request.POST.get('alpha', None)

         if poblacion:
            filter_fields['poblacion__pk'] = poblacion
         
         if sector:
            filter_fields['sector__pk'] = sector

         if alpha and alpha != '---------':
            filter_fields['nombre__startswith'] = alpha
         
         if filter_fields == {}:
            for i in Empresa.objects.all():
               data.append(i.to_JSON())
         else:
            for i in Empresa.objects.filter(**filter_fields):
               data.append(i.to_JSON())

      except Exception as e:
         data['error'] = str(e)
      return JsonResponse(data, safe=False)