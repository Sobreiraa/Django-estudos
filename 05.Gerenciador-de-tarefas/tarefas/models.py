from django.db import models

class Tarefa(models.Model):
    OPCOES_CATEGORIA = (
        ('urgente', 'Urgente'),
        ('importante', 'Importante'),
        ('precisa ser feito', 'Precisa ser feito'),
    )

    OPCOES_STATUS = (
        ('concluído', 'Concluído'),
        ('pendente', 'Pendente'),
        ('adiado', 'Adiado'),
    )

    descricao = models.CharField(max_length=400)
    data_criacao = models.DateTimeField(auto_now_add=True)
    categoria = models.CharField(max_length=30, choices=OPCOES_CATEGORIA, default='importante')
    status = models.CharField(max_length=30, choices=OPCOES_STATUS, default='pendente')


    def __str__(self) -> str:
        return self.descricao