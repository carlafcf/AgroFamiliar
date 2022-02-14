from django.contrib.auth import forms as auth_forms
from django import forms
from django.forms import ModelForm

from Usuario.models import Usuario

class FormCriarUsuario(auth_forms.UserCreationForm):

    class Meta:
        model = Usuario
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'endereco', 'cidade', 'estado']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = 'Nome'
        self.fields['last_name'].label = 'Sobrenome'
        self.fields['username'].label = 'Nome de usuário'
        self.fields['cidade'].label = 'Cidade'
        self.fields['estado'].label = 'Estado'
        self.fields['endereco'].label = 'Endereço'
        self.fields['email'].label = 'E-mail'
        self.fields['password1'].label = 'Senha'
        self.fields['password2'].label = 'Confirmar senha'