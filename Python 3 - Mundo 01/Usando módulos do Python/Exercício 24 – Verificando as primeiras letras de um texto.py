"""
Enunciado Exercício 24 – Verificando as primeiras letras de um texto

Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
"""

cidade = str(input('Em qual cidade você nasceu?: '))

#
primeiro_nome = cidade[:5]
if primeiro_nome.upper() == 'SANTO':
    print(f'Sua cidade de nascimento começa com SANTO')
else:
    print(f'Sua cidade não começa com SANTO')
