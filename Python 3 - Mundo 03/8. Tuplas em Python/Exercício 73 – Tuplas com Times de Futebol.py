"""
Enunciado Exercício 73 – Tuplas com Times de Futebol

Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.
"""

campeonato_brasileiro_2021 = (
'Atlético Mineiro',
'Flamengo',
'Palmeiras',
'Fortaleza',
'Corinthians',
'Red Bull Bragantino',
'Fluminense',
'America',
'Atlético',
'Santos',
'Ceará',
'Internacional',
'São Paulo',
'Athletico Paranaense',
'Cuiabá',
'Juventude',
'Grêmio',
'Bahia',
'Sport',
'Chapecoense')

#Mostrando os cinco primeiros colocados
print('Os cinco primeiros colocados do Campeonato Brasileiro de 2021 são: ')
for n in range(0,5):
    print(f'{campeonato_brasileiro_2021[n]}')
print('-' * 40)

#Mostrandos os rebaixos do campeonato
print('Os Rebaixados do Campeonato Brasileiro de 2021 são: ')
for n in range(16, 20):
    print(f'{campeonato_brasileiro_2021[n]}')
print('-' * 40)

#Organizando e mostrando os times em ordem alfabética
print('Times em ordem alfabética: ')
print(f'{sorted(campeonato_brasileiro_2021)}')
print('-' * 40)

#Procurando a posição da Chapecoense
print(f'A Chapecoense está na posição: {campeonato_brasileiro_2021.index('Chapecoense') + 1}')
