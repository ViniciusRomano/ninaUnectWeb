from django.contrib import admin
from .models import Funcionario
from .models import Permanencia

class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('ra', 'nome', 'rfid')

class PermanenciaAdmin(admin.ModelAdmin):
    list_display = ('funcionario', 'entrada', 'saida')
    list_filter = ('funcionario', 'entrada')

# Register your models here.
admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Permanencia, PermanenciaAdmin)