from django.urls import path
from . import views

urlpatterns = [
    path('', views.todas_tarefas, name='todas_tarefas'),
    path('pendentes/', views.tarefas_pendentes, name='tarefas_pendentes'),
    path('concluidas/', views.tarefas_concluidas, name='tarefas_concluidas'),
    path('adiadas/', views.tarefas_adiadas, name='tarefas_adiadas'),
    path('concluir/<int:tarefa_id>/', views.concluir_tarefa, name='concluir_tarefa'),
    path('excluir/<int:tarefa_id>/', views.excluir_tarefa, name='excluir_tarefa'),
    path('adiar/<int:tarefa_id>/', views.adiar_tarefa, name='adiar_tarefa'),
    path('editar/<int:tarefa_id>/', views.editar_tarefa, name='editar_tarefa' ),
    path('mover-para-lista-de-tarefas/<int:tarefa_id>/', views.mover_para_tarefas, name='mover_para_tarefas')
]
