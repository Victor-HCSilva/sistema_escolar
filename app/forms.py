from django import forms
from .models import Aluno, Presenca, Professor

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = "__all__"

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = "__all__"

class PresencaForm(forms.ModelForm):
     class Meta:
        model = Presenca
        fields = ["data"]
        widgets = {
                "data": forms.DateInput( attrs={"type":"date",'class': 'datepicker'}),
        }

#for i in Presenca.objects.all():

#sprint(i)
