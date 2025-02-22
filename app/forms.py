from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = "__all__"
"""        model = Aluno
        fields = ['nome', 'ano', 'turma', 'telefone', 'nota1', 'nota2', 'nota3', 'nota4', 'rec', "observacao"]
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'ano': forms.Select(attrs={'class': 'form-control'}),
            'turma': forms.Select(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'nota1': forms.NumberInput(attrs={'class': 'form-control'}),
            'nota2': forms.NumberInput(attrs={'class': 'form-control'}),
            'nota3': forms.NumberInput(attrs={'class': 'form-control'}),
            'nota4': forms.NumberInput(attrs={'class': 'form-control'}),
            'rec': forms.NumberInput(attrs={'class': 'form-control'}),
            'observacao': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'nome': "Nome:",
            "ano": "Ano:",
            "turma": "Turma:",
            "telefone": "Telefone:",
            'rec': "Nota da Recuperação:",
            'nota1': "Nota 1:",
            'nota2': "Nota 2:",
            'nota3': "Nota 3:",
            'nota4': "Nota 4:",
            "observacao": "Observações:",
        }
"""
from django import forms
from django.forms import inlineformset_factory
from .models import Avaliacao, NotaAvaliacao

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['tipo', 'observacao']
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'observacao': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'tipo': "Tipo de Avaliação:",
            'observacao': "Observações sobre a avaliação:",
        }


class NotaAvaliacaoForm(forms.ModelForm):
    class Meta:
        model = NotaAvaliacao
        fields = ['aluno', 'nota']
        widgets = {
            'aluno': forms.Select(attrs={'class': 'form-control'}),
            'nota': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'aluno': "Aluno:",
            'nota': "Nota:",
        }

#Cria um formset para adicionar várias notas de avaliação a uma avaliação.
NotaAvaliacaoFormSet = inlineformset_factory(Avaliacao, NotaAvaliacao, form=NotaAvaliacaoForm, extra=1, can_delete=True)
