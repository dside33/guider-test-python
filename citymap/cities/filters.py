from django_filters import (
                            FilterSet, 
                            NumberFilter
                            )
from .models import Shop

from datetime import datetime
from django.http import Http404


class ShopFilter(FilterSet):
    city = NumberFilter(field_name='city', lookup_expr='exact')
    street = NumberFilter(field_name='street', lookup_expr='exact')
    open = NumberFilter(method='filter_open')

    class Meta:
        model = Shop
        fields = []

    def filter_open(self, queryset, name, value):
        now = datetime.now().time()
        if value == 1:
            return queryset.filter(open_time__lte=now, close_time__gte=now)
        elif value == 0:
            return queryset.exclude(open_time__lte=now, close_time__gte=now)
        else:
            raise Http404("Invalid value for 'open' parameter. Expected 1 or 0.")
