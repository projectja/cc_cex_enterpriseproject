from django.contrib import admin

from .models import (
   Empresa, Marca, Product, 
   Municipio, Provincia
)



admin.site.register(Empresa)
admin.site.register(Marca)
admin.site.register(Product)
admin.site.register(Provincia)
admin.site.register(Municipio)
