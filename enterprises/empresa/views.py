import json

from django.views.generic import TemplateView, View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from django.db import connection

from .forms import (
   Filter, RequestEmpresaForm
)

from .models import Empresa



class IndexView(TemplateView):
   template_name = 'index.html'


class TablaEmpresaView(TemplateView):
   template_name = 'empresa/lista.html'


   def get_context_data(self, **kwargs):
      context = super(TablaEmpresaView, self).get_context_data(**kwargs)
      form = Filter()
      context['form'] = form
      
      return context


class EmpresaDetailView(TemplateView):
   template_name = 'empresa/detail.html'


class RequestEmpresaInfoView(View):
   
   @method_decorator(csrf_exempt)
   def dispatch(self, *args, **kwargs):
      return super().dispatch(*args, **kwargs)
      # print('Queries Counted: {}'.format(len(connection.queries)))
      # return response

   def post(self, *args, **kwargs):
      try:
         data_form = {
            'request_email': self.request.POST.get('request_email'),
            'request_f_name': self.request.POST.get('request_f_name'),
            'request_l_name': self.request.POST.get('request_l_name'),
         }
         list_emp_selecteds = json.loads(self.request.POST.get('request_empresa_list'))

         form = RequestEmpresaForm(data_form)
         
         if form.is_valid():
            selecteds = list()
            instance = form.save()
            
            for empresa_id in list_emp_selecteds:
               selecteds.append(empresa_id["id"])

            queryset = Empresa.objects.filter(id__in=selecteds)
            instance.empresas.set(list(queryset))
            resp = {
               "status": 200,
               "message": "Solicitud procesada exitosamente."
            }

            return JsonResponse(resp, safe=True)
         else:
            return JsonResponse({"error": form.errors, "status": 400}, safe=True)
      except Exception as e:
            return JsonResponse({"error": str(e), "status": 500}, safe=True)
