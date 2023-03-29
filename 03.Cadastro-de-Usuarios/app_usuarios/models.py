from django.db import models

# Create your models here.
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=55)
    sobrenome = models.CharField(max_length=55)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=9)