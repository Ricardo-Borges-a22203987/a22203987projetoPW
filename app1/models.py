from django.db import models

class Aluno(models.Model):
    ANO_CHOICES = [
        (1, '1º ano'),
        (2, '2º ano'),
        (3, '3º ano'),
    ]
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    ano = models.IntegerField(choices=ANO_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.nome
