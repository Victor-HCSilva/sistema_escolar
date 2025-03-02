from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .forms import AlunoForm, AvaliacaoForm
from .models import Aluno, Avaliacao
from django.contrib.auth.hashers import make_password
from .functions_manager import Manager


def home(request):
    h = Manager(path="index.html",context={})
    return h.method_get(request)


def cadastro(request):
    c = Manager(path="cadastro.html", context={})
    return c.method_post(model_form=AlunoForm,
                  url_to_redirect="list",
                request=request)

def list(request):
    alunos = Aluno.objects.all()
    q_alunos = len(alunos)

    context = {
	    "alunos":alunos,
	    "quantidade":q_alunos,
	}

    l = Manager(path="list.html", context=context)

    return l.method_get(request)

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

def registrar_presenca(request, turma_id):
    turma = get_object_or_404(Turma, pk=turma_id)
    alunos = turma.aluno_set.all()  # Obtém todos os alunos da turma

    if request.method == 'POST':
        # Processar múltiplas presenças
        for aluno in alunos:
            aluno_id = aluno.id
            presente = request.POST.get(f'presente_{aluno_id}') == 'on'  # Verifica se a checkbox está marcada
            data = request.POST.get('data')
            observacoes = request.POST.get(f'observacoes_{aluno_id}', '') # Pega a observação específica do aluno

            try:
                presenca, created = Presenca.objects.update_or_create(
                    aluno_id=aluno_id,
                    data=data,
                    defaults={'presente': presente, 'observacoes': observacoes}
                )
            except Exception as e:
                messages.error(request, f"Erro ao salvar presença para {aluno.nome}: {e}")
                return redirect('registrar_presenca', turma_id=turma_id) # Redireciona de volta com erro

        messages.success(request, "Presenças registradas com sucesso!")
        return redirect('list') # Redireciona para a listagem

    else:
        # Exibir o formulário para cada aluno
        form = PresencaForm()  # Instância vazia do formulário

        context = {
            'turma': turma,
            'alunos': alunos,
            'form': form,  # Passa o formulário para o template
        }
        return render(request, 'registrar_presenca.html', context)

def teste(request):
    return render(request,'teste.html')

def anotacoes(request):
    return render(request,"anotacoes.html")
