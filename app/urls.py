from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="index"),#get
    path("list/", views.list, name="list"),#get
    path("list_professor/", views.list_professor, name="list_professor"),#get
    path("cadastro/", views.cadastro, name="cadastro"),#post
    path("cadastro_professor/", views.cadastro_professor, name="cadastro_professor"),#post
    path("edit/<int:id_aluno>", views.edit, name="edit"),#post
    path("edit_professor/<int:id_professor>", views.edit_professor, name="edit_professor"),#post
    path("delete/<int:id_aluno>", views.delete, name="delete"),#delete
    path("delete_professor/<int:id_professor>", views.delete_professor, name="delete_professor"),#delete
    path("teste/", views.teste, name="teste"),#delete
    path("anotacoes/", views.anotacoes, name="abotacoes"),#GET
    path("registrar_presenca/<int:id_aluno>", views.registrar_presenca, name="registrar_presenca")
]
