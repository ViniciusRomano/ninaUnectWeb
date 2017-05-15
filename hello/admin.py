from django.contrib import admin
from .models import Funcionario
from .models import Permanencia
from .models import Departamento

class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('ra', 'nome', 'departamento','rfid')
    list_filter = ('departamento',)
    search_fields = ('ra', 'nome')

class PermanenciaAdmin(admin.ModelAdmin):
    list_display = ('funcionario', 'entrada', 'saida', 'reposicao')
    list_filter = ('entrada', 'reposicao')
    search_fields = ('funcionario__nome', 'funcionario__ra', 'entrada')

class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nome',)

# Register your models here.
admin.site.register(Permanencia, PermanenciaAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Funcionario, FuncionarioAdmin)