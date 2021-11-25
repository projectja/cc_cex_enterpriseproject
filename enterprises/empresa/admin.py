from django.contrib import admin

from .models import (
   Empresa, Countries,
   Marca, Product, Municipio,
   Provincia
)



admin.site.register(Empresa)
admin.site.register(Countries)
admin.site.register(Marca)
admin.site.register(Product)
admin.site.register(Provincia)
admin.site.register(Municipio)
