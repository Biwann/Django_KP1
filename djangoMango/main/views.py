from django.shortcuts import render
import random
from .models import Numbers
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def indexGen(request):
    k = 0
    if request.method == "GET":
        form = request.GET.get('from')
        ot = request.GET.get('to')
        if (form != '') or (ot != ''):
            a = int(form)
            b = int(ot)
            if a <= b:
                r = random.randint(a, b)

            else:
                r = 'error'
                return render(request, 'main/indexGen.html', {'number': r, 'kef':k})
        else:
            r = 'error'
            return render(request, 'main/indexGen.html', {'number': r, 'kef':k})
    return render(request, 'main/indexGen.html', {'number':r, 'kef':k})


def about(request):
    return render(request, 'main/about.html')


def check(request):
    return render(request, 'main/check.html')


def checkid(request):

    n = request.GET.get('genid')
    if (n != ''):
        n = int(n)
        if (n > 0) and (n < 10):
            numbs = Numbers.objects.get(id = n)
            return render(request, 'main/checkid.html', {'checkid': numbs})
        else:
            numbs = 'error'
            return render(request, 'main/checkid.html', {'checkid': numbs})
    else:
        numbs = 'error'
        return render(request, 'main/checkid.html', {'checkid': numbs})
    return render(request, 'main/checkid.html', {'checkid':numbs})