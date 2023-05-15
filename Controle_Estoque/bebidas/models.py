from django.db import models


# Create your models here.
# class User(models.Model):
#     nome = models.CharField('nome', max_length=20)
#     telefone = models.BigIntegerField('telefone')
#     email = models.CharField('email', max_length=30)

#     def __str__(self):
#         return f'Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}'
class Bebida(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    preco = models.FloatField()
