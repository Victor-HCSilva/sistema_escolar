from django import forms
from .models import Turma, Aviso

class TurmaForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = "__all__"

class AvisoForm(forms.ModelForm):
    class Meta:
        model = Aviso
        fields = ["titulo", "aviso",]
        widgets = {
            "titulo": forms.TextInput(attrs={'class': 'form-control'}), # Adicionado 'forms.' e atributos
            "aviso": forms.Textarea(attrs={'class': 'form-control'}), # Adicionado 'forms.' e atributos
        }
