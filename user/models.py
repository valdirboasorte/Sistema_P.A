from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('ALU', 'Aluno'),
        ('ORI', 'Orientador'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11, unique=True )

class Aluno(User):
    matricula = models.CharField(max_length=20, unique=True)
    turma = models.ForeignKey('turma.Turma', on_delete=models.CASCADE, null=True, blank=True)

class Orientador(User):
    contato = models.CharField(max_length=100)
