from django.urls import path
from app_gestao.views import login_view, home
from app_estoque.views import estoque, edit_item, delete_item
from app_financeiro.views import financeiro, delete_transaction
from app_config.views import cadastrar_cliente, delete_user
from app_dashboards.views import dashboard

urlpatterns = [
    path('', login_view, name='login'),
    path('home/', home, name='home'),
    path('home/financeiro/', financeiro, name='financeiro'),
    path('home/delete_transaction/<int:transaction_id>/', delete_transaction, name='delete_transaction'),
    path('home/dashboard/', dashboard, name='dashboard'),
    path('home/estoque/', estoque, name='estoque'),
    path('home/estoque/edit/<int:item_id>', edit_item, name='edit_item_page'),
    path('home/estoque/delete_estoque/<int:item_id>/', delete_item, name='delete_item_page'),
    path('home/cadastro/', cadastrar_cliente, name='cadastro'),
    path('home/cadastro/delete_cadastro/<int:cliente_id>/', delete_user, name='delete_user'),
]
