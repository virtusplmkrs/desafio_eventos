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


from django.urls import path
from . import views

urlpatterns = [
    path('login_usuario', views.login_user, name='login'),
    path('logout_usuario', views.logout_user, name='logout'),
    path('cadastro_usuario', views.register_user, name='register_user'),
]
