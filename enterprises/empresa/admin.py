from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext


from .utils import send_email_with_enterprise_info, create_excel_file

from .models import (
   Empresa, Marca, Product, 
   Municipio, Provincia, Solicitud
)



@admin.register(Solicitud)
class SolicitudAdmin(admin.ModelAdmin):
   list_display = [
      'request_email',
      'request_f_name',
      'status',
      'request_date',
   ]
   list_filter = ['request_email', 'status', 'request_date']
   

   def send_enterprise_info(self, request, queryset):
      for obj in queryset:
         user_email = obj.request_email
         ids_request_emp = [emp_id[0] for emp_id in obj.empresas.values_list('id')]
         excel_file = create_excel_file(ids_request_emp)
         send_email_with_enterprise_info(user_email, excel_file)
      
      updated = queryset.update(status=1)

      self.message_user(request, ngettext(
         '%d solicitud fue enviada y actualizada de forma exitosa.',
         '%d solicitudes fueron enviadas y actualizadas de forma exitosa.',
         updated,
      ) % updated, messages.SUCCESS)

   actions = [send_enterprise_info]

admin.site.register(Empresa)
admin.site.register(Marca)
admin.site.register(Product)
admin.site.register(Provincia)
admin.site.register(Municipio)