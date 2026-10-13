from django.shortcuts import render

from academex.models import ExchangeProgram


def exchange(request):
    exchanges = ExchangeProgram.objects.all()
    return render(request, "academex/exchange.html", {"exchanges": exchanges})
