from pessoal.models import Funcionario, Empresa
from .models import Permanencia
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import usuario_desktop

@api_view()
def entrada(request, ra, empresa):
    if usuario_desktop(request):
        empresa = Empresa.objects.all().get(id=empresa)
        funcionario = Funcionario.objects.get_by_empresa(empresa).get_by_ra(ra)
        return Response(Permanencia.nova_entrada(funcionario))

@api_view()
def saida(request, ra, empresa):
    if usuario_desktop(request):
        empresa = Empresa.objects.all().get(id=empresa)
        funcionario = Funcionario.objects.get_by_empresa(empresa).get_by_ra(ra)
        return Response(Permanencia.nova_saida(funcionario))