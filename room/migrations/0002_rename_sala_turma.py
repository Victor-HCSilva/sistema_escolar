# Generated by Django 5.1.6 on 2025-05-10 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_delete_aviso_remove_aluno_ano_remove_aluno_turma"),
        ("room", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Sala",
            new_name="Turma",
        ),
    ]
