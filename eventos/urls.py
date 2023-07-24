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
    path('', views.home, name='home'),
    path('<int:year>/<str:month>/', views.home, name='home'),
    path('eventos/', views.all_eventos, name='list-eventos'),
    path('add_local/', views.add_local, name='add-local'),
    path('list_local/', views.list_local, name='list-local'),
    path('Ficha_local/<local_id>/', views.ficha_local, name='ficha-local'),
    path('busca_local/', views.busca_local, name='busca-local'),
    path('update_local/<local_id>/', views.update_local, name='update-local'),
    path('add_evento/', views.add_evento, name='add-evento'),
    path('update_evento/<evento_id>/', views.update_evento, name='update-evento'),
    path('list_eventos/', views.list_eventos, name='list-evento'),
    path('delete_evento/<evento_id>/', views.delete_evento, name='delete-evento'),
    path('delete_local/<local_id>/', views.delete_local, name='delete-local'),
    path('meus_eventos/', views.meus_eventos, name='meus-eventos'),
    path('busca_eventos/', views.busca_eventos, name='busca-eventos'),
    path('admin_aprova/', views.admin_aprova, name='admin-aprova'),
    path('local_evento/<local_id>/', views.local_evento, name='local-evento'),
    path('evento_local/<evento_id>/', views.evento_local, name='evento-local'),
]
