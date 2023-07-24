Este desafio tem como objetivo construir um Calendário WEB.

Requisitos obrigatórios:
- O seu projeto deve ser um sistema web. OK
- O calendário deverá permitir ao usuário criar, editar e remover eventos. OK
- Cada evento deverá possuir uma duração em dias. OK
- Os eventos deverão ser dispostos no calendário de forma que fique claro a sua duração.

Requisitos facultativos:
- Duração em horas.
- Recorrência de eventos.
- Possibilidade de adicionar eventos em outros fuso-horários.


Tive o intuito de cumprir todas as metas dentro do prazo, mas ficaram algumas pendencias, como por
exemplo a criação do calendario, com o Django Calendar - faltou a implementação dos campos. Na barra
deendereço do navegador é possivel atualizar o calendario digitando no formato(YYYY/MM-DD HH:MM:SS),
os requisitos facultativos ficaram sem resolução. Criei alguns relatórios de listagens de Local com
seus Eventos e Eventos e seus Locais e as telas de lançamentos de locais e eventos. O eventos lançados
por um usuário não poderão ser alterados ou excluidos por outro usuário, se for necessário faça o login
no painel administrativo digitando na barra de endereço localhost:8000/admin ou 127.0.0.1:8000/admin e
realoize o login com o usuário criado na instalçao, somente ele tem poder de acessa-lo. Os visitante
poderam ver os eventos, listar e consultar. Os usuários cadastrados poderam cadastrar, alterar e excluir
seus eventos. 

As publicações dos eventos deveram ser aprovados pelo usuário adminstrador atraves do Dashboar que se 
encontra no menu Area Restrita, na opção "Aprovar Eventos".

Procurei criar algumas recursos de segurança para evitar o aceeso a algumas páginas, como por exemplo
digitar na barra de endereço uma pagina restrita sem o usuário esta logado, são funções que precisam ser
implentadas e testadas com mais cuidado. Como disse o tempo era curto, mas me empolgo em realizar um projeto
e então meus lado planejador tomou posse. Aqui deixo um pouco do meu conhecimento de forma compartilhada para
todos.

Independentemente do resultado alcançado vou termina-lo atendendo todos os requisito solicitados, como
também criarei mais algumas funcionalidade como downloads da agenda de Eventosnos formatos txt, csv e
pdf, inserir imagem do Evento e convite de participantes solicitando confirmação. Essas implementações
adicionais tem como objetivo maior aprofundar meus conhecimentos e desenvolver o raciocionio criativo.

A aplicação está com um layout simples e funcional, onde pretendo melhorar a aparencia com Bootstrap.

A maior dificuldade que encontrei foi trabalhar com algumas funções de data, o python tem uma infinidade
de bibliotecas, mas acabei por descobrir que algumas nem são necessárias pois o Django já tem muitas
dela de forma nativa, procuro trabalhar com elas para evitar tornar a app inchada e mantendo uma simpli-
cidade na manutenção do código. Materia de Java script não é muito complicado para implementar o Calendar
do  Do DJango, mas como deixei para o final acabei estrapolando o tempo.

Me coloco a disposição para qualque esclaricimento, a.yuri@yahoo.com.br


                            Agradeso por realizar esse desafio!!!


*********************************************************************************************************
////////////// "O Homem nada sabe, mas é chamado a tudo conhecer" - Hermes Trimegistro  /////////////////
*********************************************************************************************************

Procedimento para instalação do Calendário na WEB
*********************************************************************************************************
Instale a versão 3.11 do **Python** / Versão do **Django** 4.2.3 / SO Linux Debian 12
Clone este repositório : `git clone https://github.com/virtusplmkrs/desafio_eventos.git`
Vá para o repositório : `cd desafio_eventos`
*********************************************************************************************************
001:    Crie um ambiente virtual
prompt/>    python3 -m virtualenv .env

002:    Ative o ambiente virtual no linux
prompt/>    source .env/bin/activate

003:    Atualize o pip do ambiente virtual / no linux
prompt/>    python -m pip install --upgrade pip

004:    Instale o Django
prompt/>    pip install django

005:    execute o makemigrations para criação do banco de dados
prompt/>    python manage.py makemigrations

006:    execute o migrate para efetivar as alterações
prompt/>    python manage.py migrate

007:    execute o createsuperuser para criar um usuário e ter acesso ao painel de controle
prompt/>    python manage.py createsuperuser

008:    execute o runserver para verificar se tudo está ok
prompt/>    python manage.py runserver

009:    digite na barra de endereço do navegador para acessar a agenda web
        http://127.0.0.1:8000/ ou localhost:8000

010:    digite na barra de endereço do navegador para acessar o painel de controle
        http://127.0.0.1:8000/ ou localhost:8000/admin



*********************************************************************************************************
Procedimento para uso do Calendário na WEB
*********************************************************************************************************
Para conseguir realizar os lançamentos você deve se cadastrar no sistema, através da opção Cadastrar no
menu area restrita.
Para lançar os eventos faz necessários cadastrar os locais onde ocorreram os eventos.
Lembre-se para que os eventos sejam visualizados tem que passar por aprovação do administrado, então loge
no sistema com com o usuário e senha usado na instalçãoo do programa e va na opção aprovar no 
menu Area restrita.

Viva lá vida!