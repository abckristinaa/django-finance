from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name = "finance"

urlpatterns = [
    path("", LoginView.as_view(template_name="login.html"), name="login"),
    path('home', views.main, name="main"),
    path('balance', views.BalanceView.as_view(), name="general"),
    path('wallets', views.WalletView.as_view(), name="wallets"),
    path('wallet-creation', views.WalletCreateView.as_view(), name="wallet-creation"),
    path('wallet/statement', views.statement_list, name="statement"),
    path('wallet/<int:pk>/statement', views.statement_list, name="wallet-statement"),
    path('wallet/<int:pk>/operations', views.add_operation, name="operations"),
    path('wallet/<int:pk>/edit', views.WalletUpdateView.as_view(), name="wallet-edition"),
    path('wallet/<int:pk>/delete', views.WalletRemoveView.as_view(), name="wallet-deletion"),
]