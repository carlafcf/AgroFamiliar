from django.shortcuts import render
from django.http import HttpResponse
import json

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from Producao.models import Producao, Plantio

class CriarProducao(CreateView):
    model = Producao
    fields = ['nome', 'observacao']
    template_name = 'Producao/criar.html'
    success_url = reverse_lazy('producao:listar')

    # form

class EditarProducao(UpdateView):
    model = Producao
    fields = ['nome', 'observacao']
    template_name = 'Producao/editar.html'
    success_url = reverse_lazy('producao:listar')

    # form

def listar_producao(request):
    lista_producoes = Producao.objects.filter(ativo=True)

    informacoes = {
        'lista' : lista_producoes
    }

    return render(request, "Producao/listar.html", informacoes)

def listar_plantio(request):
    lista_plantios = Plantio.objects.all()

    informacoes = {
        'lista' : lista_plantios
    }

    return render(request, "Producao/listar_plantios.html", informacoes)

def detalhes_producao(request, pk):
    producao = Producao.objects.filter(pk=pk)[0]

    informacoes = {
        'producao': producao
    }

    return render(request, "Producao/detalhes.html", informacoes)

def desativar_producao(request):
    print("Desativando...")
    pk = request.GET.get('pk')
    producao = Producao.objects.get(pk=pk)
    producao.ativo = False
    producao.save()
    
    response_data = 'successful!'

    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json"
    )
