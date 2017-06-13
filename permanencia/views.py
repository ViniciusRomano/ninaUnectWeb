from django.shortcuts import render, redirect
from django.http import HttpResponse
from pessoal.models import Funcionario
from .models import Permanencia

def entrada(request, ra, token):
    funcionario = Funcionario.objects.get_by_ra(ra)
    if verificar_token(token):
        return HttpResponse(Permanencia.nova_entrada(funcionario))
    else:
        return HttpResponse("token incorreto")

def saida(request, ra, token):
    funcionario = Funcionario.objects.get_by_ra(ra)
    if verificar_token(token):
        return HttpResponse(Permanencia.nova_saida(funcionario))
    else:
        return HttpResponse("token incorreto")

def verificar_token(token):
    #realizar verificacao
    if token == '123':
        return True
    else:
        return False
    