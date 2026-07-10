"""
Enunciado Exercício 39 – Alistamento Militar

Faça um programa que leia o ano de nascimento de um jovem e informe,
conforme a sua idade, se ele ainda vai se alistar ao serviço militar(<18),
se é a hora exata de se alistar(=18) ou se já passou do tempo do alistamento(>18).
O seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

#Obtendo a data atual
from datetime import date

ano_atual = date.today().year

ano_de_nascimento = int(input('Digite seu ano de nascimento: '))

idade = ano_atual - ano_de_nascimento

if idade < 18:
    print('Ainda não é o momento de se alistar.')
    print(f'Ainda falta {(18 - idade)} anos para o seu alistamento.')
elif idade == 18:
    print('Você está no momento exato de se alistar.')
elif idade > 18:
    print('Você passou do período de alistamento.')
    print(f'O seu alistamento está {(idade - 18)} anos atrasado.')
