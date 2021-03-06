# Generated by Django 3.0.5 on 2020-04-25 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("finance", "0001_initial"),
    ]

    operations = [
        migrations.RemoveConstraint(model_name="accountoperation", name="no_dublicats",),
        migrations.RemoveField(model_name="operation", name="Сумма",),
        migrations.AddField(
            model_name="account",
            name="start_balance",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="operation", name="amount", field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="operation",
            name="type",
            field=models.CharField(
                choices=[("Поступление", "deposit"), ("Списание", "withdrawal")],
                max_length=15,
            ),
        ),
        migrations.AddConstraint(
            model_name="accountoperation",
            constraint=models.UniqueConstraint(
                fields=("created_at", "operation"), name="history_uniq"
            ),
        ),
        migrations.AddConstraint(
            model_name="operation",
            constraint=models.UniqueConstraint(
                fields=("amount", "type"), name="operation_uniq"
            ),
        ),
    ]
