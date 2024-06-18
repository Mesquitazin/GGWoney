from django.db import models
from django.utils import timezone


class CadastroCliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    empresa = models.CharField(max_length=100)
    email = models.EmailField()
    login = models.CharField(max_length=100, blank=True)
    senha = models.CharField(max_length=100, blank=True)
    data_cadastro = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome