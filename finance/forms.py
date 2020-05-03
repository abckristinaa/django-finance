from django import forms
from .models import Account


class CreateWalletForm(forms.ModelForm):
    name = forms.CharField(label="Наименование")
    start_balance = forms.IntegerField(label="Начальный баланс, руб.")

    class Meta:
        model = Account
        fields = ["name", "start_balance"]


class UpdateWalletForm(forms.ModelForm):
    name = forms.CharField(label="Наименование")

    class Meta:
        model = Account
        fields = ["name"]
