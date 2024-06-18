from django.shortcuts import render
from app_financeiro.models import Transaction
from app_dashboards.forms import DateRangeForm
import plotly.graph_objs as go
import locale


locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')  # Configurando o idioma para português do Brasil


def dashboard(request):
    dates = Transaction.objects.order_by('date').values_list('date', flat=True).distinct()
    selected_date = None

    form = DateRangeForm(request.GET or None)

    if form.is_valid():
        transactions = form.filter_transactions()
        selected_date = form.cleaned_data['start_date']
    else:
        transactions = Transaction.objects.all()

    entry_data = {}
    exit_data = {}
    for transaction in transactions:
        if transaction.type == 'Entrada':
            if transaction.description in entry_data:
                entry_data[transaction.description] += float(transaction.amount)
            else:
                entry_data[transaction.description] = float(transaction.amount)
        elif transaction.type == 'Saída':
            if transaction.description in exit_data:
                exit_data[transaction.description] += float(transaction.amount)
            else:
                exit_data[transaction.description] = float(transaction.amount)

    entry_trace = go.Bar(
        x=list(entry_data.keys()),
        y=list(entry_data.values()),
        name='Entrada',
        marker=dict(color='green'),
        text=[f'R$ {val}' for val in entry_data.values()],
    )

    entry_layout = go.Layout(
        title='Transações de Entrada',
        yaxis=dict(title='Valor'),
        plot_bgcolor='#2c3338',
        paper_bgcolor='#2c3338',
        font=dict(color='white'),
    )
    entry_figure = go.Figure(data=[entry_trace], layout=entry_layout)
    entry_plot_div = entry_figure.to_html(full_html=False)

    exit_trace = go.Bar(
        x=list(exit_data.keys()),
        y=list(exit_data.values()),
        name='Saída',
        marker=dict(color='red'),
        text=[f'R$ {val}' for val in exit_data.values()],
    )

    exit_layout = go.Layout(
        title='Transações de Saída',
        yaxis=dict(title='Valor'),
        plot_bgcolor='#2c3338',
        paper_bgcolor='#2c3338',
        font=dict(color='white'),
    )
    exit_figure = go.Figure(data=[exit_trace], layout=exit_layout)
    exit_plot_div = exit_figure.to_html(full_html=False)

    # Novo gráfico para a diferença entre o total de Entradas e Saídas ao longo do tempo
    monthly_diff_data = {}
    months_with_values = set()  # Conjunto para armazenar os meses com valores distintos de zero

    for transaction in transactions:
        year_month = transaction.date.strftime('%B/%Y')  # Formatação para mês e ano
        if transaction.type == 'Entrada':
            if year_month in monthly_diff_data:
                monthly_diff_data[year_month] += float(transaction.amount)
            else:
                monthly_diff_data[year_month] = float(transaction.amount)
                months_with_values.add(year_month)
        elif transaction.type == 'Saída':
            if year_month in monthly_diff_data:
                monthly_diff_data[year_month] -= float(transaction.amount)
            else:
                monthly_diff_data[year_month] = -float(transaction.amount)
                months_with_values.add(year_month)

    months_labels = list(months_with_values)  # Utilizando apenas os meses com valores

    monthly_diff_trace = go.Bar(
        x=list(months_with_values),  # Usar apenas os meses com valores
        y=[monthly_diff_data[month] for month in months_with_values],
        name='Total',
        marker=dict(color='blue'),
        text=[f'R$ {monthly_diff_data[month]}' for month in months_with_values],
    )

    monthly_diff_layout = go.Layout(
        title='Total Mensal',
        yaxis=dict(title='Valor'),
        plot_bgcolor='#2c3338',
        paper_bgcolor='#2c3338',
        font=dict(color='white'),
    )

    monthly_diff_figure = go.Figure(data=[monthly_diff_trace], layout=monthly_diff_layout)
    monthly_diff_figure.update_xaxes(tickvals=list(months_with_values), ticktext=months_labels)
    monthly_diff_plot_div = monthly_diff_figure.to_html(full_html=False)

    return render(request, 'dashboard.html', {
        'entry_plot_div': entry_plot_div,
        'exit_plot_div': exit_plot_div,
        'monthly_diff_plot_div': monthly_diff_plot_div,
        'dates': dates,
        'selected_date': selected_date,
        'form': form
    })