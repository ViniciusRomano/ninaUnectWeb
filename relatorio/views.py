from django.shortcuts import render, redirect

from datetime import date, timedelta, datetime

from permanencia.models import Permanencia
from pessoal.models import Funcionario

# Create your views here.
def dia(request, dia, mes, ano):
    """
    Permanencias de uma data especifica    
    """
    data = date(int(ano), int(mes), int(dia))
    permanencias = Permanencia.objects.ano(ano).mes(mes).dia(dia)
    return render(request, 'dia.html', {'permanencias': permanencias, 'data': data})

def hoje(request):
    data = date.today()
    return redirect('dia', dia=data.day, mes=data.month, ano=data.year)

def funcionario(request, ra):
    """
    Relatorio funcionario
    """
    funcionario = Funcionario.objects.get_by_ra(ra)
    permanencias = funcionario.permanencias.all()
    return render(request, 'permanencia.html', {'permanencias': permanencias, 'funcionario': funcionario, 'tempo': tempo(permanencias)})

def tempo(permanencias):
    """
    parametro: lista de permanencias
    retorno: tempo total da lista de permanencias
    """
    tempo = timedelta() #deltatime eh usado para operacoes entre time's
    for permanencia in permanencias:
        tempo += permanencia.hora_saida() - permanencia.entrada #[horario de saida OU agora] - horario de entrada
    tempo = (datetime.min + tempo).time() #converte o deltatime em time
    return tempo