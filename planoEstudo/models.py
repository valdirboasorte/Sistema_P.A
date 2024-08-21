from django.db import models
from user.models import Orientador
from agenda.models import Agenda

class PlanoDeEstudo(models.Model):
    descricao = models.TextField()
    autor = models.ForeignKey(Orientador, on_delete=models.CASCADE, related_name='autor')
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE, related_name='planos_de_estudo')