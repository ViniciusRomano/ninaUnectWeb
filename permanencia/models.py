from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

from pessoal.models import Funcionario

class PermanenciaQuerySet(models.QuerySet):
    def dia(self, dia):
        return self.filter(entrada__day=dia)

    def mes(self, mes):
        return self.filter(entrada__month=mes)

    def ano(self, ano):
        return self.filter(entrada__year=ano)

    def reposicao(self, reposicao):
        return self.filter(reposicao=reposicao)

    def empresa(self, empresa):
        return self.filter(funcionario__departamento__empresa=empresa)
        
class Permanencia(models.Model):
    funcionario = models.ForeignKey(Funcionario, related_name='permanencias')
    entrada = models.DateTimeField('entrada', auto_now_add=True)
    saida = models.DateTimeField('saida', blank=True, null=True)
    reposicao = models.BooleanField(default=False)
    objects = PermanenciaQuerySet.as_manager()
    
    def hora_saida(self):
        return self.saida if self.saida is not None else timezone.now()
    
    @classmethod
    def nova_entrada(self, funcionario):
        try:
            if funcionario.permanencias.latest('entrada').saida is not None: #se a ultima permanencia tem uma saida
                Permanencia(funcionario=funcionario).save() #cria nova permanencia
            else:
                return "Certifique-se que sua ultima permanencia possui uma saida"
        except Permanencia.DoesNotExist: #primeira permanencia
            Permanencia(funcionario=funcionario).save()
        mensagem = "%s Entrada: " % funcionario.nome
        return mensagem + timezone.now().__str__() 
    
    @classmethod
    def nova_saida(self, funcionario):
        """
        escreve horario de saida na ultima permanencia, se nao possui horario de saida
        """
        try:
            p = funcionario.permanencias.latest('entrada')
            if p.saida is None: 
                p.saida = timezone.now()
                p.save()
            else:
                return "Faca uma entrada primeiro"
        except Permanencia.DoesNotExist:
            return "Nao existem permanencias"
        mensagem = "Saida %s registrada as " % funcionario.nome
        return mensagem + timezone.now().__str__() 