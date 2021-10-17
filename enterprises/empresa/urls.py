from django.urls import path

from .views import IndexView, ListaEmpresaView


urlpatterns = [
   path('', IndexView.as_view(), name='index'),
   path('lista-empresas/', 
         ListaEmpresaView.as_view(), name='lista_empresas'),

]