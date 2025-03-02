from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .forms import AlunoForm, AvaliacaoForm
from .models import Aluno, Avaliacao
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect, get_object_or_404
import logging

# Configura o logger (você pode ajustar o nível e o formato)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class Manager:
    def __init__(self, path: str, context: dict):
        self.context = context
        self.path = path

    def method_get(self, request):
        return render(request, self.path, self.context)

    def method_post(self, model_form, url_to_redirect, request):
        if request.method == "POST":
            logger.debug("Requisição POST recebida em method_post")  # Depuração
            logger.debug(f"Dados POST: {request.POST}")
            form = model_form(request.POST)

            if form.is_valid():
                logger.debug("Formulário válido em method_post")  # Depuração
                form.save()
                return redirect(url_to_redirect)
            else:
                logger.warning("Formulário inválido em method_post")  # Depuração
                logger.warning(f"Erros do formulário: {form.errors}")
                self.context["form"] = form
                return render(request, self.path, self.context)

        else:
            logger.debug("Requisição GET recebida em method_post")  # Depuração
            form = model_form()

        self.context["form"] = form
        return render(request, self.path, self.context)

    def method_put(self, request, model_form, url_to_redirect, Model, id):
        instance = get_object_or_404(Model, id=id)
        logger.debug(f"Instância encontrada: {instance}")  # Depuração

        if request.method == "POST":
            logger.debug("Requisição POST recebida em method_put")  # Depuração
            logger.debug(f"Dados POST: {request.POST}")  # Depuração

            form = model_form(request.POST, instance=instance)  # Passa a instância

            if form.is_valid():
                logger.debug("Formulário válido em method_put")  # Depuração
                logger.debug(f"Dados antes do save: {instance.__dict__}")
                form.save()  # Atualiza a instância existente
                logger.debug(f"Dados depois do save: {instance.__dict__}")

                return redirect(url_to_redirect)
            else:
                logger.warning("Formulário inválido em method_put")  # Depuração
                logger.warning(f"Erros do formulário: {form.errors}")  # Depuração
                self.context["form"] = form
                return render(request, self.path, self.context)

        else:
            logger.debug("Requisição GET recebida em method_put (exibindo formulário)")  # Depuração
            form = model_form(instance=instance)

        self.context["form"] = form
        return render(request, self.path, self.context)

    def method_delete(self,request, model_form, url_to_redirect, Model, id):
        instance = get_object_or_404(Model, id=id)

        print("Aluno com este nome será excluido:",instance.nome)

        if request.method == "POST":
            print("Excluido")
            instance.delete()
            return redirect(url_to_redirect)     
             
        return render(request,self.path, self.context)
        
