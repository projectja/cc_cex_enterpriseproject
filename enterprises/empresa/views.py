from django.views.generic import TemplateView

from .forms import Filter



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