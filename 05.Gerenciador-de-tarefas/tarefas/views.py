from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa
from .forms import AdicionarTarefa, EditarTarefaForm

def todas_tarefas(request):
    todas_tarefas = Tarefa.objects.all()
    return render(request, 'tarefas/todas_tarefas.html', {'todas_tarefas': todas_tarefas})


def tarefas_pendentes(request):
    tarefas_pendentes = Tarefa.objects.filter(status='pendente')
    if request.method == "POST":
        form = AdicionarTarefa(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('tarefas_pendentes')
    else:
        form = AdicionarTarefa()
    return render(request, 'tarefas/tarefas_pendentes.html', {'tarefas_pendentes': tarefas_pendentes, 
                                                              'form': form})


def tarefas_concluidas(request):
    tarefas_concluidas = Tarefa.objects.filter(status='concluído')
    return render(request, 'tarefas/tarefas_concluidas.html', {'tarefas_concluidas': tarefas_concluidas})


def tarefas_adiadas(request):
    tarefas_adiadas = Tarefa.objects.filter(status='adiado')
    return render(request, 'tarefas/tarefas_adiadas.html', {'tarefas_adiadas': tarefas_adiadas})


def concluir_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    tarefa.status = 'concluído'
    tarefa.save()
    return redirect('tarefas_pendentes')


def adiar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    tarefa.status = 'adiado'
    tarefa.save()
    return redirect('tarefas_pendentes')


def excluir_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    tarefa.delete()
    return redirect('tarefas_pendentes')


def editar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    if request.method == "POST":
        form = EditarTarefaForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            tarefa.descricao = cd['tarefa']
            tarefa.categoria = cd['categoria']
            tarefa.save()
            return redirect('tarefas_pendentes')
    else:
        form = EditarTarefaForm(initial={'descricao':tarefa.descricao, 'categoria': tarefa.categoria})
    return render(request, 'tarefas/editar_tarefa.html', {'tarefa': tarefa, 'form':form})


def mover_para_tarefas(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    tarefa.status = 'pendente'
    tarefa.save()
    return redirect('tarefas_pendentes')