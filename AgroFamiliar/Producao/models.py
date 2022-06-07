from dataclasses import dataclass
from django.db import models

class Producao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    observacao = models.TextField(verbose_name="Observação")
    ativo = models.BooleanField(verbose_name="Ativo", default=True)
    # fazenda = models.ForeignKey('Fazenda', on_delete=models.RESTRICT)

    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ['nome']
        verbose_name = "Produção"
        verbose_name_plural = "Produções"
    
class Plantio(models.Model):
    data_inicio = models.DateField(verbose_name="Data de plantio")
    quantidade = models.PositiveIntegerField(verbose_name="Quantidade")
    producao = models.ForeignKey('Producao', on_delete=models.RESTRICT)
    
    def __str__(self):
        return str(self.producao) + " - " + str(self.data_inicio)
    
    class Meta:
        ordering = ['-data_inicio']
        verbose_name = "Plantio"
        verbose_name_plural = "Plantios"

class Colheita(models.Model):
    data = models.DateField(verbose_name="Data da colheita")
    quantidade = models.PositiveIntegerField(verbose_name="Quantidade")
    producao = models.ForeignKey('Producao', on_delete=models.RESTRICT)
    
    def __str__(self):
        return str(self.producao) + " - " + str(self.data)
    
    class Meta:
        ordering = ['-data']
        verbose_name = "Colheita"
        verbose_name_plural = "Colheitas"

# class Relatorio(models.Model):
#     ...
#     producao = models.ForeignKey('Producao', on_delete=models.RESTRICT)

