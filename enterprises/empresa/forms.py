from django import forms

from .models import (
   Poblacion, Sector
)


ALPHABETIC_CHOICES = (
   ('---------', '---------'),
   ('a', 'A'),
   ('b', 'B'),
   ('c', 'C'),
)



class Filter(forms.Form):

   alpha = forms.ChoiceField(
      choices=ALPHABETIC_CHOICES,
      widget=forms.Select(
         attrs={
            'class': 'form-control'}))
   
   poblacion = forms.ModelChoiceField(
      queryset=Poblacion.objects.all(),
      widget=forms.Select(
         attrs={
            'class': 'form-control'}))
   
   sector = forms.ModelChoiceField(
      queryset=Sector.objects.all(),
      widget=forms.Select(
         attrs={
            'class': 'form-control'}))
   
