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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('eventos.urls')),
    path('membros/', include('django.contrib.auth.urls')),
    path('membros/', include('membros.urls')),
]

admin.site.site_header = "Painel ADM"
admin.site.site_title = "Agenda de Eventos|"
admin.site.index_title = ""