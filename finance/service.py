from .models import Account, AccountOperation, Operation


def set_current_balance(wallet_id, operation_id):
    wallet = Account.objects.get(id=wallet_id)
    operation = Operation.objects.get(id=operation_id)
    current_balance = wallet.current_balance
    if operation.type == "deposit":
        new_balance = current_balance + operation.amount
    else:
        new_balance = current_balance - operation.amount
    wallet.current_balance = new_balance
    return new_balance
