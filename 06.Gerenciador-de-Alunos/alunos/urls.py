from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.visualizar_aluno, name='visualizar_aluno'),
    path('adicionar_aluno/', views.adicionar_aluno, name='adicionar_aluno'),
    path('editar_aluno/<int:id>/', views.editar_aluno, name='editar_aluno'),
    path('deletar_aluno/<int:id>/', views.deletar_aluno, name='deletar_aluno')
]
