from django.shortcuts import render
from django.http import HttpResponse
import json

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from Producao.models import Colheita, Producao, Plantio

class CriarProducao(CreateView):
    model = Producao
    fields = ['nome', 'observacao']
    template_name = 'Producao/criar.html'
    success_url = reverse_lazy('producao:listar')

class CriarPlantio(CreateView):
    model = Plantio
    fields = ['producao', 'data_inicio', 'quantidade']
    template_name = 'Producao/criar_plantio.html'
    success_url = reverse_lazy('producao:listar_plantio')
    
class CriarColheita(CreateView):
    model = Colheita
    fields = ['producao', 'data', 'quantidade']
    template_name = 'Producao/criar_colheita.html'
    success_url = reverse_lazy('producao:listar_colheita')

class EditarProducao(UpdateView):
    model = Producao
    fields = ['nome', 'observacao']
    template_name = 'Producao/editar.html'
    success_url = reverse_lazy('producao:listar')

class EditarPlantio(UpdateView):
    model = Plantio
    fields = ['producao', 'data_inicio','quantidade']
    template_name = 'Producao/editar_plantio.html'
    success_url = reverse_lazy('producao:listar_plantio')
    
class EditarColheita(UpdateView):
    model = Colheita
    fields = ['producao', 'data','quantidade']
    template_name = 'Producao/editar_colheita.html'
    success_url = reverse_lazy('producao:listar_colheita')

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

def detalhes_plantio(request, pk):
    plantio = Plantio.objects.filter(pk=pk)[0]

    informacoes = {
        'plantio': plantio
    }

    return render(request, "Plantio/detalhes.html", informacoes)


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
