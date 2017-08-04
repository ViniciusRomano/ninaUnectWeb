from django.shortcuts import render, redirect

from datetime import date, timedelta, datetime

from permanencia.models import Permanencia
from pessoal.models import Funcionario, Empresa

# Create your views here.
def dia(request, empresa, dia, mes, ano):
    """
    Permanencias de uma data especifica    
    """
    data = date(int(ano), int(mes), int(dia))
    empresa = Empresa.objects.all().get(pk=empresa)
    permanencias = Permanencia.objects.empresa(empresa).ano(ano).mes(mes).dia(dia)
    return render(request, 'dia.html', {'permanencias': permanencias, 'data': data})

def hoje(request, empresa):
    data = date.today()
    return redirect('dia', empresa=empresa, dia=data.day, mes=data.month, ano=data.year)

def funcionario(request, empresa, ra):
    """
    Relatorio funcionario
    """
    data = date.today()

    dia = request.GET.get('dia', None)
    mes = request.GET.get('mes', data.month)
    ano = request.GET.get('ano', data.year)
    empresa = Empresa.objects.all().get(pk=empresa)
    funcionario = Funcionario.objects.get_by_empresa(empresa).get_by_ra(ra)
    permanencias = funcionario.permanencias.ano(ano).mes(mes)
    if dia is not None:
        permanencias = permanencias.dia(dia)
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