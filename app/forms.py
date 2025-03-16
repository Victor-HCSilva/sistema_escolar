from django import forms
from .models import Aluno, Presenca, Aviso

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

class AvisoForm(forms.ModelForm):
    class Meta:
        model = Aviso
        fields = ["titulo", "aviso",]
        widgets = {
            "titulo": forms.TextInput(attrs={'class': 'form-control'}), # Adicionado 'forms.' e atributos
            "aviso": forms.Textarea(attrs={'class': 'form-control'}), # Adicionado 'forms.' e atributos
        }


#for i in Presenca.objects.all():

#sprint(i)
