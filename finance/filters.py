import django_filters

from .models import AccountOperation


class StatementFilter(django_filters.FilterSet):
    created_at = django_filters.DateFromToRangeFilter(label="Период:")
    account = django_filters.ModelMultipleChoiceFilter
    description = django_filters.CharFilter(lookup_expr="lower_icontains")

    class Meta:
        model = AccountOperation
        fields = [
            "created_at",
            "description",
            "account",
            "operation__amount",
            "operation__type",
        ]
