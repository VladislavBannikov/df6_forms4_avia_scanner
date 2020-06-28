import time
import random

from django.shortcuts import render
from django.http import JsonResponse
from django.core.cache import cache

from .models import City
from .forms import SearchTicket


def ticket_page_view(request):
    template = 'app/ticket_page.html'

    context = {
        'form': SearchTicket()
    }

    return render(request, template, context)


def cities_lookup(request):
    """Ajax request предлагающий города для автоподстановки, возвращает JSON"""
    results = cache.get("cities")
    if results is None:
        # TODO: Возможно это не самый оптимальный способ, но другого я не нашел.
        results = [i[0] for i in City.objects.all().values_list("name")]
        cache.set("cities", results, 20)
        print('---No cache')
    else:
        print('---From cache')
        # TODO: Почему debug_toolbar не показывает этот кэш?

    return JsonResponse(results, safe=False)
