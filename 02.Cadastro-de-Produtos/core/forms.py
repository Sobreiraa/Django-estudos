from django import forms
from django.core.mail.message import EmailMessage
from .models import Produto

class ContatoForm(forms.Form): #Form
    nome = forms.CharField(label='Nome:', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=100)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())


    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'

        mail = EmailMessage (
            subject = 'E-mail enviado pelo sistema django2.', #Assunto
            body = conteudo, #Corpo do e-mail
            from_email = 'contato@dominio.com.br', #Quem está enviando
            to=['contato@seudominio.com.br'], #Para quem será enviado
            headers = {'Reply-To': email}, #Resposta para quem será enviado
        )

        mail.send()


class ProdutoModelForm(forms.ModelForm): #ModelForm
    
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque', 'imagem']