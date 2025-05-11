from django.db import models
from app import models as md

class Turma(models.Model):
    aluno = models.ForeignKey(md.Aluno, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=8)
    numero = models.IntegerField()
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

    def __str__(self) -> str:
        return f"Sala numero: {self.numero}"

class Aviso(models.Model):
    #professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    aviso = models.CharField(max_length=50000)
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Aviso: {self.titulo} | Data de criação: {self.data}"
