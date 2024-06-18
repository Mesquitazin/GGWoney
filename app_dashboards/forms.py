from django import forms
from app_financeiro.models import Transaction


class DateRangeForm(forms.Form):
    start_date = forms.DateField(label='Data de Início', widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(label='Data de Fim', widget=forms.DateInput(attrs={'type': 'date'}))

    def filter_transactions(self):
        start_date = self.cleaned_data['start_date']
        end_date = self.cleaned_data['end_date']

        # Filtrar transações pelo intervalo de datas
        transactions = Transaction.objects.filter(date__range=[start_date, end_date])
        return transactions
