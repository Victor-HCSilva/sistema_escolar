from django.db import models
from django.db.models import ForeignKey
from datetime import date
from django.utils import timezone

class Aluno(models.Model):
    matricula = models.IntegerField(default=000000)
    nome = models.CharField(max_length=250)
    telefone = models.CharField(max_length=14, default="000000000")
    rec = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    nota1 = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    nota2 = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    nota3 = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    nota4 = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    observacao = models.TextField(
        max_length=12000, default="Escreva alguma observação"
    )
    ano = models.CharField(max_length=100, choices=[
            ("1° ano", "1° ano"),
            ("2° ano", "2° ano"),
            ("3° ano", "3° ano"),
            ("4° ano", "4° ano"),
            ("5° ano", "5° ano"),
            ("6° ano", "6° ano"),
            ("7° ano", "7° ano"),
            ("8° ano", "8° ano"),
            ("9° ano", "9° ano"),
        ]
    )
    turma = models.CharField(
        max_length=250,
        choices=[
            ("Turma A", "Turma A"),
            ("Turma B", "Turma B"),
            ("Turma C", "Turma C"),
            ("Turma D", "Turma D"),
            ("Turma E", "Turma E"),
            ("Turma F", "Turma F"),
        ],
    )

    def __str__(self):
        return self.nome


class Avaliacao(models.Model):
    tipo = models.CharField(
        max_length=250,
        choices=[
            ("Trabalho em dupla", "Trabalho em dupla"),
            ("Trabalho com 4 comp.", "Trabalho com 4 comp."),
            ("Prova", "Prova"),
            ("Trabalho individual", "Trabalho individual"),
        ],
    )
    alunos = models.ManyToManyField(Aluno, through="NotaAvaliacao") # Relação muitos-para-muitos
    observacao = models.TextField(
        max_length=12000, default="Descreva sobre o desempenho dos componentes"
    )

class NotaAvaliacao(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    avaliacao = models.ForeignKey(Avaliacao, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)

    class Meta:
        unique_together = ('aluno', 'avaliacao')  # Garante que um aluno tenha apenas uma nota por avaliação

    def __str__(self):
        return self.nome

class Professor(models.Model):
    nome = models.CharField(max_length=250)
    senha = models.CharField(max_length=25)
    turma = models.ManyToManyField(Aluno)

    def __str__(self):
        return self.nome

class Anotacoes(models.Model):
    data = models.DateField(default=timezone.now())
    anotacao = models.CharField(max_length=10000, default="Escreva algo Hoje!")
    tipo = models.CharField(max_length=200, default="Sem tipo definido")
    importancia = models.IntegerField(default=1)
