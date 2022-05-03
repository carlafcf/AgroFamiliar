# MVT

# Model - descreve o banco
# View - funcionalidade do sistema
# Template - telas

from django.urls import path
from Producao import views

app_name = "producao"

urlpatterns = [
    path('criar_producao/', views.CriarProducao.as_view(), name='criar_producao'),
    path('listar_producao/', views.listar_producao, name='listar_producao'),
    path('listar_producao/desativar/', views.desativar_producao, name='desativar_producao'),
    path('editar_producao/<int:pk>', views.EditarProducao.as_view(), name='editar_producao'),
    path('detalhes_producao/<int:pk>', views.detalhes_producao, name='detalhes_producao'),

    path('listar_plantio/', views.listar_plantio, name='listar_plantio'),
]