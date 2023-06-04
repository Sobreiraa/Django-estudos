from django.db import models

# Create your models here.
class Aluno(models.Model):
    matricula = models.PositiveIntegerField()
    nome = models.CharField(max_length=55)
    sobrenome = models.CharField(max_length=55)
    email = models.EmailField(max_length=100)
    materia = models.CharField(max_length=55)
    media_nota = models.FloatField()

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
