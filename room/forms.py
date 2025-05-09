from django import forms
from .models import Sala, Aviso

class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = "__all__"

class AvisoForm(forms.ModelForm):
    class Meta:
        model = Aviso
        fields = ["titulo", "aviso",]
        widgets = {
            "titulo": forms.TextInput(attrs={'class': 'form-control'}), # Adicionado 'forms.' e atributos
            "aviso": forms.Textarea(attrs={'class': 'form-control'}), # Adicionado 'forms.' e atributos
        }
