from django import forms
from app_estoque.models import ItemEstoque


class ItemEstoqueForm(forms.ModelForm):
    class Meta:
        model = ItemEstoque
        fields = ['nome', 'quantidade', 'valor']

    def __init__(self, *args, **kwargs):
        super(ItemEstoqueForm, self).__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs['placeholder'] = 'Nome do Item'
        self.fields['quantidade'].widget.attrs['placeholder'] = 'Quantidade'
        self.fields['valor'].widget.attrs['placeholder'] = 'Valor'

    def for_edit(self):
        for field_name, field in self.fields.items():
            field.required = False  # Permite campos vazios para edição


class DeleteItemForm(forms.Form):
    item_id = forms.IntegerField(
        widget=forms.TextInput(attrs={'placeholder': 'ID do Item a ser excluído'})
    )




