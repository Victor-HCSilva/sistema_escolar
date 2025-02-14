from django.urls import path
from . import views

urlpatterns = [
	path("", views.home, name="index"),#get
	path("list/", views.list, name="list"),#get
	path("cadastro/", views.cadastro, name="cadastro"),#post
	path("edit/<int:id_aluno>", views.edit, name="edit"),#post
	path("delete/<int:id_aluno>", views.delete, name="delete"),#delete
	path("teste/", views.teste, name="teste"),#delete
    path("avaliacao/", views.avalicao, name="avaliacao"),#delete
    
]
