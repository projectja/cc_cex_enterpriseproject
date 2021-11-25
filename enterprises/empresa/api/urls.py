from django.urls import path

from .views import ApiEmpresaList


urlpatterns = [
   path('list', ApiEmpresaList.as_view(), name="empresa_list"),
]