from django.db import models
from django.urls import reverse
from django.db.models import Sum


class Account(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False)
    start_balance = models.PositiveIntegerField(default=0)
    current_balance = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "account"

    def __str__(self):
        return self.name

    @staticmethod
    def get_absolute_url():
        return reverse('finance:wallets')

    @classmethod
    def total(cls):
        return cls.objects.all().aggregate(Sum('current_balance'))["current_balance__sum"]


class Operation(models.Model):
    amount = models.IntegerField(default=0)
    type = models.CharField(choices=[
        ("Поступление", "deposit"),
        ("Списание", "withdrawal"),
        ], max_length=15)

    class Meta:
        db_table = "operation"
        constraints = [
            models.UniqueConstraint(
                fields=["amount", "type"], name="operation_uniq"
            )
        ]


class AccountOperation(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=120, blank=True)
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        db_table = "account_operation"
        constraints = [
            models.UniqueConstraint(
                fields=["created_at", "operation"], name="history_uniq"
            )
        ]
