from django.db import models

# Create your models here.

class Produto(models.Model):
    cod_produto = models.CharField(max_length=5)
    nome = models.CharField(max_length=200)
    categoria = models.CharField(max_length=50)
    estoque_atual = models.IntegerField()
    estoque_minimo = models.IntegerField()


    def __str__(self):
        return self.nome 