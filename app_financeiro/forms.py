from django import forms
from .models import Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['description', 'amount', 'type']

    def __init__(self, *args, **kwargs):
        super(TransactionForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['placeholder'] = 'Descrição'
        self.fields['amount'].widget.attrs['placeholder'] = 'Valor'

        self.fields['description'].label = 'Descrição'
        self.fields['amount'].label = 'Valor'
        self.fields['type'].label = 'Tipo'
