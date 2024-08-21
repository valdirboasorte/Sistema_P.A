from django.db import models
from user.models import Aluno
from planoEstudo.models import PlanoDeEstudo

class Comentario(models.Model):
    autor = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='autor')
    texto = models.TextField()
    plano_de_estudo = models.ForeignKey(PlanoDeEstudo, on_delete=models.CASCADE, related_name='comentarios')