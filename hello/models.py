from django.db import models
from django.utils import timezone
from django.db.models import Manager
from django.db.models.query import QuerySet

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class Departamento(models.Model):
    nome = models.CharField(max_length=150)
    def __unicode__(self):
        return self.nome

class FuncionarioManager(models.Manager):
    pass

class FuncionarioQuerySet(models.query.QuerySet):
    def get_by_ra(self, ra):
        return self.filter(ra=ra).first()

    def get_by_rfid(self, rfid):
        return self.filter(rfid=rfid).first()

    def get_by_nome(self, nome):
        return self.filter(nome__icontains=nome) #icontains(like ignore case)

class Funcionario(models.Model):
    ra = models.PositiveIntegerField(primary_key=True)
    nome = models.CharField(max_length=150)
    rfid = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento)
    objects = FuncionarioManager.from_queryset(FuncionarioQuerySet)()

    def __unicode__(self):
        return self.nome

class PermanenciaManager(models.Manager):
    pass

class PermanenciaQuerySet(models.query.QuerySet):
    def get_by_data(self, dia, mes, ano):
        return Permanencia.objects.filter(entrada__day=dia, entrada__month=mes, entrada__year=ano)

    def get_by_funcionario(self, ra):
        return Permanencia.objects.filter(funcionario__ra=ra)

    def nova_entrada(self, ra):
        """
        cria uma nova permanencia se a ultima foi fechada
        """
        try:
            funcionario = Funcionario.objects.get_by_ra(ra)
            if Permanencia.objects.get_by_funcionario(ra).latest('entrada').saida != None: #se a ultima permanencia tem uma saida
                Permanencia(funcionario=funcionario).save() #cria nova permanencia
            else:
                return "Certifique-se que sua ultima permanencia possui uma saida"
        except Permanencia.DoesNotExist: #primeira permanencia
            Permanencia(funcionario=funcionario).save()
        return "Entrada realizada"

    def nova_saida(self, ra):
        """
        escreve horario de saida na ultima permanencia, se nao possui horario de saida
        """
        try:
            p = self.filter(funcionario__ra=ra).latest('entrada')
            if p.saida == None:
                p.saida = timezone.now()
                p.save()
            else:
                return "Faca uma entrada primeiro"
        except Permanencia.DoesNotExist:
            return "Nao existem permanencias"
        return "Saida realizada"

class Permanencia(models.Model):
    funcionario = models.ForeignKey(Funcionario)
    entrada = models.DateTimeField('entrada', auto_now_add=True)
    saida = models.DateTimeField('saida', blank=True, null=True)
    reposicao = models.BooleanField(default=False)
    objects = PermanenciaManager.from_queryset(PermanenciaQuerySet)()