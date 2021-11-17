# MVT

# Model - descreve o banco
# View - funcionalidade do sistema
# Template - telas

from django.urls import path
from Producao import views

urlpatterns = [
    path('criar/', views.CriarProducao.as_view(), name='criar'),
    path('listar/', views.listar_producao, name='listar'),
    # path('editar/<int:pk>', Home.as_view(), name='editar'),
    # path('deletar/<int:pk>', Home.as_view(), name='deletar'),
    # path('detalhes/<int:pk>', Home.as_view(), name='detalhes'),
]