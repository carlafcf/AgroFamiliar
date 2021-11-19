from django.urls import path
from . import views

app_name = "fazenda"

urlpatterns = [
    path('criar/', views.CriarFazenda.as_view(), name='criar'),
    path('listar/', views.listar_fazenda, name='listar'),
    #path('editar/<int:pk>', Home.as_view(), name='editar'),
    #path('deletar/<int:pk>', Home.as_view(), name='deletar'),
    #path('detalhes/<int:pk>', Home.as_view(), name='detalhes'),
]