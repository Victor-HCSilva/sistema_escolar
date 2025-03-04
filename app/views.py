from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .forms import AlunoForm, PresencaForm
from .models import Aluno
from django.contrib.auth.hashers import make_password
from .functions_manager import Manager

def home(request):
    h = Manager(path="index.html",context={})
    return h.method_get(request)

def cadastro(request):
    if request.method == "POST":
        alunoForm = AlunoForm(request.POST)    

        if alunoForm.is_valid() :
            alunoForm.save()
            return redirect("list")
        else:
            print("Erro no formluario:",alunoForm.errors)

    else:
        alunoForm = AlunoForm()    

    context = {
     "alunoForm":AlunoForm,
     }
        
    return render(request, "cadastro.html", context)

def list(request):
    alunos = Aluno.objects.all()

    return render(request, "list.html", {"alunos":alunos})


def edit(request, id_aluno):
    e = Manager(path="edit.html",context={})

    return e.method_put(
            request=request,
            model_form=AlunoForm,
            url_to_redirect="list",
            Model=Aluno,
            id=id_aluno,)

def delete(request, id_aluno):
    d = Manager(path="delete.html", context={})

    return d.method_delete(request=request,
                           model_form=AlunoForm,
                           url_to_redirect="list",
                           Model=Aluno, 
                           id=id_aluno)


from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import Aluno, Presenca  # Importe Presenca
from .forms import PresencaForm

def registrar_presenca(request, id_aluno):
    aluno = get_object_or_404(Aluno, id=id_aluno)
    form = PresencaForm() # Não precisa de instance ao inicializar, pois estamos criando um novo objeto

    if request.method == 'POST':
        form = PresencaForm(request.POST)
        if form.is_valid():
            presenca = form.save(commit=False)  # Cria o objeto Presenca mas não salva ainda
            presenca.aluno = aluno  # Define o aluno para a presença
            presenca.save()  # Salva a presença no banco de dados

            data = presenca.data  # Pega a data da presença
            messages.success(request, f"Presença registrada para {aluno.nome} em {data}")
            return redirect('list')  # Adapte o redirect para onde você quer ir
        else:
            print("Erros:", form.errors)

    else:
        context = {
            'form': form,
            'aluno': aluno,
        }
        return render(request, 'registrar_presenca.html', context)

def teste(request):
    return render(request,'teste.html')

def anotacoes(request):
    return render(request,"anotacoes.html")
