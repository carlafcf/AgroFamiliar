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
    path('editar/<int:pk>', views.EditarProducao.as_view(), name='editar'),
    path('desativar/<int:pk>', views.desativar_producao, name='desativar'),
    path('detalhes/<int:pk>', views.detalhes_producao, name='detalhes'),
]