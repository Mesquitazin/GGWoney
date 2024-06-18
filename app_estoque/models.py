from django.db import models
from django.utils import timezone


class ItemEstoque(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_adicao = models.DateTimeField(default=timezone.now)
