# Generated by Django 5.1.6 on 2025-05-09 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_professor_is_admin"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="aviso",
            name="professor",
        ),
    ]
