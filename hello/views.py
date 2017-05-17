from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, timedelta
from django.utils import timezone

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
    funcionario = Funcionario.objects.get_by_ra(ra)
    permanencias = Permanencia.objects.get_by_funcionario(ra).get_by_data(dia, mes, ano)
    return render(request, 'permanencia.html', {'permanencias': permanencias, 'funcionario': funcionario, 'data': date(int(ano), int(mes), int(dia)), 'minutos': tempo(permanencias)})

def entrada(request, ra):
    return HttpResponse(Permanencia.objects.nova_entrada(ra))

def saida(request, ra):
    return HttpResponse(Permanencia.objects.nova_saida(ra))

def hoje(request):
    hoje = timezone.now()
    return render(request, 'hoje.html', {'permanencias': Permanencia.objects.get_by_data(hoje.day, hoje.month, hoje.year), 'data': hoje})

def dia(request, dia, mes, ano):
    permanencias = Permanencia.objects.get_by_data(dia, mes, ano)
    return render(request, 'dia.html', {'permanencias': permanencias, 'data': date(int(ano), int(mes), int(dia))})

def tempo(permanencias):
    tempo = timedelta()
    for permanencia in permanencias:
            tempo += (permanencia.saida if permanencia.saida != None else timezone.now()) - permanencia.entrada
    return (tempo.seconds//60)%60


    #dias, horas, minutos
    #td.days, td.seconds//3600, (td.seconds//60)%60