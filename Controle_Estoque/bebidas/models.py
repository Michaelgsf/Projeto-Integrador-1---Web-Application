from django.db import models


class Bebidas(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    preco = models.FloatField()

    def __str__(self):
        return self.nome


class Venda(models.Model):
    nome = models.ForeignKey(Bebidas, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    def __str__(self):
        return f"Venda de {self.quantidade} unidades de {self.bebida.nome}"
