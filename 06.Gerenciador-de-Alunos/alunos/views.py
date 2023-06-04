from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import AlunoForm
from .models import Aluno

def index(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos/index.html', {'alunos': alunos})


def visualizar_aluno(request, id):
    aluno = Aluno.objects.get(id=id)
    return HttpResponseRedirect(reverse('index'))


def adicionar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
           matricula = form.cleaned_data['matricula']
           nome = form.cleaned_data['nome']
           sobrenome = form.cleaned_data['sobrenome']
           email = form.cleaned_data['email']
           materia = form.cleaned_data['materia']
           media = form.cleaned_data['media_nota']

           aluno = Aluno (
                matricula=matricula,
                nome=nome,
                sobrenome=sobrenome,
                email=email,
                materia=materia,
                media_nota=media, 
           )

           aluno.save()
           return render(request, 'alunos/adicionar_aluno.html', {
               'form': AlunoForm(),
               'success': True
           })

    else:
        form = AlunoForm()
        return render(request, 'alunos/adicionar_aluno.html', {
            'form': AlunoForm()
        })


def editar_aluno(request, id):
    if request.method == 'POST':
        aluno = Aluno.objects.get(id=id)
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return render(request, 'alunos/editar_aluno.html', {
                'form': form,
                'success': True
            })
    else:
        aluno = Aluno.objects.get(id=id)
        form = AlunoForm(instance=aluno)
    return render(request, 'alunos/editar_aluno.html', {
        'form': form
    })


def deletar_aluno(request, id):
    if request.method == 'POST':
        aluno = Aluno.objects.get(id=id)
        aluno.delete()
    return HttpResponseRedirect(reverse('index'))