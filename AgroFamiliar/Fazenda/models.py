from django.db import models


class Fazenda(models.Model):
    nome = models.CharField(max_length=100, verbose_name="nome")
    endereco = models.TextField(verbose_name="endereco")
    cidade = models.CharField(max_length=100, verbose_name="cidade")
    estado = models.CharField(max_length=2, verbose_name="estado")

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']