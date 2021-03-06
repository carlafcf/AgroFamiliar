from django.contrib.auth.models import User
from django.db import models

class Usuario(User):
    endereco = models.CharField(max_length=100, verbose_name='Endereço')
    cidade = models.CharField(max_length=100, verbose_name='Cidade')
    estado = models.CharField(max_length=100, verbose_name='Estado')

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        ordering = ['first_name', 'last_name']
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
