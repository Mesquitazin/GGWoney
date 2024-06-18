from django import forms
from .models import CadastroCliente
import random
import string


class CadastroClienteForm(forms.ModelForm):
    class Meta:
        model = CadastroCliente
        fields = ['nome', 'cpf', 'empresa', 'email', 'login', 'senha']

        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome do Cliente'}),
            'cpf': forms.TextInput(attrs={'placeholder': 'CPF'}),
            'empresa': forms.TextInput(attrs={'placeholder': 'Empresa'}),
            'email': forms.EmailInput(attrs={'placeholder': 'E-Mail'}),
            'login': forms.TextInput(attrs={'placeholder': 'Login'}),
            'senha': forms.PasswordInput(render_value=True, attrs={'placeholder': 'Senha'}),
        }

    def __init__(self, *args, **kwargs):
        super(CadastroClienteForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()

        # Verificar se já existe um cliente com o mesmo nome
        existing_name = CadastroCliente.objects.filter(nome=cleaned_data['nome']).exclude(pk=self.instance.pk).first()
        if existing_name:
            raise forms.ValidationError('Já existe um cliente com o mesmo nome.')

        # Verificar se já existe um cliente com o mesmo CPF
        existing_cpf = CadastroCliente.objects.filter(cpf=cleaned_data['cpf']).exclude(pk=self.instance.pk).first()
        if existing_cpf:
            raise forms.ValidationError('Já existe um cliente com o mesmo CPF.')

        # Verificar se já existe um cliente com o mesmo login
        existing_login = CadastroCliente.objects.filter(login=cleaned_data['login']).exclude(pk=self.instance.pk).first()
        if existing_login:
            raise forms.ValidationError('Já existe um cliente com o mesmo login.')

        # Verificar se já existe um cliente com o mesmo e-mail
        existing_email = CadastroCliente.objects.filter(email=cleaned_data['email']).exclude(pk=self.instance.pk).first()
        if existing_email:
            raise forms.ValidationError('Já existe um cliente com o mesmo e-mail.')

        # Se a senha estiver vazia, gera automaticamente
        if not cleaned_data.get('senha'):
            cleaned_data['senha'] = self.generate_password()

        return cleaned_data

    def generate_password(self, length=12):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))
