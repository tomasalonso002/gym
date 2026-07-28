from django import forms
from .models import CargaHoraria, SueldoHora
from django.contrib.auth.forms import UserCreationForm

class CargaHorariaForm(forms.ModelForm):
    class Meta:
        model = CargaHoraria
        fields = ['cantidad']


class SueldoHoraForm(forms.ModelForm):
    class Meta:
        model = SueldoHora
        fields = ['valor']


