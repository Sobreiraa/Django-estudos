from django.shortcuts import render
from .models import Usuario

# Create your views here.
def index(request):
    return render(request, 'usuarios/index.html')


def usuarios(request):
    # Salvando os dados da tela no banco de dados.
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.sobrenome = request.POST.get('sobrenome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.sexo = request.POST.get('sexo')
    novo_usuario.save()
    # Exibindo todos os usuários já cadastrados
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    # Retornando os dados em um template html
    return render(request, 'usuarios/usuarios.html', usuarios)
    
