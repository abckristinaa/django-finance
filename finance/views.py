from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import generic

from finance.models import Account, AccountOperation, Operation

from .filters import StatementFilter
from .forms import CreateWalletForm, UpdateWalletForm


def main(request):
    return render(request, "main.html")


class WalletView(generic.ListView):
    """ Renders list of existing wallets for making changes."""

    model = Account
    template_name = "wallets.html"


class BalanceView(WalletView):
    """Renders list of existing wallets with balance."""

    template_name = "balances.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["total"] = Account.total()
        return context


class WalletCreateView(generic.CreateView):
    form_class = CreateWalletForm
    template_name = "wallet_detail.html"


class WalletUpdateView(generic.UpdateView):
    model = Account
    form_class = UpdateWalletForm
    template_name = "wallet_detail.html"


class WalletRemoveView(generic.DeleteView):
    model = Account
    template_name = "account_confirm_delete.html"
    template_name_suffix = ""
    success_url = "/wallets"


def statement_list(request, pk=None):
    if pk:
        queryset = AccountOperation.objects.filter(account=pk)
    else:
        queryset = AccountOperation.objects.all()
    f = StatementFilter(request.GET, queryset)
    return render(request, "statement.html", {"filter": f})


@transaction.atomic
def add_operation(request, pk):
    wallet = Account.objects.get(id=pk)
    if request.method == "POST":
        form_data = request.POST
        amount = int(form_data["amount"])
        operation_type = form_data["type"]
        current_balance = wallet.current_balance
        if operation_type == "withdrawal":
            if int(amount) > current_balance:
                return HttpResponse("Денежных средств в кошельке недостаточно для списания.")

        operation, created = Operation.objects.get_or_create(
            amount=amount, type=operation_type
        )
        if created:
            operation.save()

        journal_operation = AccountOperation(
            description=form_data["description"], operation=operation, account=wallet
        )
        journal_operation.save()

        if operation_type == "deposit":
            new_balance = current_balance + amount
        else:
            new_balance = current_balance - amount
        wallet.current_balance = new_balance
        wallet.save()
        return redirect("finance:general")
    else:
        return render(request, "operations.html", {"wallet": wallet})
