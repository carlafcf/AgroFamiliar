# MVT

# Model - descreve o banco
# View - funcionalidade do sistema
# Template - telas

from django.urls import path
from Producao import views

app_name = "producao"

urlpatterns = [
    path('criar/', views.CriarProducao.as_view(), name='criar'),
    path('listar/', views.listar_producao, name='listar'),
    path('listar/desativar/', views.desativar_producao, name='desativar'),
    path('editar/<int:pk>', views.EditarProducao.as_view(), name='editar'),
    path('detalhes/<int:pk>', views.detalhes_producao, name='detalhes'),
]