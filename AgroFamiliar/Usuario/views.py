from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from Usuario.models import Usuario
from Usuario import forms

class Cadastrar(CreateView):
    form_class = forms.FormCriarUsuario
    template_name = 'Usuario/cadastrar.html'
    success_url = reverse_lazy('usuario:login')

    # form
