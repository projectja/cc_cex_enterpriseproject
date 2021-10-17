from django.contrib import admin

from .models import (
   Poblacion, Sector, Empresa
)


admin.site.register(Poblacion)
admin.site.register(Sector)
admin.site.register(Empresa)
