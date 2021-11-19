from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from Fazenda.models import Fazenda

class CriarFazenda(CreateView):
    model = Fazenda
    fields = ['nome', 'endereco', 'cidade', 'estado']
    template_name = 'Fazenda/criar.html'
    success_url = reverse_lazy('fazenda:listar')


def listar_fazenda(request):
    lista_fazenda = Fazenda.objects.all()

    informacoes = {
        'lista' : lista_fazenda
    }

    return render(request, "Fazenda/listar.html", informacoes)