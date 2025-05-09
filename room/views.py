from .models import Sala, Aviso
from .forms import SalaForm, AvisoForm
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
