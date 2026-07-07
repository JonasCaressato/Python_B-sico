"""
Enunciado Exercício 32 – Ano Bissexto

Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
"""

print('Descubra se o ano é bissexto!')
n1 = int(input('Digite um ano: '))
n2 = str(n1)[-2:]

if n2 == '00':
    if n1 % 400 == 0:
        print('Bissexto!')
    else:
        print('Não é Bissexto!')
elif n1 % 4 == 0:
    print('Bissexto!')
else:
    print('Não é Bissexto!')
