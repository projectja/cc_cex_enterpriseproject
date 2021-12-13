import xlwt
import base64
from django.conf import settings
from io import BytesIO
from django.http import HttpResponse

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (
	Mail, Attachment, FileContent, FileName,
	FileType, Disposition, ContentId
)

from .models import Empresa
from .api.serializers import EmpresaSerializerToExcel


def get_data_rows_to_excel(id_list):
   data = list()
   queryset = Empresa.objects.prefetch_related('direccion_actividad').filter(pk__in=id_list)

   serialize = EmpresaSerializerToExcel(queryset, many=True)

   for odict in serialize.data:
      temp_list = list()

      for i in odict.values():
         if isinstance(i, list):
            i = ', '.join(txt for txt in i)

         temp_list.append(i)

      data.append(tuple(temp_list))
   
   return data


def create_excel_file(id_list):
   # Create a file-like buffer to receive Excel data.
   buffer = BytesIO()

   wb = xlwt.Workbook()
   ws = wb.add_sheet("Empresas")

   row_num = 0

   font_style = xlwt.XFStyle()
   font_style.font.bold = True

   # TODO Default `headers` for testing.
   # It's possible improve to dinamically headers set.
   columns = [
      "Nombre", 
      "Sector de Actividad",
      "Direccion de Actividad",
      "CIF",
      "Pyme", 
      "Dirección Fiscal", "Nombre: Persona de Contácto", 
      "Cargo: Persona de Contácto", 
      "Nro. Empleados Fijos",
      "Nro. Empleados Eventuales", 
      "Volumen de Facturación",
      "Frecuiencia de Exportación",
      "Exportación Relativa",
      "Destino de Exportacion"
   ]

   for col_num in range(len(columns)):
      ws.write(row_num, col_num, columns[col_num], font_style)

   font_style = xlwt.XFStyle()

   rows = get_data_rows_to_excel(id_list)

   for row in rows:
      row_num += 1
      for col_num in range(len(row)):
         ws.write(row_num, col_num, row[col_num], font_style)
   
   wb.save(buffer)
   buffer.seek(0)
   
   return buffer
   
def send_email_with_enterprise_info(email, file):
   destinatarios = list()
   destinatarios.append(email)
   try:
      message = Mail(
         from_email=settings.DEFAULT_FROM_EMAIL,
         to_emails=destinatarios,
         subject='Informacion de Empresas by: CLEX Project',
         html_content='<strong>and easy to do anywhere, even with Python</strong>'
      )

      file_data = file.read()
      encoded = base64.b64encode(file_data).decode()

      attach = Attachment()   
      attach.file_content = FileContent(encoded)
      attach.file_type = FileType("application/vnd.ms-excel")
      attach.file_name = FileName("test.xls")
      attach.disposition = Disposition('attachment')
      content_id = 'Content 1'
      attach.content_id = ContentId(content_id)

      message.attachment = attach
      sg = SendGridAPIClient(settings.EMAIL_HOST_PASSWORD)
      sg.send(message)
   except Exception as e:
      print(e)