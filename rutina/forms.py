from django import forms
from .models import Rutina,RutinaPersonalizada

class RutinaForm(forms.ModelForm):
    class Meta:
        model = Rutina
        fields = ['nombre', 'archivo']

class RutinaPersonalizadaForm(forms.ModelForm):
    class Meta:
        model = RutinaPersonalizada
        fields = ['nombre', 'archivo']