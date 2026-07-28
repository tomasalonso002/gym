from django import forms

from .models import Noticias



class NoticiasForm(forms.ModelForm):
    class Meta:
        model = Noticias
        fields = ['titulo', 'contenido', 'archivo']