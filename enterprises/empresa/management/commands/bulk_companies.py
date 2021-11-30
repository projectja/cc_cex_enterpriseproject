# Modulo que genera registros de empresas,
# los registros estan asociados a los campos del
# modelo `Empresa`. Cada campo generado es un valor
# aleatorio en base a documentos en el equipo del usuario
# que ejecute el comando.
#
# El script genera Nombres de empresa de forma aleatoria,
# descripcion de empresas de forma aleatoria, y pais de origen
# y pais de operacion de forma aleatoria.
import random
import string
from django.core.management.base import BaseCommand

from empresa.models import (
   Empresa, Product,
   Municipio, Marca,
   Countries
   
)

from empresa.constants import (
   PRODUCTOS_SERVICIOS, EMP_FIJOS,
   EMP_EVENT, VOL_FACT, FREQ_EXPORT
)

PHONE_EMPRESA = "+582832410525"
PHONE_TEST = "+584143722004"
CARGO = "Software Developer"
EMAIL_EMPRESA = "test@email.com"
PERSONA_CONTACT = "David Tester"
DIRECCION_FISCAL = "221b Baker Street"

PATH_TEST = r"C:\Users\Familia Navas\Desktop\Dave's Files\Practicas_programacion\Dummy names for random factory\test_names.txt"

LISTA_PRODUCTOS_SERVICIOS_OPTIONS = [ps[0] for ps in PRODUCTOS_SERVICIOS]
LISTA_EMPLEADOS_FIJOS_OPTIONS = [ef[0] for ef in EMP_FIJOS]
LISTA_EMPLEADOS_EVENTUALES_OPTIONS = [ee[0] for ee in EMP_EVENT]
LISTA_VOLUMEN_FACTURADO_OPTIONS = [vf[0] for vf in VOL_FACT]
LISTA_FRECUENCIA_EXPORTACION_OPTIONS = [fe[0] for fe in FREQ_EXPORT]

LISTA_PORCENTAJES = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# LISTA_DIRECCION_ACTIVIDAD_OPTIONS = list(Municipio.objects.all())
# LISTA_PRODUCTOS_SERVICIOS = list(Product.objects.all())
# LISTA_COUNTRIES_EXPORTACION_DESTINO = list(Countries.objects.all())


def get_random_productos_servicios():
   return random.choice(LISTA_PRODUCTOS_SERVICIOS_OPTIONS)

def get_random_empleados_fijos():
   return random.choice(LISTA_EMPLEADOS_FIJOS_OPTIONS)

def get_random_empleados_eventuales():
   return random.choice(LISTA_EMPLEADOS_EVENTUALES_OPTIONS)

def get_random_volumen_facturado():
   return random.choice(LISTA_VOLUMEN_FACTURADO_OPTIONS)

def get_random_frecuencia_exportacion():
   return random.choice(LISTA_FRECUENCIA_EXPORTACION_OPTIONS)

def get_random_export_relativa():
   return random.choice(LISTA_PORCENTAJES)

def get_random_volumen_exportacion():
   return random.choice(LISTA_PORCENTAJES)

def get_random_cif():
   r_cif = ''
   return '{}'.format(r_cif.join(random.choices(string.digits, k=9)))

def get_is_pyme():
   options = [0, 1]
   return random.choice(options)

# def get_random_direccion_actividad():
#    return random.sample(LISTA_DIRECCION_ACTIVIDAD_OPTIONS, 4)

# def get_random_countries_exportacion_destino():
#    return random.sample(LISTA_COUNTRIES_EXPORTACION_DESTINO, 4)

# def get_random_productos():
#    return random.sample(LISTA_PRODUCTOS_SERVICIOS, 4)


def save_company_data(name):
   model_fields = {
      'sector_actividad': get_random_productos_servicios(),
      'name': name,
      'cif': get_random_cif(),
      'pyme': get_is_pyme(),
      'direccion_fiscal': DIRECCION_FISCAL,
      'phone_empresa': PHONE_EMPRESA,
      'email_empresa': EMAIL_EMPRESA,
      'nombre_persona_contacto': PERSONA_CONTACT,
      'cargo_persona_contacto': CARGO,
      'email_persona_contacto': EMAIL_EMPRESA,
      'phone_persona_contacto': PHONE_TEST,
      'empleados_fijos': get_random_empleados_fijos(),
      'empleados_eventuales': get_random_empleados_eventuales(),
      'volumen_facturacion': get_random_volumen_facturado(),
      'export_frecuencia': get_random_frecuencia_exportacion(),
      'export_relativa': get_random_export_relativa(),
      'export_vol': get_random_volumen_exportacion(),
   }
   
   empresa = Empresa(**model_fields)
   empresa.save()

class Command(BaseCommand):

   def handle(self, *args, **kwargs):
      with open(PATH_TEST, 'r') as company_names:
         turns = 3
         laps = 0
         iterator = 0

         company_names_list = list(company_names)

         while laps < turns:
            try:
               name = company_names_list[iterator]
            
               if laps == 1:
                  if ' ' in name:
                     splited_name = name.split()
                     company_name = random.choice(splited_name)

                  else:
                     company_name = name
                     ramdom_name_bucket = name

                  save_company_data(company_name)

               elif laps == 2:
                  if ' ' in name:
                     splited_name = name.split()
                     name1 = random.choice(splited_name)
                     name2 = random.choice(splited_name)
                     company_name = name1 + ' '+ name2

                  else:
                     company_name = name + ' ' + ramdom_name_bucket          
                     ramdom_name_bucket = name
                  
                  save_company_data(company_name)

            except IndexError:
               iterator = 0
               laps += 1
               continue

            iterator += 1

      print("Done!")
