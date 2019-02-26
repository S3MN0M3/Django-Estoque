from django.db import models
from django.utils import timezone


class Bebida(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Estoque(models.Model):
    marca = models.ForeignKey(
        Bebida,
         on_delete=models.PROTECT)

    valor = models.DecimalField(
        max_digits=5,
        decimal_places=2)
    
    data = models.DateTimeField(
        blank=False)

    quantidade = models.IntegerField(
        default=1)   

    entrada = models.BooleanField()

    saida = models.BooleanField()
    
    observacoes = models.TextField(null=True, blank=True)

    def __str__(self):
        if self.entrada:
            return 'Entrou %s %s - Data: %s'%(
                self.quantidade,
                self.marca,
                self.data)
        else:
            return 'Saiu %s %s - Data: %s'%(
                self.quantidade,
                self.marca,
                self.data)
