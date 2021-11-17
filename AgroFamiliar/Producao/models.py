from django.db import models

class Producao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    observacao = models.TextField(verbose_name="Observação")
    # fazenda = models.ForeignKey('Fazenda', on_delete=models.RESTRICT)

    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ['nome']

# class Relatorio(models.Model):
#     ...
#     producao = models.ForeignKey('Producao', on_delete=models.RESTRICT)

    # def __str__(self):
    #     return self.data
    
    # class Meta:
    #     ordering = ['-data']

