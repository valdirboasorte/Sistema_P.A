from django.db import models
from user.models import Aluno

class Agenda(models.Model):
    STATUS_CHOICES = [
        ('ES', 'Espera'),
        ('AC', 'Aceito'),
        ('CA', 'Cancelado'),
        ('RE', 'Realizado'),
    ]

    dia = models.DateTimeField()
    descricao = models.TextField()
    local = models.CharField(max_length=50)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='ES'
    )

    turma = models.ForeignKey('turma.Turma', on_delete=models.CASCADE, null=True, blank=True)
    autor = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='agendamentos')

    def __str__(self):
        return f"{self.dia} - {self.status}"