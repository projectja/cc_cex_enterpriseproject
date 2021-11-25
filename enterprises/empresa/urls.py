from django.urls import path


from .views import IndexView, TablaEmpresaView


urlpatterns = [
   path('', IndexView.as_view(), name='index'),
   path('tabla-empresas/', TablaEmpresaView.as_view(), name='tabla_empresas'),
]
