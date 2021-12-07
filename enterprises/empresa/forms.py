from django import forms
from django_countries import countries
from django_countries.widgets import CountrySelectWidget


from .models import (
   Municipio, Empresa, Solicitud
)


from .constants import (
   PRODUCTOS_SERVICIOS,
   EMP_FIJOS, EMP_EVENT, 
   VOL_FACT, FREQ_EXPORT,
)

DIRECCION_ACTIVIDAD_CHOICES = ()
EXPORT_DESTINO_CHOICES = ()

try:
   for pk, name in Municipio.objects.values_list('id', 'nombre'):
         municipio = (pk, name,)
         DIRECCION_ACTIVIDAD_CHOICES += (municipio,)


   for code, name in list(countries):
         country = (code, name,)
         EXPORT_DESTINO_CHOICES += (country,)
except Exception as e:
   print(e)
   pass




class Filter(forms.ModelForm):
   
   # SECTOR Y PRODUCTOS
   sector_actividad = forms.ChoiceField(
      choices=PRODUCTOS_SERVICIOS, 
      required=False,
      widget=forms.Select(
         attrs={
            'class': 'form-control mb-3 form-filter-input'}))
   
   query = forms.CharField(
      widget=forms.TextInput(
         attrs={
            'class': 'form-control',
            'placeholder': 'Buscar',
            'autocomplete': 'off'}))
   
   direccion_actividad = forms.ChoiceField(
      choices=DIRECCION_ACTIVIDAD_CHOICES, 
      required=False,
      widget=forms.Select(
         attrs={
            'class': 'form-control mb-3 form-filter-input select2',
            'multiple': 'multiple'}))


   # DIMENSION
   empleados_fijos = forms.ChoiceField(
      choices=EMP_FIJOS,
      widget=forms.RadioSelect)

   empleados_eventuales = forms.ChoiceField(
      choices=EMP_EVENT,
      widget=forms.RadioSelect(
         attrs={
            'class': 'form-group form-filter-input mb-3'}))

   volumen_facturacion = forms.ChoiceField(
      choices=VOL_FACT,
      widget=forms.RadioSelect(
         attrs={
            'class': 'form-group form-filter-input mb-3'}))


   # PERFIL EXPORTADOR
   export_frecuencia = forms.ChoiceField(
      choices=FREQ_EXPORT,
      widget=forms.RadioSelect(
         attrs={
            'class': 'form-group form-filter-input mb-3'}))

   export_relativa = forms.IntegerField(
      widget=forms.NumberInput(
         attrs=
         {'class': 'form-control form-filter-input mb-3', 'min':'0', 'max': '100'}))

   export_destino = forms.ChoiceField(
      choices=EXPORT_DESTINO_CHOICES, 
      required=False,
      widget=forms.Select(
         attrs={
            'class': 'form-control mb-3 form-filter-input select2',
            'multiple': 'multiple'}))
   
   class Meta:
      model = Empresa
      fields = (
         'sector_actividad', 'direccion_actividad',
         'empleados_fijos', 'empleados_eventuales',
         'volumen_facturacion', 'export_relativa',
         'export_destino', 'export_frecuencia',
      )


class RequestEmpresaForm(forms.ModelForm):

   class Meta:
      model = Solicitud
      fields = (
         'request_email',
         'request_f_name',
         'request_l_name',
      )