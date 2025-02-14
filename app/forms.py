from django import forms
from .models import Aluno, Avaliacao  # Importe os modelos corretamente

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome','ano','turma', 'telefone','nota1', 'nota2', 'nota3', 'nota4','rec', "observacao"] # Removi as notas daqui
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'ano':forms.Select(attrs={'class':'fom-control'}),
            'turma':forms.Select(attrs={'class':'fom-control'}),
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
            "ano":"Ano:",
            "turma":"Turma:",
            "telefone": "Telefone:",
            'rec': "Nota da Recuperação:",
            'nota1':"Nota 1:",
            'nota2':"Nota 2:",
            'nota3':"Nota 3:",
            'nota4':"Nota 4:",
            "observacao": "Observações:",
        }


class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ["tipo", "alunos"] # Use o ManyToManyField 'alunos'
        widgets = {
            "tipo": forms.Select(attrs={"class": "form-control"}),  # Use Select para o campo 'tipo'
            "alunos": forms.SelectMultiple(attrs={"class": "form-control"}), # Usar SelectMultiple para o ManyToManyField
        }
        labels = {
            "tipo": "Tipo de avaliação:",
            "alunos": "Selecione os Alunos:", #Label do campo manytomany
        }
