from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
import json

from django.views.generic.edit import CreateView

from Usuario.models import Usuario
from Usuario import forms

class Cadastrar(CreateView):
    form_class = forms.FormCriarUsuario
    template_name = 'Usuario/cadastrar.html'
    success_url = reverse_lazy('usuario:login')

    # form

def listar (request, ativo):
    lista_usuarios = Usuario.objects.filter(is_active=ativo)
    
    informacoes = {
        'lista_usuarios': lista_usuarios,
        'ativo': ativo
    }

    return render(request, "Usuario/listar.html", informacoes)

def mudar_status(request):
    pk = request.GET.get('pk')

    usuario = Usuario.objects.get(pk=pk)
    usuario.is_active = not usuario.is_active
    usuario.save()

    response_data = 'successful!'

    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json"
    )

def mudar_status_admin(request):
    pk = request.GET.get('pk')

    usuario = Usuario.objects.get(pk=pk)
    usuario.is_superuser = not usuario.is_superuser
    usuario.save()

    response_data = usuario.is_superuser

    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json"
    )