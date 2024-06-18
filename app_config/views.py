from django.shortcuts import render, redirect, get_object_or_404
from app_config.forms import CadastroClienteForm
from app_config.models import CadastroCliente


def cadastrar_cliente(request):
    if request.method == 'POST':
        form = CadastroClienteForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirecione ou faça qualquer outra coisa após salvar os dados
            return redirect('cadastro')
    else:
        form = CadastroClienteForm()

    # Adicione o código para obter clientes
    clientes = CadastroCliente.objects.all()

    return render(request, 'config.html', {'form': form, 'clientes': clientes})


def delete_user(request, cliente_id):
    item = get_object_or_404(CadastroCliente, id=cliente_id)

    if request.method == 'POST':
        # Se o formulário foi submetido com confirmação
        item.delete()
        return redirect('cadastro')

    return render(request, 'delete_user.html', {'item': item})