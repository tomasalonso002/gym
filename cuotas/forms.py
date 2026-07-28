from django import forms
from .models import Pago, Plan

class PlanForm(forms.ModelForm):
    class Meta:
        model= Plan
        fields = ['nombre','dias_por_semana','precio']


class PagoForm(forms.ModelForm):
    class Meta:
        model= Pago
        fields = ['comprobante']