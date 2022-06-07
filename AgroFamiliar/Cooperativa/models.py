from Usuario.models import Usuario
from django.db import models

class Coperativa(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome da Coperativa')
    responsavel = models.ForeignKey('Usuario', on_delete=models.RESTRICT)
    endereco = models.CharField(max_length=100, verbose_name='Endereço')

    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ['nome']
        verbose_name = "Cooperativa"
        verbose_name_plural = "Cooperativas"

class Cooperado(models.Model):
    usuario = models.ForeignKey('Usuario', on_delete=models.RESTRICT)
    cooperativa = models.ForeignKey('Cooperativa', on_delete=models.RESTRICT)

    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ['nome']
        verbose_name = "Cooperado"
        verbose_name_plural = "Cooperados"

 
# Create your models here.
