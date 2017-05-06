from django.db import models
from django.utils import timezone

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class Funcionario(models.Model):
    ra = models.PositiveIntegerField(primary_key=True)
    nome = models.CharField(max_length=150)
    rfid = models.CharField(max_length=100)
    
    def marcar_entrada(self):
        "cria uma nova permanencia se a ultima foi fechada"
        try:
            p = Permanencia.objects.filter(funcionario=self).latest('entrada')
            if p.saida != None:
                Permanencia(funcionario=self).save()
            else:
                print ("Certifique-se que sua ultima entrada possui uma saida")
        except Permanencia.DoesNotExist:
            Permanencia(funcionario=self).save()
        
    def marcar_saida(self):
        "escreve horario de saida na ultima permanencia, se a mesma nao possui horario de saida"
        p = Permanencia.objects.filter(funcionario=self).latest('entrada')
        if p.saida == None:
            p.saida = timezone.now()
            p.save()
        else:
            print ("Faca uma entrada primeiro")

    def __unicode__(self):
        return self.nome

class Permanencia(models.Model):
    funcionario = models.ForeignKey(Funcionario)
    entrada = models.DateTimeField('entrada', auto_now_add=True)
    saida = models.DateTimeField('saida', blank=True, null=True)