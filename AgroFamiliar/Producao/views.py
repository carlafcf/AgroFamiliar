from django.shortcuts import render
from django.views.generic.edit import CreateView

from Producao.models import Producao

class CriarProducao(CreateView):
    model = Producao
    fields = ['nome', 'observacao']
    template_name = 'Producao/criar.html'

    # form

def listar_producao(request):
    lista_producoes = Producao.objects.all()

    informacoes = {
        'lista' : lista_producoes
    }

    return render(request, "Producao/listar.html", informacoes)
