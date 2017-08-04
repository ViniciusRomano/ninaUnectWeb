from django.contrib import admin

from .models import Funcionario
from .models import Departamento
from .models import Empresa
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('ra', 'nome', 'departamento','rfid')
    list_filter = ('departamento',)
    search_fields = ('ra', 'nome')

class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'empresa')

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome',)

admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Empresa, EmpresaAdmin)