from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .forms import AlunoForm, PresencaForm, AvisoForm, ProfessorForm
from .models import Aluno, Presenca, Aviso, Professor
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

def registrar_presenca(request, id_aluno): 
    aluno = get_object_or_404(Aluno, pk=id_aluno)
    presencas = Presenca.objects.filter(aluno=aluno)
    nome_aluno = aluno.nome.title() 
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
        context ={
            'form': form,
            'aluno': aluno,
            "presencas":presencas,
            'nome':nome_aluno,
        }
        return render(request, 'registrar_presenca.html', context)

def room(request):
    if request.method == "GET":
        form = AvisoForm()
        avisos = Aviso.objects.all()
        return render(request, "room.html", {"form":form, "avisos":avisos})
    elif request.method == "POST":
        form = AvisoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("room")
        else:
            print("Erros nno formulario:",form.errors)

def teste(request):
    return render(request,'teste.html')

def anotacoes(request):
    return render(request,"anotacoes.html")


def cadastro_professor(request):
    if request.method == "POST":
        form = ProfessorForm(request.POST)    
        if form.is_valid() :
            form.save()
            return redirect("list_professor")
        else:
            print("Erro no formluario:",form.errors)
    else:
        form = ProfessorForm(request.POST)    
    context = {
        "form":form,
     }
    return render(request, "cadastro_professor.html", context)

def edit_professor(request, id_professor):
    e = Manager(path="edit_professor.html",context={})
    return e.method_put(
            request=request,
            model_form=ProfessorForm,
            url_to_redirect="list",
            Model=Professor,
            id=id_professor,)


def list_professor(request):
    professor = Professor.objects.all()
    return render(request, "list_professor.html", {"professor":professor})

def delete_professor(request, id_professor):
    d = Manager(path="delete_professor.html", context={})
    return d.method_delete(request=request,
                           model_form=ProfessorForm,
                           url_to_redirect="list_professor",
                           Model=Professor, 
                           id=id_professor)


