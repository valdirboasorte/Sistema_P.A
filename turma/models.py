from django.db import models

class Turma(models.Model):
    nome = models.CharField(max_length=50)
    autor = models.ForeignKey('user.Orientador', verbose_name=("Autor da turma"), on_delete=models.CASCADE)

    def __str__(self):
        return self.nome