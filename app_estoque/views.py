from django.shortcuts import render, redirect, get_object_or_404
from app_estoque.models import ItemEstoque
from app_estoque.forms import ItemEstoqueForm, DeleteItemForm
from django.db.models import Q


def estoque(request, item_id=None):
    error_message = None

    # Se um item_id for fornecido, trata-se de uma solicitação de edição
    if item_id:
        item = ItemEstoque.objects.get(id=item_id)
        if request.method == 'POST':
            form = ItemEstoqueForm(request.POST, instance=item)
            if form.is_valid():
                nome = form.cleaned_data['nome']
                if ItemEstoque.objects.exclude(id=item_id).filter(nome=nome).exists():
                    error_message = 'Um item com o mesmo nome já existe no estoque.'
                else:
                    form.save()
                    return redirect('estoque')
        else:
            form = ItemEstoqueForm(instance=item)
    else:
        item = None

    if request.method == 'POST':
        form = ItemEstoqueForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            if ItemEstoque.objects.filter(nome=nome).exists():
                error_message = 'Um item com o mesmo nome já existe no estoque.'
            else:
                form.save()
                return redirect('estoque')
    else:
        form = ItemEstoqueForm()

    # Verifique se há um parâmetro de pesquisa na URL
    query = request.GET.get('query', '')
    if query:
        items = ItemEstoque.objects.filter(Q(nome__icontains=query))
    else:
        items = ItemEstoque.objects.all()

    return render(request, 'estoque.html', {'form': form, 'items': items, 'edit_item': item, 'error_message': error_message})


def edit_item(request, item_id):
    try:
        item = ItemEstoque.objects.get(id=item_id)
    except ItemEstoque.DoesNotExist:
        form = ItemEstoqueForm()
        error_message = 'Item não encontrado. Verifique o ID informado.'
        return render(request, 'edit_item.html', {'form': form, 'error': error_message, 'item': None})

    if request.method == 'POST':
        form = ItemEstoqueForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('estoque')

    else:
        form = ItemEstoqueForm(instance=item)

    return render(request, 'edit_item.html', {'form': form, 'error': None, 'item': item})


def delete_item(request, item_id):
    item = get_object_or_404(ItemEstoque, id=item_id)

    if request.method == 'POST':
        # Se o formulário foi submetido com confirmação
        item.delete()
        return redirect('estoque')

    return render(request, 'delete_item.html', {'item': item})





