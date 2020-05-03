import django_filters

from .models import AccountOperation


class StatementFilter(django_filters.FilterSet):
    created_at = django_filters.DateFromToRangeFilter(label="Период:")
    account = django_filters.ModelMultipleChoiceFilter

    class Meta:
        model = AccountOperation
        fields = [
            "created_at",
            "account",
        ]
