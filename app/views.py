from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .forms import AlunoForm, AvaliacaoForm
from .models import Aluno, Avaliacao
from django.contrib.auth.hashers import make_password

def home(request):
	return render(request, "index.html")


#cadastro sem senha
def cadastro(request):
    if request.method == "POST":
        form = AlunoForm(request.POST)

        if form.is_valid():
            print("Formulário válido")
            form.save() # Salva o objeto aluno
            return redirect("list") # Redireciona para a lista de alunos

    else:
        form = AlunoForm()

    context = {
        "form": form,
    }
    return render(request, "cadastro.html", context)

def list(request):
	alunos = Aluno.objects.all()
	q_alunos = len(alunos)

	context = {
	"alunos":alunos,
	"quantidade":q_alunos,
	}
	return render(request, "list.html", context)

def edit(request, id_aluno):
    aluno = get_object_or_404(Aluno, id=id_aluno)
    if request.method == "POST":
        form = AlunoForm(request.POST, instance=aluno) # Passe os dados e a instância
        if form.is_valid():
            print("Formulário válido")
            # Atualize os campos do aluno com os dados do formulário (já validados)
            aluno = form.save(commit=False) # Não salva ainda.

            # Hash a senha se ela foi alterada.  Importante!
            senha = form.cleaned_data.get("senha") # Obtém a senha do formulário
            if senha: # Se a senha foi alterada
                aluno.senha = make_password(senha) # Hash a nova senha

            aluno.save() # Salva o objeto aluno
            return redirect("list") # Redireciona para a lista de alunos
        else:
            print("Formulário inválido")
            # Imprima os erros do formulário no console (para depuração)
            print(form.errors)
            # Lidar com os erros do formulário.  Mostre os erros no template!
            context = {
                "form": form,
                "aluno": aluno,
            }
            return render(request, "edit.html", context)

    else: # Se não for POST (GET request)
        form = AlunoForm(instance=aluno)

    context = {
        "form": form,
        "aluno": aluno,
    }
    return render(request, "edit.html", context)

def delete(request, id_aluno):
	aluno = get_object_or_404(Aluno, id=id_aluno)

	if request.method == "POST":
		aluno.delete()
		return redirect("list")

	context = {
	"aluno":aluno,
	}
	return render(request, "delete.html", context)


def avalicao(request):
    form  = AvaliacaoForm()
    avaliacoes = Avaliacao.objects.all()

    if request.method == "POST":
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            print("Fomulario válido - POST")
            form.save()
        else:
            print("Formulário inválido:\n",form.errors)
    else:
        form = AvaliacaoForm()
    context = {
        "form":form,
        "avaliacaoes":avaliacoes,
        }
    return render(request, "avaliacoes.html", context)

def teste(request):
    return render(request,'teste.html')

def anotacoes(request):
    return render(request,"anotacoes.html")
