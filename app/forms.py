from django import forms
from .models import Aluno, Presenca

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = "__all__"                
        
class PresencaForm(forms.ModelForm):
     class Meta:
        model = Presenca 
        fields = ["data"]
        widgets = {
                "data": forms.DateInput( attrs={"type":"date",'class': 'datepicker'}),  
        }

