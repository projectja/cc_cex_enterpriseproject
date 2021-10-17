from django.shortcuts import render

from django.views.generic import TemplateView
from django_filters.views import FilterView

from .filters import EmpresaFilter
from .models import Empresa

class IndexView(TemplateView):
   template_name = 'index.html'



class ListaEmpresaView(FilterView):
   filterset_class = EmpresaFilter
   template_name = 'empresa/lista.html'
   paginate_by = 6 