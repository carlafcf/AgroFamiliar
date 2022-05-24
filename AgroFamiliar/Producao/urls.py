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

    path('criar_plantio/', views.CriarPlantio.as_view(), name='criar_plantio'),
    path('listar_plantio/', views.listar_plantio, name='listar_plantio'),
    path('editar_plantio/<int:pk>', views.EditarPlantio.as_view(), name='editar_plantio'),
    path('detalhes_plantio/<int:pk>', views.detalhes_plantio, name='detalhes_plantio'),
    
    path('criar_colheita/', views.CriarColheita.as_view(), name='criar_colheita'),
]