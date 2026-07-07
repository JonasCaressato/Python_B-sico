"""
Enunciado Exercício 35 – Analisando Triângulo v1.0

Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.
"""

print('Descubra se três retas formam um triângulo')

lado_1 = int(input('Digite a primeira reta: '))
lado_2 = int(input('Digite a segunda reta: '))
lado_3 = int(input('Digite a terceira reta: '))

if lado_1 < lado_2 + lado_3 and lado_2 < lado_1 + lado_3 and lado_3 < lado_2 + lado_1:
    print(f'FORMAM UM TRIANGULO!')
else:
    print(f'NÃO FORMAM UM TRIANGULO!')
