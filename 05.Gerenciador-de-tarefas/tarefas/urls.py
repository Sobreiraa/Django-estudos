from django.urls import path
from . import views

urlpatterns = [
    path('', views.tarefas_lista, name='tarefas_lista'),
]
