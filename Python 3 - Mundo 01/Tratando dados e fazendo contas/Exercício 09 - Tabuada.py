"""
Enuciado exercício 09 - Tabuada:

Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
"""

numero =  int(input('Digite um numero para ver sua tabuada: '))
print('-' * 30)
for n in range (1, 11):
    print(f'{numero} x {n} = {numero * n}')

print('-' * 30)