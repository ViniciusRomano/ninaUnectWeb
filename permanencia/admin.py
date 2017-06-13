from django.contrib import admin

from .models import Permanencia

class PermanenciaAdmin(admin.ModelAdmin):
    list_display = ('funcionario', 'entrada', 'saida', 'reposicao')
    list_filter = ('entrada', 'reposicao')
    search_fields = ('funcionario__nome', 'funcionario__ra', 'entrada')

admin.site.register(Permanencia, PermanenciaAdmin)