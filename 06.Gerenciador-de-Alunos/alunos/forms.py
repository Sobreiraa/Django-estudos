from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['matricula', 'nome', 'sobrenome', 'email', 'materia', 'media_nota']
        labels = {
            'matricula': 'Matrícula', 
            'nome': 'Nome', 
            'sobrenome': 'Sobrenome', 
            'email': 'E-mail', 
            'materia': 'Matéria', 
            'media_nota': 'Média',
        }
        widgets = {
            'matricula': forms.NumberInput(attrs={'class': 'form-control'}), 
            'nome': forms.TextInput(attrs={'class': 'form-control'}), 
            'sobrenome': forms.TextInput(attrs={'class': 'form-control'}), 
            'email': forms.EmailInput(attrs={'class': 'form-control'}), 
            'materia': forms.TextInput(attrs={'class': 'form-control'}), 
            'media_nota': forms.NumberInput(attrs={'class': 'form-control'}),
        } 
    