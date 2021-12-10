from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext


from .utils import send_email_with_enterprise_info, create_excel_file

from .models import (
   Empresa, Marca, Product, 
   Municipio, Provincia, Solicitud
)


def send_enterprise_info(modeladmin, request, queryset):

   for obj in queryset:
      user_email = obj.request_email
      ids_request_emp = [emp_id[0] for emp_id in obj.empresas.values_list('id')]
      excel_file = create_excel_file(ids_request_emp)
      send_email_with_enterprise_info(user_email, excel_file)
      


@admin.register(Solicitud)
class SolicitudAdmin(admin.ModelAdmin):
   list_display = [
      'request_email',
      'request_f_name',
      'status',
      'request_date',
   ]
   list_filter = ['request_email', 'status', 'request_date']
   actions = [send_enterprise_info]



admin.site.register(Empresa)
admin.site.register(Marca)
admin.site.register(Product)
admin.site.register(Provincia)
admin.site.register(Municipio)