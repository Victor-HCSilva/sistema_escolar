from .models import Turma, Aviso
from .forms import TurmaForm, AvisoForm
from django.shortcuts import render, get_object_or_404, redirect

def room(request):
    avisos = Aviso.objects.all()
    if request.method == "POST":
        form = AvisoForm(request.POST)
        if form.is_valid():
            print("Form salvo")
            form.save()
            return redirect("index")
        else:
            print("Erro no formulario:", form.errors)
    else:
        form = AvisoForm()
    context = {
        "form": form,
        "avisos": avisos,
    }
    return render(request, "room.html", context)

def turmas(request):
    if request.method == "POST":
        form = TurmaForm(request.POST)
        if form.is_valid():
            print("Form salvo")
            form.save()
            return redirect("index")
        else:
            pritn("Erros:", form.errors)
    else:
        form = TurmaForm()
        turmas = Turma.objects.all()
    context = {
        "form":form,
        "turmas":turmas,
    }
    return render(request, "turmas.html", context)
