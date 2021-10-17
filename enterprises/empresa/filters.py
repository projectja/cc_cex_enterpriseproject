import django_filters
from django import forms


from .models import (
   Poblacion, Sector, Empresa
)



class EmpresaFilter(django_filters.FilterSet):

   nombre = django_filters.CharFilter(
      lookup_expr='icontains', 
      widget=forms.TextInput(
         attrs={
            'class': 'form-control form-control-navbar',
            'placeholder': 'Search...',
            }))

   poblacion = django_filters.ModelChoiceFilter(
      queryset=Poblacion.objects.all(), 
      widget=forms.Select(
         attrs={
            'class': 'form-control'}))

   sector = django_filters.ModelChoiceFilter(
      queryset=Sector.objects.all(), 
      widget=forms.Select(
         attrs={
            'class': 'form-control'}))


   class Meta:
      model = Empresa
      fields = [
         'nombre', 'poblacion',
         'sector']