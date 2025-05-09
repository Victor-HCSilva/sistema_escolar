from django.db import models
from django.db.models import ForeignKey
from datetime import date
from django.utils import timezone

class Aluno(models.Model):
    #Depois criar senha aleaotia na hora de criar - > senha = models.CharField(max_length=30)
    matricula = models.IntegerField(default=000000, unique=True)
    nome = models.CharField(max_length=250)
    telefone = models.CharField(max_length=14, default="000000000")
    rec = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    nota1 = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    nota2 = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    nota3 = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    nota4 = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
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


    def __str__(self):
        return f"Nome: {self.nome} - {self.turma}"

class Presenca(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='presencas')
    data = models.DateField()

    def __str__(self):
        return f"{self.aluno.nome} em {self.data}"


class Professor(models.Model):
    nome = models.CharField(max_length=250)
    is_admin = models.BooleanField(default=False)
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
