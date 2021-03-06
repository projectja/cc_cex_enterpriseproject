from django.urls import path


from .views import (
   IndexView, TablaEmpresaView, 
   EmpresaDetailView, RequestEmpresaInfoView
)


urlpatterns = [
   path('', IndexView.as_view(), name='index'),
   path('tabla-empresas/', TablaEmpresaView.as_view(), name='tabla_empresas'),
   path('empresa-detail/<int:pk>/', EmpresaDetailView.as_view(), name='empresa_detail'),
   path('tabla-empresas/request-empresa-info/', RequestEmpresaInfoView.as_view(), name='request_empresa_info'),
]
