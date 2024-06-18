from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Login'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))

    def clean(self):
        cleaned_data = super().clean()

        # Adicione suas próprias validações, se necessário

        return cleaned_data