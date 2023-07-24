":*******************************************************************************************:"
" Application: Agenda de Eventos                                               Eventos (\/¬) :"
" Date       : __/__/____                                           Versão: DjPy: 01.00.00-X :"
" Dev        :                                                                               :"
" Description:                                                                               :"
":*******************************************************************************************:"
" Application: Agenda de Eventos                                               Eventos (\/¬) :"
" Date       : 21/07/2023                                           Versão: DjPy: 01.00.00-X :"
" Dev        : Alexandre Yuri                                                                :"
" Description: Create version Master                                                         :"
":*******************************************************************************************:"


from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Local
from .models import MyEventoUser
from .models import Evento

#admin.site.register(Local)
admin.site.register(MyEventoUser)
#admin.site.register(Evento)

admin.site.unregister(Group)


@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'fone')
    ordering = ('nome',)
    search_fields = ('nome', 'endereco')

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    fields = (('nome', 'local'), 'data_evento', 'data_final', 'descricao', 'promoter', 'aprovado')
    list_display = ('nome', 'data_evento', 'local')
    list_filter = ('data_evento', 'local')
    ordering = ('-data_evento',)