"""
Enunciado Exercício 41 – Classificando Atletas

A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
e mostre a sua categoria, conforme a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER
"""

from datetime import date
ano_atual = date.today().year

ano_de_nascimento = int(input('Seu ano de nascimento: '))

if ano_atual - ano_de_nascimento <= 9:
    print('Atleta MIRIM')
elif 9 < ano_atual - ano_de_nascimento <= 14:
    print('Atleta INFANTIL')
elif 14 < ano_atual - ano_de_nascimento <= 19:
    print('Atleta JÚNIOR')
elif 19 < ano_atual - ano_de_nascimento <= 25:
    print('Atleta SÊNIOR')
elif ano_atual - ano_de_nascimento > 25:
    print('Atleta MASTER')

