from django.shortcuts import render, redirect
from app_gestao.forms import LoginForm
from app_config.models import CadastroCliente


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificar se as credenciais são válidas usando o modelo CadastroCliente
            user = CadastroCliente.objects.filter(login=username, senha=password).first()

            if user is not None:
                # Aqui você pode adicionar a lógica adicional, se necessário
                return redirect('home')  # Substitua 'home' pelo nome da sua URL de home
            else:
                return render(request, 'login.html', {'form': form, 'message': 'Usuário ou senha inválidos.'})
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def home(request):
    return render(request, 'home.html')


def dashboard(request):
    return render(request, 'dashboard.html')
