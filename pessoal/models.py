from __future__ import unicode_literals

from django.db import models

class Empresa(models.Model):
    nome = models.CharField(max_length=150)
    def __str__(self):
        return self.nome

class Departamento(models.Model):
    empresa = models.ForeignKey(Empresa, related_name='departamentos')
    nome = models.CharField(max_length=150)
    def __str__(self):
        return self.nome

class FuncionarioQuerySet(models.QuerySet):
    def get_by_ra(self, ra):
        return self.get(ra=ra)

    def get_by_rfid(self, rfid):
        return self.get(rfid=rfid)

    def get_by_nome(self, nome):
        return self.filter(nome__icontains=nome) #icontains(like ignore case)

    def get_by_empresa(self, empresa):
        return self.filter(departamento__empresa=empresa)

class Funcionario(models.Model):
    ra = models.PositiveIntegerField(primary_key=True)
    nome = models.CharField(max_length=150)
    rfid = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento)
    objects = FuncionarioQuerySet.as_manager()
    def __str__(self):
        return self.nome