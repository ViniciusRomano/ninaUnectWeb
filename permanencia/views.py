from django.shortcuts import render, redirect
from django.http import HttpResponse
from pessoal.models import Funcionario
from .models import Permanencia
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from .utils import usuario_desktop

@api_view()
def entrada(request, ra):
    if usuario_desktop(request):
        funcionario = Funcionario.objects.get_by_ra(ra)
        return Response(Permanencia.nova_entrada(funcionario))

@api_view()
def saida(request, ra):
    if usuario_desktop(request):
        funcionario = Funcionario.objects.get_by_ra(ra)
        return Response(Permanencia.nova_saida(funcionario))

