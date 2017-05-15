from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime

from .models import Greeting
from .models import Permanencia
from .models import Funcionario

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')


def db(request):
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

def permanencias(request, ra, dia, mes, ano):
    funcionario = Funcionario.objects.filter(ra=ra).first()
    permanencias = Permanencia.objects.filter(funcionario=funcionario).filter(entrada__day=dia, entrada__month=mes, entrada__year=ano)
    return render(request, 'permanencia.html', {'permanencias': permanencias, 'funcionario': funcionario, 'data': date(int(ano), int(mes), int(dia))})

def entrada(request, ra):
    return HttpResponse(Funcionario.objects.filter(ra=ra).first().marcar_entrada())

def saida(request, ra):
    return HttpResponse(Funcionario.objects.filter(ra=ra).first().marcar_saida())

def hoje(request):
    hoje = datetime.now()
    permanencias = Permanencia.objects.filter(entrada__day=hoje.day, entrada__month=hoje.month, entrada__year=hoje.year)
    return render(request, 'agora.html', {'permanencias': permanencias, 'data': hoje})

def dia(request, dia, mes, ano):
    permanencias = Permanencia.objects.filter(entrada__day=dia, entrada__month=mes, entrada__year=ano)
    return render(request, 'dia.html', {'permanencias': permanencias, 'data': date(int(ano), int(mes), int(dia))})