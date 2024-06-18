from django.shortcuts import render, redirect, get_object_or_404
from app_financeiro.forms import TransactionForm
from app_financeiro.models import Transaction
from django.db.models import F
from django.db.models import Q


def financeiro(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            # Processar os dados do formulário
            description = form.cleaned_data['description']
            amount = form.cleaned_data['amount']
            type = form.cleaned_data['type']

            # Verificar se já existe uma transação com a mesma descrição e mesmo tipo de ENTRADA
            existing_entry_transaction = Transaction.objects.filter(description=description, type='Entrada').first()

            # Verificar se já existe uma transação com a mesma descrição e mesmo tipo de SAÍDA
            existing_exit_transaction = Transaction.objects.filter(description=description, type='Saída').first()

            if existing_entry_transaction and type == 'Entrada':
                # Atualizar o valor da transação existente de ENTRADA
                existing_entry_transaction.amount = F('amount') + amount
                existing_entry_transaction.save()
            elif existing_exit_transaction and type == 'Saída':
                # Atualizar o valor da transação existente de SAÍDA
                existing_exit_transaction.amount = F('amount') + amount
                existing_exit_transaction.save()
            else:
                # Criar uma nova transação no banco de dados
                Transaction.objects.create(description=description, amount=amount, type=type)

            # Redirecione o usuário para a página financeiro após a adição bem-sucedida
            return redirect('financeiro')
        else:
            # Se o formulário não for válido, você pode lidar com erros aqui
            # Por exemplo, você pode passar os erros para o template
            errors = form.errors
    else:
        form = TransactionForm()
        errors = None  # Inicialize os erros como None

    # Verifique se há um parâmetro de pesquisa na URL
    query = request.GET.get('query', '')
    if query:
        transactions = Transaction.objects.filter(
            Q(description__icontains=query) |
            Q(amount__icontains=query) |
            Q(type__icontains=query)
        )
    else:
        transactions = Transaction.objects.all()

    # Calcule os totais
    total_incomes = sum(transaction.amount for transaction in transactions if transaction.type == 'Entrada')
    total_expenses = sum(transaction.amount for transaction in transactions if transaction.type == 'Saída')
    total_balance = total_incomes - total_expenses

    return render(request, 'financeiro.html', {'form': form, 'transactions': transactions, 'total_incomes': total_incomes, 'total_expenses': total_expenses, 'total_balance': total_balance, 'errors': errors})


def delete_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)

    if request.method == 'POST':
        # Se o formulário foi submetido com confirmação
        transaction.delete()
        return redirect('financeiro')

    return render(request, 'confirm_delete.html', {'transaction': transaction})
