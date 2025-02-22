from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .forms import AlunoForm, AvaliacaoForm
from .models import Aluno, Avaliacao
from django.contrib.auth.hashers import make_password

class Manager:
    def __init__(self, path:str, context: dict):
        self.context = context
        self.path = path

    def method_get(self, request):
        return render(request, self.path, self.context)

    def method_post(self, model_form, url_to_redirect, request):
        if request.method == "POST":
            form = model_form(request.POST)

            if form.is_valid():
                form.save()
                return redirect(url_to_redirect)

        else:
            form = model_form()

        self.context["form"] = form
        return render(request,self.path, self.context)

    def method_put(self, model_form, url_to_redirect, context, Model, id):
        instance = get_object_or_404(Model, id=id)

        if request == "POST":
            form = model_form(request.POST, instance=instance)

            if form.is_valid():
                form.save()
                redirect(url_to_redirect)

        else:
            form = model_form(instance=instance)

        context["form"] = form
        return render(request,self.path, context)

    def method_delete(self, model_form, url_to_redirect, Model, id):
        instance = get_object_or_404(Model, id=id)

        if request == "POST":
            form = model_form(request.POST, instance=instance)

            if form.is_valid():
                form.delete()
                redirect(url_to_redirect)

        else:
            form = model_form(instance=instance)

        self.context["form"] = form
        return render(request,self.path, context)
