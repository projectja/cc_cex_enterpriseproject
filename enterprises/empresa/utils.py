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
      "Nombre", "Sector de Actividad", "CIF", 
      "Direccion Fiscal", "Nombre: Persona de Contecto", 
      "Cargo: Persona de Contacto", "Nro. Empleados Fijos", 
      "Volumen de Facturacion"
   ]

   for col_num in range(len(columns)):
      ws.write(row_num, col_num, columns[col_num], font_style)

   font_style = xlwt.XFStyle()

   # TODO Default `args_list`
   # It's possible improve to dinamically args list.
   args_list = [
      "name", "sector_actividad", "cif", 
      "direccion_fiscal", "nombre_persona_contacto", 
      "cargo_persona_contacto", "empleados_fijos",
      "volumen_facturacion"
   ]
   

   rows = Empresa.objects.get_data_rows(id_list, *args_list)

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