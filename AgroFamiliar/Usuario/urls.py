from django.urls import path

from django.contrib.auth import views as auth_views
from Usuario import views

app_name = 'usuario'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='Usuario/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('cadastrar/', views.Cadastrar.as_view(), name="cadastrar"),
    # path('editar/<int:pk>', views.Editar.as_view(), name = 'editar'),
    path('listar/<int:ativo>', views.listar, name='listar'),
    path('listar/mudar_status/', views.mudar_status, name='mudar_status'),
    path('listar/mudar_status_admin/', views.mudar_status_admin, name='mudar_status_admin'),
]