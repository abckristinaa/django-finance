# Generated by Django 3.0.5 on 2020-04-15 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('current_balance', models.PositiveIntegerField(default=0)),
            ],
            options={
                'db_table': 'account',
            },
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Сумма', models.PositiveIntegerField()),
                ('type', models.CharField(choices=[('Поступление', 'plus'), ('Списание', 'minus')], max_length=15)),
            ],
            options={
                'db_table': 'operation',
            },
        ),
        migrations.CreateModel(
            name='AccountOperation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(blank=True, max_length=120)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='finance.Account')),
                ('operation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='finance.Operation')),
            ],
            options={
                'db_table': 'account_operation',
            },
        ),
        migrations.AddConstraint(
            model_name='accountoperation',
            constraint=models.UniqueConstraint(fields=('created_at', 'operation'), name='no_dublicats'),
        ),
    ]