from django.db import models


class Transaction(models.Model):
    DESCRIPTION_CHOICES = (
        ('Entrada', 'Entrada'),
        ('Saída', 'Saída'),
    )

    description = models.CharField(max_length=255, verbose_name='Descrição')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor')
    type = models.CharField(max_length=10, choices=DESCRIPTION_CHOICES, verbose_name='Tipo')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Transação'
        verbose_name_plural = 'Transações'
        ordering = ['-date']
